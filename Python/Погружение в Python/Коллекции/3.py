"""
На вход подается словарь со списком вещей для похода в качестве ключа и их
массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную
грузоподъёмность.

В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.

В переменную result выведите список, содержащий все возможные варианты
backpack. Напечатайте переменную result.

*Верните все возможные варианты комплектации рюкзака.
"""
from pprint import pprint

def fill_backpack(items, max_weight):
    result = []
    items_list = list(items.keys())

    for i in range(1, 2 ** len(items_list)):
        subset = [items_list[j] for j in range(len(items_list)) if
                  (i & (1 << j)) > 0]
        subset_weight = sum(items[item] for item in subset)

        if subset_weight <= max_weight:
            backpack = {item: items[item] for item in subset}
            result.append(backpack)

    return result


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = fill_backpack(items, max_weight)

for backpack in result:
    print(backpack)

# 2

backpacks = []
sorted_result = []
for i in range(2 ** len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)
pprint(result)
