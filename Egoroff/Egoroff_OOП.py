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


class Point:
    def set_coordinates(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_distance(self, point2):
        print(((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5) if isinstance(point2, Point) else print("Передана не точка")
        #print( [ "Передана не точка", (((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5) ][isinstance(point2, Point)] )

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)  # вернёт 5.0
p1.get_distance('10')


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
class Stack():
    def __init__(self):
        self.values = []

    def push(self, item):
        #self.items = item
        self.values.append(item)

    def pop(self):
        return self.values.pop(-1) if len(self.values) != 0 else print("Empty Stack")

    def peek(self):
        return self.values[-1] if len(self.values) != 0 else print("Empty Stack")

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2
# class UserMail:
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, mail):
#         # Метод должен проверять,
#         # что в новой почте есть только один символ @ и после нее есть точка.
#         # Если данные условия выполняются, новая почта сохраняется в атрибут __email,
#         # в противном случае выведите сообщение "Ошибочная почта";
#         lin = ''.join(a for a in filter(lambda l: '@' in l and l.count('@') == 1, [mail]) if '.' in a.split('@')[1])
#         self.__email = lin if len(lin) != 0 else print("Ошибочная почта")
#
#     email = property(fget=get_email, fset=set_email)
#
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3]  # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.q)  # prince@still.wait
#print(UserMail.__dict__)

