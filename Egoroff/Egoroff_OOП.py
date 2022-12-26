# class Lion:
#     def roar(self):
#         roar = "Rrrrrrr!!!"
#         print(roar)
#
#
# simba = Lion()
# simba.roar() ##

# class Counter:
#     def start_from(self, x=0):
#         self.x = x
#
#     def increment(self):
#         self.x += 1
#
#     def display(self):
#         print(f'Текущее значение счетчика = {self.x}')
#
#     def reset(self):
#         self.x = 0
#
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display()  # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display()  # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display()  # печатает "Текущее значение счетчика = 0"
# c2 = Counter()
# c2.start_from(3)
# c2.display()  # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display()  # печатает "Текущее значение счетчика = 4"


# class Point:
#     def set_coordinates(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def get_distance(self, point2):
#         print(((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5) if isinstance(point2, Point) else print("Передана не точка")
#         #print( [ "Передана не точка", (((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5) ][isinstance(point2, Point)] )
#
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2)  # вернёт 5.0
# p1.get_distance('10')


# class Laptop:
#     def __init__(self, brand=None, model=None, price=None):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{self.brand} {self.model}'
#     # def laptop_name(self):
#     #     print(f'{self.brand} {self.model}')
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"

# class SoccerPlayer:
#     def __init__(self, name, surname, goals=0, assists=0):
#         self.goals = goals
#         self.assists = assists
#         self.name = name
#         self.surname = surname
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"

# class Zebra:
#     def __init__(self):
#         self.stripe = ["Полоска белая", "Полоска черная"]
#
#     def which_stripe(self):
#         print(self.stripe[0])
#         self.stripe[0], self.stripe[1] = self.stripe[1], self.stripe[0]
# #
#
# z1 = Zebra()
# z1.which_stripe()  # печатает "Полоска белая"
# z1.which_stripe()  # печатает "Полоска черная"
# z1.which_stripe()  # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe()  # печатает "Полоска белая"
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#     def is_adult(self):
#         return self.age >= 18
#
#
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult())  # выводит "True"
# class Dog:
#     def __init__(name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         retutn (f"{self.name} is {self.age} years old")
#
#     def speak (self, sound):
#         return (f"{self.name} says {sound}")
#
# jack = Dog("Jack", 4)
#
# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'
# class Stack():
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         #self.items = item
#         self.values.append(item)
#
#     def pop(self):
#         return self.values.pop(-1) if len(self.values) != 0 else print("Empty Stack")
#
#     def peek(self):
#         return self.values[-1] if len(self.values) != 0 else print("Empty Stack")
#
#     def is_empty(self):
#         return len(self.values) == 0
#
#     def size(self):
#         return len(self.values)
#
#
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
# print(s.size())  # распечатает 2
# class UserMail:
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, mail):
#         lin = ''.join(a for a in filter(lambda l: '@' in l and l.count('@') == 1, [mail]) if '.' in a.split('@')[1])
#         self.__email = lin if len(lin) != 0 else print("Ошибочная почта")
#
#     email = property(fget=get_email, fset=set_email)
# #
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3]  # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.q)  # prince@still.wait
# print(UserMail.__dict__)

# 2.5 Публичные, приватные, защищенные атрибуты и методы
class Student:
    def __init__(self,  name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch =branch

    def __display_details(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')

    def access_private_method(self):
        return self.__display_details()

obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()

# class Money:
#
#     def __init__(self, dollar=0, cent=0):
#         self.total_cents = dollar * 100 + cent
#
#     @classmethod
#     def verify_dollars(cls, x):
#         if type(x) != int or x < 0:
#             print("Error dollars")
#             return False
#         return True
#
#     @classmethod
#     def verify_cents(cls, y):
#         if type(y) != int or y > 100 or y < 0:
#             print("Error cents")
#         return True
#
#     @property
#     def dollars(self):
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, doll):
#         # print('setter get:', doll, type(doll))
#         if self.verify_dollars(doll):
#             self.total_cents = doll * 100 + self.cents
#             # print(self.total_cents)
#
#     @property
#     def cents(self):
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, cen):
#         if self.verify_cents(cen):
#             self.total_cents = self.dollars * 100 + cen
#
#     def __str__(self):
#         return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


# Bill = Money(101, 101)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# # print(Bill.total_cents)
# print(Bill.dollars, Bill.cents)  # 101 99
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

# 3.2 Магические методы __len__ и __abs__
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name + self.surname)
#
#
# # 3.3 Магические методы __add__, __mul__, __sub__ и __truediv__
#
# class BankAccount:
#     def __init__(self, name, balance):
#         print('New object init', '>', name)
#         self.name = name
#         self.balance = balance
#
#     def __repr__(self):
#         return f'Client {self.name} balance {self.balance}'
#
#     def __add__(self, other):
#         if isinstance(other, BankAccount):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             print('metod __ADD__ was called')
#             # return self.balance + other
#             return BankAccount(self.name, self.balance + other)
#         raise NotImplemented
#
#     def __radd__(self, other):
#         print('__radd__ was called')
#         return self + other


