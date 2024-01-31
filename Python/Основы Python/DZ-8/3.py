"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_number = input("Введите число: ")

try:
    user_number = int(user_number)
    if user_number == 0:
        raise ZeroError("Вы ввели ноль. На ноль делить нельзя.")
except ValueError:
    print("Вы ввели не число.")
except ZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {user_number}")
