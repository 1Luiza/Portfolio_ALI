"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали
и чего удалось добиться
"""

from timeit import timeit


# 1 вариант
def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    max_1 = max(arg_list)
    arg_list.remove(max_1)
    max_2 = max(arg_list)
    max_list = [max_1, max_2]
    return sum(max_list)


a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
print(my_func(a, b, c))
print(timeit("my_func(a, b, c)", globals=globals(), number=1000))


# 2 вариант
def get_max(*args):
    return (sum(sorted(list(args), reverse=True)[:2]))


print(get_max(3, 5, 6))
print(timeit("get_max(3, 5, 6)", globals=globals(), number=1000))

"""добавлено решение с помощью встроенной функции sorted, что сокращает 
время работы программы и визуально разгружает программу. При аргументах 3, 5, 6
время, затрачиваемое на выполнение 1 варианта: 0.0007614000351168215, 
на выполнение 2 варианта: 0.0006644999957643449."""


# 1 вариант
def my_func(arg_1, arg_2):
    while abs(arg_2) > 0:
        res = arg_1 * arg_1
        return 1 / res


x = int(input("Введите x: "))
y = int(input("Введите y: "))
print(my_func(x, y))
print(timeit("my_func(x,y)", globals=globals(), number=1000))

# 2 вариант
x = int(input("Введите x: "))
y = int(input("Введите y: "))
print(x ** y)
print(timeit("x ** y", globals=globals(), number=1000))

"""добавлено решение через встроенную функцию **, что в некоторых случаях
сокращает время работы программы и визуально разгружает программу. При х = 2, 
 у = -2 время, затрачиваемое на выполнение 1 варианта: 0.00020929996389895678, 
 на выполнение 2 варианта: 0.00018550001550465822."""
