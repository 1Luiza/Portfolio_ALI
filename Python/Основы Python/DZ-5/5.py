"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
with open("5.txt", "w", encoding='utf-8') as sum_f:
    print("5 7 9 10 12 13", file=sum_f)
with open("5.txt", "r", encoding='utf-8') as sum_f:
    content = sum_f.read()
    sum_el = 0
    for el in content.split():
        sum_el += int(el)
print(sum_el)
