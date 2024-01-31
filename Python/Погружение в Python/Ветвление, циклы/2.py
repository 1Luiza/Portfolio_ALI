"""
Проверка, является ли число простым или составным
"""

num = int(input("Введите число для проверки: "))

"""
def is_prime(num):
    if num <= 1 or num > 100000:
        return "Число должно быть больше 1 и меньше 100000"
    if num == 2:
        return f"{num} является простым числом"
    if num % 2 == 0:
        return f"{num} является составным числом"

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return f"{num} является составным числом"

    return f"{num} является простым числом"

result = is_prime(num)
print(result)
"""

if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "является простым числом")
    else:
        print(num, "является составным числом")
