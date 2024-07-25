# 1
def my_func(arg_1, arg_2):
    while abs(arg_2) > 0:
        res = arg_1 * arg_1
        return 1 / res
    # return arg_1 ** arg_2


# 2
"""
month = int(input("Введите номер месяца: "))
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Введите число от 1 до 12")
"""


# 3
class Stationery:

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Отрисовка {self.title}")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Отрисовка {self.title}")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Отрисовка {self.title}")


PS = Pen("ручкой")
PCS = Pencil("карандашом")
HS = Handle("маркером")


# 4
class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(arg_1, arg_2):
    if arg_2 == 0:
        raise ZeroError("Вы ввели ноль. На ноль делить нельзя.")
    try:
        return arg_1 / arg_2
    except ZeroError:
        return "введите число больше 0"


# 5
a = 3
b = 6
day = 1
# print(f"{day} день: {a}")
while a < b:
    result = a * 0.1 + a
    a = result
    day += 1
    # print(f"{day} день: {round(result, 2)}")
# print(f"На {day} день спортсмен достиг результата - не менее {b} км")
