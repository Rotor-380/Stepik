# m = 'prince@still.wait'
#
# # lin = list(a for a in filter(lambda l: '@' in l ,m.lower().split()) if '.' in a.split('@')[1])
# # print(*list(filter(lambda r: r not in list(j for i in [lin] for j in i for k in '!"#$%&\'()+,-/:;<=>?[\]^`{|}~' if k in j ) ,lin)))
#
#
# lin = list(a for a in filter(lambda l: '@' in l and l.count('@') == 1, [m]) if '.' in a.split('@')[1])
# print(lin)
# #print(*list(filter(lambda r: r not in list(j for i in [lin] for j in i for k in '!"#$%&\'()+,-/:;<=>?[\]^`{|}~' if k in j ) ,lin)))


# import numpy as np
# # a = np.array([[1,2,3], [4,2,1], [1,0,1]])
# # b = np.array([[1,2,1], [1,-1,2], [1,2,1]])
# # c = np.array([[2,2], [1,4]])
# # d = np.array([[3,1], [2,1], [-1,2]])
# # g = np.array([[1,1,2,3], [4,2,1,3], [2,1,2,3], [1,2,5,4]])
# # print(np.transpose(d))
# # print(np.linalg.det(c))
# # print(np.linalg.det(a))
# # print(np.linalg.det(g))
# # # print(np.dot(a, b), '\n','\n', np.dot(b, a), '\n','\n', np.dot(a, d), '\n','\n', np.dot(b, d), '\n','\n', np.dot(d,c))
# # # print(np.dot(a, b)[0, 1],  np.dot(b, a)[0, 1], np.dot(a, d)[0, 1] , np.dot(b, d)[0, 1], np.dot(d,c)[0, 1])
# # a_inv = np.linalg.inv(a)
# # print(a_inv.sum())
# # print((np.dot(a,a_inv)).sum())
# # A = np.array([[4, 2, -1], [1, 2, 1], [0, 1, -1]])
# # b = np.array([0, 1, -3])
# # print(sum(np.linalg.solve(A, b)))
#
# A = np.array([[3, -6], [1, -2]])
# b = np.array([5, -4])
# try:
#     print(np.linalg.solve(A, b))
# except np.linalg.LinAlgError as ex:
#     print(ex)
# import numpy as np
# import numpy.linalg as npl
# a=np.array([[-1,0,-1,-2,2],[2,-1,1,-2,2],[1,-2,0,-1,-1], [2,1,2,1,1]])
# print (npl.matrix_rank(a))
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if Vector.validate(x) and Vector.validate(y):
#             self.x = x
#             self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x,y):
#         return x*x+y*y
#
#
# v = Vector(2, 600)
# rez = Vector.norm2(5, 6)
# coord = v.get_coord()
# print(rez)
# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
#
# cat = Cat('Musiya')
# print(cat.str())

# 15. Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие | ООП Python

# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=

class Clock:
    __Day = 86400  # seconds in a day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds mac be a Number')
        self.seconds = seconds % self.__Day

    @classmethod
    def __verifay_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Write variable mast be int or Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verifay_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verifay_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verifay_data(other)
        return self.seconds <= sc


# c1 = Clock(1000)
# c2 = Clock(1200)
# print(c1 > [1, 2])

# 16. Магические методы __eq__ и __hash__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)


# print(p1 == p2)
# print(hash(p1))
# print(hash(p2))

# 12. Магический метод __call__. Функторы и классы-декораторы

class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('arg mast be a string')
        return args[0].strip(self.__chars)


s1 = StripChars("&:?!.; ")
rez = s1(' Hello World! ')


# print(rez)



# for g in geom:
#     print(g.get_pr())

# 18. Магические методы __getitem__, __setitem__ и __delitem__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Index error')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Index mast be INT >0')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Index mast be INT >0')

        del self.marks[key]


# s1 = Student('Ivan', [5, 5, 4, 2, 3])
# print(s1.marks)
# del s1[2]
# print(s1[3])
# print(s1.marks)

# 19. Магические методы __iter__ и __next__

class FRange:

    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2d:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2d(0, 2, 0.5, 4)
# print(next(fr))
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# for row in fr:
#     for x in row:
#         print(x, end=' ')
#     print()


##23. Наследование. Атрибуты private и protected

class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'Inicialization Geom for {self.__class__}')
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def get_cords(self):
        return (self.__x1, self.__y1)


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill='red'):
        super().__init__(x1, x2, y1, y2)
        self.__fill = fill



# r = Rect(0, 0, 10, 20)
# print(r.get_cords())
# print(r.__dict__)

# 24. Полиморфизм и абстрактные методы
# class Geom:
#     def get_pr(self):
#         raise NotImplementedError
#
#
# class Rectangle(Geom):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_pr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square(Geom):
#     def __init__(self, a):
#         self.a = a
#
#     def get_pr(self):
#         return 4 * self.a
#
#
# class Triangle(Geom):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c


# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(5, 6, 7)
# t2 = Triangle(1, 2, 3)
# geom = [r1, r2, s1, s2, t1, t2]

#25. Множественное наследование

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('init Goods')
        self.name = name
        self.weight =weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')

class MixinLog:
    ID = 0

    def __init__(self):
        print('init MixinLog')
        self .ID +=1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: was sall at 00:00 ')


class Notebook(Goods, MixinLog):
    pass

n = Notebook('Lg', 1.5, 30000)

n.print_info()
n.save_sell_log()
