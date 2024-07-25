"""
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение
NegativeValueError.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с
шириной 5 и r4 с отрицательной шириной (-2). Убедимся, что r1.width корректно
установлен на 5, а создание r4 вызывает исключение NegativeValueError с текстом
Ширина должна быть положительной, а не {value}

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники
r2 с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4.
При необходимости выбрасывать исклчение NegativeValueError с текстом Высота
должна быть положительной, а не {value}

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с
шириной 5 и проверяем, что r1.perimeter() возвращает 20. Также создан
прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter()
возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5
и проверяем, что r1.area() возвращает 25. Также создан прямоугольник r2 с
шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с
шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и
проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и
высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с
шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и
проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и
высоты (2 и 2.0 соответственно).
"""
import doctest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        """
        test_width
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r4 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2

        test_height
        >>> r2 = Rectangle(3,4)
        >>> r2.width
        3
        >>> r2.height
        4
        """
        if width <= 0:
            raise NegativeValueError(
                f'Ширина должна быть положительной, а не {width}')
        self.width = width
        if height is None:
            self.height = width
        else:
            if height <= 0:
                raise NegativeValueError(
                    f'Высота должна быть положительной, а не {height}')
            self.height = height

    def perimeter(self):
        """
        test_perimeter
         >>> r1 = Rectangle(5)
         >>> r1.perimeter()
         20
         >>> r2 = Rectangle(3,4)
         >>> r2.area()
         12
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        test_area
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3,4)
        >>> r2.perimeter()
        14
        """
        return self.width * self.height

    def __add__(self, other):
        """
        test_addition
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3,4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        test_subtraction
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3,4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
