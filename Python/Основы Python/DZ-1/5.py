"""
Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.
"""
revenue = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек фирмы: "))
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print("Прибыль - выручка больше издержек")
    print(f"Рентабельность выручки {round(profitability, 3)}")
    staff = int(input("Введите численность сотрудников фирмы: "))
    staff_profit = profit / staff
    print(f"Прибыль фирмы на одного сотрудника - {round(staff_profit, 3)}")
else:
    print("Убыток - издержки больше выручки")
