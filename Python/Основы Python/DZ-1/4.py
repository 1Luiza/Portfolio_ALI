"""
Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.
"""
n = int(input("Введите целое положительное число: "))
max_digit = 0
while n > 0:
    current_digit = n % 10
    if max_digit < current_digit:
        max_digit = current_digit
    else:
        n = n / 10
print(f"{max_digit}")
