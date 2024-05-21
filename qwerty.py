# a = 15
# if a > 10 and a < 20:
#     print("True")

# else:
#     print("False")

# a = ['a','b','c','d','e']
# if len(a) < 6 and len(a) > 0:
#     print("True")
# else:
#     print("False")

# def divide(x, y):
#     try:
#         result = x // y 
#         print("yes this is out answer",result)
#     except ZeroDivisionError:
#         print("Sorry you are diving by zero")
# divide(3,0)

# lst = ["'a'","'b'","'c'"]
# for i in lst:
#     print(i)

# lst = ['a','b','c']
# a = 0
# while a < len(lst): 
#     print(lst[a])
#     a += 1

# dct = {
#     'a':1,
#     'b':2,
# }
# lst1 = ['c','d']
# lst2 = [3,4]
# MyBox = {}
# for i in dct:
#     (lst1|lst2)
#     i.add(lst1|lst2)
#     print(i)

# def func():
#     num = 1
# func()
# print(num)#будет ошибка потому что принт находится за функцией а переменная внутри нее

# a = [1,2,3,4,5,6,12,24]
# a.remove(12)
# print(a)

# a = {1,2,3,'Apple','CS','Mango','Grapes'}
# a.add('hello')
# print(a)

# a = {'Joseph','Peter'}
# b = {96,65,2,1,59}
# print(a | b)3



# set1 = {'Uzbekistan','USA','Russia','China','Argentina','Mexico','Germany','Italy'}
# def add_country1():
#     set2 = str(input('Введите страну которую хотите добавить: '))
#     set1.add(set2)
#     print(set1)


# def add_country2():
#     set3 = str(input('Введите страну которую хотите удалить: ' ))
#     set1.remove(set3)
#     print(set1)

# def add_country3():
#     set4 = str(input('Введите страну которую хотите найти: '))
#     set1.intersection(set4)
#     print('Да там есть эта страна')


# a = int(input("Введите один вариант действия: 0 или 1 или 2: "))

# if a == 0:
#     add_country1()
# elif a == 1:
#     add_country2()
# elif a == 2:
#     add_country3()


# a = {'A','B','C','D','E','F','G'}
# b = {1,2,3,4,5,6,7,8,}
# def qwerty1():
#     print(a)
# def qwerty2():
#     print(b)

# c = int(input("Введите один вариант действия: 1 или 2: "))
# if c == 1:
#     qwerty1()
# elif c == 2:
#     qwerty2()

# class Myacademy:                
#     man = 10
#     a = input('pointer')
# p = Myacademy()
# print(p.a)
# print(p.man)


# class academy:
#     def __init__(self,type,age,lang):
#         self.type = type
#         self.age = age
#         self.lang = lang
#     def __str__(self):
#         return f"{self.type}({self.age})({self.lang})"

# p = academy('man',35,'uz')
# c = academy('women',25,'eng')
# print(p.type)
# print(p.lang)
# print(c.age)

# class ACADEMY:
#     name = ''
#     def fik(self):
#         print({self.name})


# p = ACADEMY('A','B','C','D','E','F','G')
# c = ACADEMY(1,2,3,4,5,6,7,8,)
# print(p.name)
# print(p.name)

# class Bexruz:

#     def bexruz(self)

#     name = "Bexruz"
#     country = "Tashkent"
#     data_of_birth = 14
    
#     def __init__(self,name,country,data_of_birth):
#         self.name = name
#         self.country = country
#         self.data_of_birth = data_of_birth

# b = Bexruz('Bexruz','Tashkent',14)
# print("His nsme is ", b.name," he was born in ", b.country,"He is",b.data_of_birth,"years old")

