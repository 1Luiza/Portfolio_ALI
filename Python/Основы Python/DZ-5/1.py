"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

user_info = open("1.txt", "w", encoding='utf-8')
while True:
    text = input("Введите данные: ")
    if text == '':
        break
    user_info.write(text + '\n')
user_info.close()
