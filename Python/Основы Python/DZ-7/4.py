"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехал")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} - {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


TC = TownCar(50, 'black', 'Volkswagen', False)
SC = SportCar(60, 'red', 'Honda', False)
WC = WorkCar(35, 'blue', 'UAZ', False)
PC = PoliceCar(60, 'white', 'Ford', True)

print(f"{TC.name} цвета {TC.color}. Полицейская машина? {TC.is_police}")
print(f"{SC.name} цвета {SC.color}. Полицейская машина? {SC.is_police}")
print(f"{WC.name} цвета {WC.color}. Полицейская машина? {WC.is_police}")
print(f"{PC.name} цвета {PC.color}. Полицейская машина? {PC.is_police}")

TC.go()
SC.stop()
WC.turn("направо")
PC.show_speed()
