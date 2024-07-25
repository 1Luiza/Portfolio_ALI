"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали
и чего удалось добиться
"""
from numpy import array
from pympler import asizeof
from json import dumps

lst = [45, 65, 0, 12, 3, 7, 2, 88]
new_list = [lst[i] for i in range(len(lst)) if lst[i - 1] < lst[i]]
print(lst)
print(new_list)
print(asizeof.asizeof(lst))

lst = array([45, 65, 0, 12, 3, 7, 2, 88])
new_list = [lst[i] for i in range(len(lst)) if lst[i - 1] < lst[i]]
print(array(lst))
print(new_list)
print(asizeof.asizeof(lst))

"""Лист lst преобразован в массив типа numpy.ndarray. Размер lst = 358, размер 
lst преобразованного = 160"""

month = int(input("Введите номер месяца: "))
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Введите число от 1 до 12")

dumped_seasons_dict = dumps(seasons_dict)
print(asizeof.asizeof(seasons_dict))
print(asizeof.asizeof(dumped_seasons_dict))

"""После использования программой словаря, он преобразован в json строку. 
Преобразованный словарь в данной программе не может быть использован, поэтому 
преобразование в конце для примера оптимизации памяти. 
Размер словаря = 584, размер преобразованного в json словаря = 112"""
