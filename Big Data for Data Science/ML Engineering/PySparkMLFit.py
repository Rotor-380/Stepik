import io
import sys

from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression, DecisionTreeRegressor, GBTRegressor, RandomForestRegressor
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
import random

random.seed(1234)

# Используйте как путь куда сохранить модель
MODEL_PATH = 'spark_ml_model'


def process(spark, train_data, test_data):
    #train_data - путь к файлу с данными для обучения модели
    #test_data - путь к файлу с данными для оценки качества модели
    #Ваш код

    df_train = spark.read.parquet(train_data)
    df_test = spark.read.parquet(test_data)

    df_train = df_train.drop('is_cpc')
    df_test = df_test.drop('is_cpc')

    feature = VectorAssembler(inputCols=df_train.columns[:-1],outputCol="features")
    
    # Создание моделей
    lr = LinearRegression(labelCol="ctr", featuresCol="features") # линейная регрессия добавлена как некий бейзлайн
    dt = DecisionTreeRegressor(featuresCol='features', labelCol='ctr') # дерево решений 
    gbt = GBTRegressor(featuresCol='features', labelCol='ctr') # градиентный бустинг
    rf = RandomForestRegressor(featuresCol='features', labelCol='ctr') # случайный лес
    
    # Создание сеток гиперпараметров для моделей
    lr_paramGrid = ParamGridBuilder()\
                                    .addGrid(lr.maxIter, [ 10, 15, 20 ])\
                                    .addGrid(lr.regParam, [0.001, 0.01, 0.1])\
                                    .addGrid(lr.elasticNetParam, [0.001, 0.01, 0.1]).build()
    dt_paramGrid = ParamGridBuilder()\
                                    .addGrid(dt.maxDepth, [1, 3, 7])\
                                    .addGrid(dt.maxBins, [ 64, 128, 256 ])\
                                    .addGrid(dt.minInfoGain, [0.0, 0.1, 0.2])\
                                    .addGrid(dt.minInstancesPerNode, [1, 2, 3]).build()
    gbt_paramGrid = ParamGridBuilder()\
                                    .addGrid(gbt.maxDepth, [3, 5, 9 ])\
                                    .addGrid(gbt.maxBins, [ 128, 256, 300 ])\
                                    .addGrid(gbt.minInstancesPerNode, [1, 3, 7 ])\
                                    .addGrid(gbt.maxIter, [ 25, 50, 100 ]).build()
    rf_paramGrid = ParamGridBuilder()\
                                    .addGrid(rf.maxDepth, [ 10, 15, 25 ])\
                                    .addGrid(rf.maxBins, [200, 256, 300 ])\
                                    .addGrid(rf.minInstancesPerNode, [1, 3, 6 ])\
                                    .addGrid(rf.numTrees, [ 25, 50, 100 ]).build()

    lr_pipeline = Pipeline(stages=[feature, lr])
    dt_pipeline = Pipeline(stages=[feature, dt])
    gbt_pipeline = Pipeline(stages=[feature, gbt])
    rf_pipeline = Pipeline(stages=[feature, rf])
    
    # Создание кросс-валидаторов
    lr_crossval = CrossValidator(estimator=lr_pipeline, 
                                 estimatorParamMaps=lr_paramGrid, 
                                 evaluator=RegressionEvaluator(labelCol="ctr", 
                                                               predictionCol="prediction", 
                                                               metricName="rmse"), 
                                 numFolds=3)
    dt_crossval = CrossValidator(estimator=dt_pipeline, 
                                 estimatorParamMaps=dt_paramGrid, 
                                 evaluator=RegressionEvaluator(labelCol="ctr", 
                                                               predictionCol="prediction", 
                                                               metricName="rmse"), 
                                 numFolds=3)
    gbt_crossval = CrossValidator(estimator=gbt_pipeline, 
                                  estimatorParamMaps=gbt_paramGrid, 
                                  evaluator=RegressionEvaluator(labelCol="ctr", 
                                                                predictionCol="prediction", 
                                                                metricName="rmse"), 
                                  numFolds=3)
    rf_crossval = CrossValidator(estimator=rf_pipeline, 
                                 estimatorParamMaps=rf_paramGrid, 
                                 evaluator=RegressionEvaluator(labelCol="ctr", 
                                                               predictionCol="prediction", 
                                                               metricName="rmse"), 
                                 numFolds=3)

    # Обучаем модели 
    cv_Model_lr = lr_crossval.fit(df_train)
    cv_Model_dt = dt_crossval.fit(df_train)
    cv_Model_gbt = gbt_crossval.fit(df_train)
    cv_Model_rf = rf_crossval.fit(df_train)

    # Предсказание на тестовой выборке
    predictions_lr = cv_Model_lr.transform(df_test)
    predictions_dt = cv_Model_dt.transform(df_test)
    predictions_gbt = cv_Model_gbt.transform(df_test)
    predictions_rf = cv_Model_rf.transform(df_test)

    # Вычисление RMSE для каждой модели
    evaluator = RegressionEvaluator(labelCol="ctr", predictionCol="prediction", metricName="rmse")
    
    rmse_lr = evaluator.evaluate(predictions_lr)
    rmse_dt = evaluator.evaluate(predictions_dt)
    rmse_gbt = evaluator.evaluate(predictions_gbt)
    rmse_rf = evaluator.evaluate(predictions_rf)

    # Выбор лучшей модели
    models = [(cv_Model_lr, rmse_lr, 'Linear Regression'), 
              (cv_Model_dt, rmse_dt, 'Decision Tree'), 
              (cv_Model_gbt, rmse_gbt, 'Gradient-Boosted Trees'),
              (cv_Model_rf, rmse_rf, 'Random Forest')]
    best_model, best_rmse, best_model_name = min(models, key=lambda model: model[1])

    print(f"Best model is: '{best_model_name}' with RMSE = {best_rmse}")

    # Сохранение лучшей модели
    best_model.bestModel.write().overwrite().save(MODEL_PATH) # перезапись, на всякий случай

def main(argv):
    train_data = argv[0]
    print("Input path to train data: " + train_data)
    test_data = argv[1]
    print("Input path to test data: " + test_data)
    spark = _spark_session()
    process(spark, train_data, test_data)


def _spark_session():
    return SparkSession.builder.appName('PySparkMLFitJob').getOrCreate()


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) != 2:
        sys.exit("Train and test data are require.")
    else:
        main(arg)
