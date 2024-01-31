"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("2.txt", encoding='utf-8') as text:
    lines = 1
    words = 0
    for line in text:
        lines += line.count("\n")
        print(f"Строка {line[:]} содержит {len(line.split())} словa")
print(f"Количество строк в файле {lines}")
