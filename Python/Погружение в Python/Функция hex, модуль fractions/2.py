"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с
числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

def parse_fraction(fraction_str):
    # Разбиваем строку на числитель и знаменатель
    numerator, denominator = map(int, fraction_str.split('/'))
    return numerator, denominator


def add_fractions(frac1, frac2):
    num1, den1 = parse_fraction(frac1)
    num2, den2 = parse_fraction(frac2)

    # Находим общий знаменатель
    common_denominator = den1 * den2

    # Складываем числители с общим знаменателем
    sum_numerator = num1 * den2 + num2 * den1

    return f"{sum_numerator}/{common_denominator}"


def multiply_fractions(frac1, frac2):
    num1, den1 = parse_fraction(frac1)
    num2, den2 = parse_fraction(frac2)

    # Умножаем числители и знаменатели
    product_numerator = num1 * num2
    product_denominator = den1 * den2

    return f"{product_numerator}/{product_denominator}"


sum_result = add_fractions(frac1, frac2)

# Произведение дробей
product_result = multiply_fractions(frac1, frac2)

print(f'Сумма дробей: {sum_result}')
print(f'Произведение дробей: {product_result}')

a = Fraction(frac1)
b = Fraction(frac2)

print(f'Сумма дробей: {a + b}')
print(f'Произведение дробей: {a * b}')

# правильное решение

from fractions import Fraction
#frac1 = '2/5'
#frac2 = '3/5'

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")