# t = BankAccount('ivan', 200)
# print(t+30)
#
# class Vector:
#     def __init__(self, *args):
#         self.values = sorted(i for i in args if isinstance(i, int))
#
#     def __str__(self):
#         return f'Вектор{tuple(self.values)}' if len(self.values) > 0 else "Пустой вектор"
#
#     def __len__(self):
#         return len(self.values)
#
#     #  @classmethod
#     # def __verifay_data(cls, var):
#
#     def __add__(self, var):
#         if isinstance(var, Vector):
#             if len(self.values) != len(var.values):
#                 print("Сложение векторов разной длины недопустимо")
#             else:
#                 return Vector(*list(map(lambda x, y: x + y, self.values, var.values)))
#         if isinstance(var, int):
#             return Vector(*list(map(lambda x: x + var, self.values)))
#         if not isinstance(var, (Vector, int)):
#             print(f'Вектор нельзя сложить с {var}')
#         # return self.values + var
#
#     def __radd__(self, other):
#         return self + other
#
#     def __mul__(self, var):
#         if isinstance(var, Vector):
#             if len(self.values) != len(var.values):
#                 print("Умножение  векторов разной длины недопустимо")
#             else:
#                 return Vector(*list(map(lambda x, y: x * y, self.values, var.values)))
#         if isinstance(var, int):
#             return Vector(*list(map(lambda x: x * var, self.values)))
#         if not isinstance(var, (Vector, int)):
#             print(f'Вектор нельзя умножать с {var}')


# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
# print(v2 + 7)
# v3 = v1 + 'rrr'
# v3 = v1 + v2
# print(v3)  # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4)
# v5 = v1 * 2
# print(v5)  # печатает "Вектор(2, 4, 6)"
# v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"


# 3.4 Специальные методы сравнения объектов классов


# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#     def __eq__(self, other):
#         print('__eq__ call')
#         if isinstance(other, Rectangle):
#             return self.a == other.a and self.b == other.b
#
#     def __lt__(self, other):
#         print('__lt__ call')
#         if isinstance(other, Rectangle):
#             return self.area < other.area
#         elif isinstance(other, (int, float)):
#             return self.area < other
#
#     def __le__(self, other):
#         return self == other or self < other


class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    @classmethod
    def __verifay_data(cls, other):
        if not isinstance(other, (ChessPlayer, int)):
            return ('Невозможно выполнить сравнение')
        return other if isinstance(other, int) else other.rating

    def __eq__(self, other):
        r_t = self.__verifay_data(other)
        return self.rating == r_t if type(r_t) is int else r_t

    def __gt__(self, other):
        r_t = self.__verifay_data(other)
        return self.rating > r_t if type(r_t) is int else r_t

    def __lt__(self, other):
        r_t = self.__verifay_data(other)
        return self.rating < r_t if type(r_t) is int else r_t


# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000) # False
# print(ian == 2789) # True
# print(magnus == ian) # False
# print(magnus > ian) # True
# print(magnus < ian) # False
# print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"
# print(ian == [1,2])
# print(ian == magnus)

from functools import total_ordering


@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


# acc1 = Account(10)
# acc2 = Account(20)
# print(acc1 > acc2)
# print(acc1 < acc2)
# print(acc1 == acc2)
# print(acc1 != acc2)
# print(acc1 >= acc2)
# print(acc1 <= acc2)
# 16. Магические методы __eq__ и __hash__

# 3.6 Магический метод __bool__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self.x - self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


p1 = Point(3, 5)


# print(bool(p1))

class Quadrilateral:
    def __init__(self, width, height=0):
        self.width = width
        self.height = height
        if self.height == 0:
            self.height = self.width

    def __str__(self):
        return (f'Куб размером {self.width}х{self.width}') if self.height == self.width else (
            f'Прямоугольник размером {self.width}х{self.height}')

    def __bool__(self):
        return self.height == self.width


# q1 = Quadrilateral(10)
# print(q1)  # печатает "Куб размером 10х10"
# print(bool(q1))  # печатает "True"
# q2 = Quadrilateral(3, 5)
# print(q2)  # печатает "Прямоугольник размером 3х5"
# print(q2 == True)  # печатает "False"

# 3.7 Магический метод __call__

class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.lenght = 0
        # print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.lenght += len(args)
        # print('object called', self.counter)

    def average(self):
        return self.summa / self.lenght


b = Counter()
# print(b)
# print(b)

# b()
# b(1,2)
# b(3,4,5)
# print(b.average())
from time import perf_counter as pc


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = pc()
        # print('function call', self.fn.__name__)
        result = self.fn(*args, **kwargs)
        finish = pc()
        # print('work time =', finish - start)
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


