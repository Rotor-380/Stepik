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

