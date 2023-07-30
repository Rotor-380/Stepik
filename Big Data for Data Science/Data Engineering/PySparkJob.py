import io
import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType


def process(spark, input_file, target_path):
    df_clickstream = spark.read.parquet(input_file)  # загрузка данных

    # Создание датасета с требуемыми данными
    result_df = df_clickstream.select('date', 'ad_id', 'target_audience_count', 'has_video', 'ad_cost', 'ad_cost_type')

    # создаём колонку 'is_cpm', где значение принимает 1 если тип объявления CPM, иначе 0
    result_df = result_df.withColumn('is_cpm', (F.col('ad_cost_type') == 'CPM').cast(IntegerType()))

    # создаём колонку 'is_cpc', где значение принимает 1 если тип объявления CPM, иначе 0
    result_df = result_df.withColumn('is_cpc', (F.col('ad_cost_type') == 'CPC').cast(IntegerType()))

    # создаём колонку 'day_count' - Число дней, которое показывалась реклама
    result_df = result_df.withColumn('day_count', F.count('date').over(Window.partitionBy('ad_id')))

    # Добавим в оригинальный датасет колонки 'clicks' и 'views'
    df_clickstream = df_clickstream.withColumn('clicks', (F.col('event') == 'click').cast(IntegerType()))
    df_clickstream = df_clickstream.withColumn('views', (F.col('event') == 'view').cast(IntegerType()))

    # Добавим колонки 'total_clicks' и 'total_views' в оригинальный датасет в которых будет содержаться сумма кликов и просмотров для каждого объявления
    df_clickstream = df_clickstream.withColumn('total_clicks', F.sum('clicks').over(Window.partitionBy('ad_id')))
    df_clickstream = df_clickstream.withColumn('total_views', F.sum('views').over(Window.partitionBy('ad_id')))

    # Добавим колонку 'CTR' в оригинальный датасет
    df_clickstream = df_clickstream.withColumn('CTR', F.col('total_clicks') / F.col('total_views'))

    # Добавим колонку 'CTR' в 'result_df'
    result_df = result_df.join(df_clickstream.select('ad_id', 'CTR'), on='ad_id', how='left')

    # так как в итоговом датасете отсутствуют колонки event и platform, то возникает видмость дублей, удалим их
    result_df = result_df.dropDuplicates()

    # Разделим данные, как указано в задании в следующем соотношении train/test = 0.75/0.25
    train, test = result_df.randomSplit([0.75, 0.25])

    # сохранение данных
    train_path = target_path + "/train"
    test_path = target_path + "/test"
    train.write.parquet(train_path)
    test.write.parquet(test_path)

def main(argv):
    input_path = argv[0]
    print("Input path to file: " + input_path)
    target_path = argv[1]
    print("Target path: " + target_path)
    spark = _spark_session()
    process(spark, input_path, target_path)


def _spark_session():
    return SparkSession.builder.appName('PySparkJob').getOrCreate()


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) != 2:
        sys.exit("Input and Target path are require.")
    else:
        main(arg)
