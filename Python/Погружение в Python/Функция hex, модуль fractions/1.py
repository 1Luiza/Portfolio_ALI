"""
Напишите программу, которая получает целое число num и возвращает
его шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.
"""
num = int(input("введите число: "))
hex_chars = "0123456789ABCDEF"
a = num
base = 16
res = ''
while num > 0:
    remainder = num % base
    res = hex_chars[remainder] + res
    num //= base
print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {hex(a)}')


#правильное решение
HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)