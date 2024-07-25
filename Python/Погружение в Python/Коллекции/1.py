'''
На вход подается словарь со списком вещей для похода в качестве ключа и их
массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack, передав его максимальную
грузоподъёмность.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и
сохранен в переменную backpack.
'''

items = {
    "спальник": 1.0,
    "палатка": 2.0,
    "термос": 0.5,
    "карта": 0.1,
    "фонарик": 0.2,
    "котелок": 0.5,
    "еда": 2.0,
    "одежда": 1.0,
    "обувь": 0.8,
    "нож": 0.2
}
max_weight = 10.0

backpack = {}

"""
current_weight = 0

for item, weight in items.items():
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight
"""

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

print(backpack)
