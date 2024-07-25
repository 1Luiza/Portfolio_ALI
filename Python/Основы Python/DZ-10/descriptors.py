"""
Создать не менее двух дескрипторов для атрибутов классов, которые
вы создали ранее в ДЗ
"""


class Attributes:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 15:
            raise ValueError("Не может быть меньше 15")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = Attributes()
    width = Attributes()
    mass_of_meter = 25
    thikness = 5

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        result = (self.length * self.width * Road.mass_of_meter *
                  Road.thikness) / 1000
        print(result)


r_1 = Road(20, 5000)
r_1.mass()


class NonInt:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if type(value) is int or float:
            raise ValueError("Не может быть числом")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = NonInt()
    surname = NonInt()
    position = NonInt()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self.income['wage'] + self.income['bonus'])


pos_1 = Position('Ivan', 'Ivanov', 'driver', 10, 10000)
pos_1.get_full_name()
pos_1.get_total_income()
