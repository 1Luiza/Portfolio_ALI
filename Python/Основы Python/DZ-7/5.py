"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""


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

PS.draw()
PCS.draw()
HS.draw()
