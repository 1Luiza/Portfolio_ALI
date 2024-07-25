"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для
работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
"""
functions = """
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
"""

with open("__init__.py", "w") as file:
    file.write(functions)