def fib(n):
    if n <= 2: return 1
    return fib(n - 1) + fib(n - 2)


# fact = Timer(fact)

# print(Timer(fib)(30))

class Addition:
    def __init__(self):
        self.summa = 0

    def __call__(self, *args):
        x = list(filter(lambda x: isinstance(x, (int, float)), args))
        self.summa += sum(x)
        print(f"Сумма переданных значений = {self.summa}")
        self.summa = 0


add = Addition()


# add(10, 20) # печатает "Сумма переданных значений = 30"
# add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
# add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"

# 3.8 Полиморфизм в Python
#
# class UnitedKingdom:
#
#     @staticmethod
#     def capital():
#         print("London is the capital of Great Britain.")
#
#     @staticmethod
#     def language():
#         print("English is the primary language of Great Britain.")
#
#
# class Spain:
#
#     @staticmethod
#     def capital():
#         print("Madrid is the capital of Spain.")
#
#     @staticmethod
#     def language():
#         print("Spanish is the primary language of Spain.")
#
#
# obj_uk = UnitedKingdom()
# obj_spa = Spain()
# for country in (obj_spa, obj_uk):
#     country.capital()
#     country.language()

# 3.9 Методы __getitem__ , __setitem__ и __delitem__

class Vector:

    def __init__(self, *args):
        self.value = list(args)

    def __repr__(self):
        return str(self.value)

    def __getitem__(self, item):
        if 0 <= item < len(self.value):
            return self.marks[item]
        else:
            raise IndexError('Index error')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Index mast be INT >0')
        if key >= len(self.value):
            off = key + 1 - len(self.value)
            self.value.extend([None] * off)
        self.value[key] = value


# 3.10 Магические методы __iter__ и __next__

class Marks:
    def __init__(self, val):
        self.val = val
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.val):
            self.index = 0
            raise StopIteration
        letter = self.val[self.index]
        self.index += 1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


l = Marks([3, 4, 5, 3, 4])
igor = Student('Igor', 'Bulkin', l)


# print(igor.__dict__)
# for i in igor:
#     print(i)

class PowerTwo:
    def __init__(self, x):
        self.stop = x
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        # if self.start == self.stop:
        #     raise StopIteration
        # else:
        self.start += 1
        return self.start * 10


# for i in PowerTwo(4): # итерируемся до 4й степени двойки
#     print(i)
numbers = PowerTwo(2)

iterator = iter(numbers)


# print(next(iterator)) # печатает 1
# print(next(iterator)) # печатает 2
# print(next(iterator)) # печатает 4
# print(next(iterator)) # исключение StopIteration


class NewInt(int):
    def repeat(self, x=2):
        return int(str(self) * x)

    def to_bin(self):
        return bin(self)[2:]


# a = NewInt(9)
# print(a.repeat(3))  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3)) # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

# 4.5 Делегирование в Python

class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue, kind='Car'):
        super().__init__(brand, max_speed, mileage)
        self.kind = kind
        self.__gasoline_residue = gasoline_residue
        self.mileage = mileage

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int) and value >= 0:
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name, kind='Boat'):
        super().__init__(brand, max_speed)
        self.kind = kind
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity, kind='Plane'):
        super().__init__(brand, max_speed)
        self.kind = kind
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
#
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
#
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

class Initialization:
    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')
            # self.capacity = 0
            # self.food = 0


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"

class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"

class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    @classmethod
    def __verifay_data(cls, other):
        if not isinstance(other, (object, int)):
            return f'Невозможно сравнить количество сладкоежек с {other}'
        return other if isinstance(other, int) else other.capacity

    def __eq__(self, other):
        r_t = self.__verifay_data(other)
        return self.capacity == r_t if type(r_t) is int else r_t

    def __gt__(self, other):
        r_t = self.__verifay_data(other)
        return self.capacity > r_t if type(r_t) is int else r_t

    def __lt__(self, other):
        r_t = self.__verifay_data(other)
        return self.capacity < r_t if type(r_t) is int else r_t


# v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
# v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
# # print('*****v_second*****', v_second)
# m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
# s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
# print(s_first > m_first)  # True
# print(30000 == s_first)  # True
# print(s_first == 25000)  # False
# print(100000 < s_first)  # False
# print(100 < s_first)  # True


#4.6 Множественное наследование в Python. Multiple inheritance in Python

class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('I now medicine')

    def can_build(self):
        print("I'm a doctor i can build, but badly")

class Builder():
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('I mow know how to build')
    def can_build(self):
        print('I can build very vell')

class Person(Builder,Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self,degree)
    def __str__(self):
        return f'Person {self.rank} {self.degree}'

s = Person(5, 'spec')
# print(s)