# import datetime 
# class Alisher:
#     def __init__(self,person,name,country,date_of_birth,age):
#         self.person = person
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
#         self.age = age
# a = Alisher(1,"Ferdi Odilia","France","1962-07-12",60)
# b = Alisher(2,"Shweta Maddox","Canada","1982-10-20",40)
# c = Alisher(3,"Elizaveta Tilman","USA","2000-01-01",23)
# print("Person: ",a.person,
#       "Name: ",a.name,
#       "Country: ",a.country,
#       "Date of Birth: ",a.date_of_birth,
#       "Age: ",a.age)
# print("Person: ",b.person,
#       "Name: ",b.name,
# #       "Country: ",b.country,
# #       "Date of Birth: ",b.date_of_birth,
# #       "Age: ",b.age)
# # print("Person: ",c.person,
# #       "Name: ",c.name,
# #       "Country: ",c.country,
# #       "Date of Birth: ",c.date_of_birth,
# #       "Age: ",c.age)

# class FamilyIbragim:
#     @staticmethod
#     def is_age():
#         age = 15
#         if age > 18:
#             print("True")
#         else:
#             print("False")

#     def spalniyIX(self,b):
#         self.b = b
#         print('this is simple method1', self.b)


# class FamilySalima(FamilyIbragim):
#     pass

# a = FamilySalima()
# a.spalniyIX(20)
# a.is_age(20)


# class Vehicle:
#     def __init__(self,name,milege,capacity):
#         a = name
#         b = milege
#         c = capacity
#     def fare(self):
#         return self.capacity * 100
    
# class Vehicle:
#     def __init__(self, name,mileage,capacity):
#         self.a = name
#         self.b = mileage
#         self.c = capacity
    
#     def fare(self):
#         return self.c * 100

# class Bus(Vehicle):
#     def fare(self):
#         return 5500

# # Пример использования:
# bus = Bus("School Bus", 50, 15)
# print(f"Общая стоимость проезда на автобусе : {bus.fare()}")  # Output должен быть 5500


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = str(input('Введите действие которое хотите совершить: '))
# if c == '+': 
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     print(a / b)
# elif c == '*':
#     print(a * b)

# alish = int(input('Введите превую цифру: '))
# alish1 = int(input('Введите вторую цифру: '))
# class  IBRAGIM:
#     def input():
#          a = '+'
#          b = '-'
#          c = '/'
#          d = '*'
# def plus():
#       print(a + b)
# def mines():
#      print(a - b)
# def myltiply():
#      print(a * b)
# def share():
#      print(a / b)
# slr = str(input('Введите действие которое хотите совершить +,-,* или /: *'))
# if slr == '+':
#      plus()
# elif slr == '-':
#      mines()
# elif slr == '*':
#      myltiply()
# elif slr == '/':
#      share()

class Calculator:
    def plus(self,a,b):
        return a + b
    def minus(self,a,b):
        return a - b
    def myltiply(self,a,b):
        return a * b
    def share(self,a,b):
        return a / b
    def cube(self,a,b):
        return a ** b
cal=Calculator()

class B(Calculator):
    pass

a = B()

def Input():
    a=int(input("Введите первую цифру: "))
    b=int(input("Введите вторую цифру: "))
    return a,b

znak=input("Выберите знак: + , - , * , / , **; ")

if znak in ["+","-","*","/","**",]:
    num1,num2=Input()

    if znak=="+":
        cal = input("Вы готовы заплатить 10$ ?: ")
    if cal == "да":
        print("result: ",a.plus(num1,num2))
    if znak == '-':
        cal = input("Вы готовы заплатить 10$ ?: ")
    if cal == "да":
        print("result: ",a.minus(num1,num2))
    if znak == '*':
        cal = input("Вы готовы заплатить 10$ ?: ")
    if cal == "да":
        print("result: ",a.myltiply(num1,num2))
    if  znak == '/':
        cal = input("Вы готовы заплатить 10$ ?: ")
    if cal == "да":
        print("result: ",a.share(num1,num2))
    if znak == '**':
        cal = input("Вы готовы заплатить 10$ ?: ")
    if cal == "да":
        print("result: ",a.cube(num1,num2))
    
      