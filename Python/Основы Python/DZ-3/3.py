"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    max_1 = max(arg_list)
    arg_list.remove(max_1)
    max_2 = max(arg_list)
    max_list = [max_1, max_2]
    print(sum(max_list))


a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
my_func(a, b, c)
