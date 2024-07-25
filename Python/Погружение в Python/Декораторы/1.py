"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать
по три случайных числа в каждой строке, от 100-1000 строк, и записывать их в
CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно
сгенерировать.


Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного
уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию
find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из
аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью
функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON
содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле
results.json будет сохранена информация о параметрах и результатах вычислений
для каждой строки данных из CSV-файла.
"""
from random import randint
import csv
import json
import math


def save_to_json(func):
    def wrapper(*args):
        results = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row[0].split())
                roots = func(a, b, c)
                results.append({'parameters': [a, b, c], 'roots': roots})

            with open('results.json', 'w') as f:
                json.dump(results, f, indent=4)

    return wrapper


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = [' '.join(str(randint(1, 100)) for _ in range(3))]
            writer.writerow(row)


@save_to_json
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c

    if discr < 0:
        return None
    if discr == 0:
        x = -b / (2 * a)
        return x
    if discr > 0:
        sqrt_d = math.sqrt(discr)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return x1, x2


generate_csv_file("rows", 6)
find_roots("rows")
