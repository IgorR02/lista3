import math
import random
#Zad1
# a = [x - 1 for x in range(1, 10)]
# print(a)
# b = [4 ** x for x in range(0, 7)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

#Zad2
# list1 = [random.randint(0, 10) for x in range(10)]
# print(list1)
# list2 = [x for x in list1 if x % 2 == 0]
# print(list2)

#Zad3
# dictionary = {"Milk": "l", "Apple": "piece", "Nuts": "kg", "Banana": "piece"}
# list = [key : value for key, value in dictionary.items() if value == "piece"]
# print(list)

#Zad4
# a = int(input("Podaj bok trojkata a:"))
# b = int(input("Podaj bok trojkata b:"))
# c = int(input("Podaj bok trojkata c:"))
# def SquareTriangle(a, b, c):
#     if a ** 2 + b ** 2 == c ** 2:
#         print("Trojkat jest prostokatny")
#     else:
#         print("Trojkat nie jest prostokatny")
# print(SquareTriangle(a, b, c))

#Zad5

#Alternatywnie:
# a = float(input("Podaj dlugosc pierwszej podstawy:"))
# b = float(input("Podaj dlugosc drugiej podstawy:"))
# h = float(input("Podaj wysokosc:"))
# a = 2
# b = 3
# h = 4
# def Trapeze(a, b, h ):
#     field = ((a + b) * h) / 2
#     print(field)
# print(Trapeze(a, b, h))

#Zad6
# a = 1
# b = 4
# ile = 10
# def StringProduct(a , b, ile):
#     product = 0
#     for x in range(ile):
#         product = product + (a * b)
#         print(product)
# print(StringProduct(a, b, ile))

#Zad7
# def StringProduct2(*el):
#     product = 1
#     for x in el:
#         product *= x
#         print(product)
# print(StringProduct2(1, 2, 3, 4))

#Zad8
# def ShoppingList(**shli):
#     Slist = {"Milk": 3.99, "Apple": 1.99, "Nuts": 49.99, "Banana": 2}
#     length = len(Slist)
#     value = sum(Slist.values())
#     return length, value
# print(ShoppingList())

#Zad9


