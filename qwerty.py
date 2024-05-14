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



set1 = {'Uzbekistan','USA','Russia','China','Argentina','Mexico','Germany','Italy'}
def add_country1():
    set2 = str(input('Введите страну которую хотите добавить: '))
    set1.add(set2)
    print(set1)


def add_country2():
    set3 = str(input('Введите страну которую хотите удалить: ' ))
    set1.remove(set3)
    print(set1)

def add_country3():
    set4 = str(input('Введите страну которую хотите найти: '))
    set1.intersection(set4)
    print('Да там есть эта страна')


a = int(input("Введите один вариант действия: 0 или 1 или 2: "))

if a == 0:
    add_country1()
elif a == 1:
    add_country2()
elif a == 2:
    add_country3()
