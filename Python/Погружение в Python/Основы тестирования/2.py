import unittest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
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
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


class TestCaseName(unittest.TestCase):
    """Тестирование класса Rectangle"""

    def test_width(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.width, 5)

    def test_height(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.height, 4)

    def test_perimeter(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.perimeter(), 20)

    def test_area(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_addition(self):
        r1 = Rectangle(5)
        r2 = Rectangle(3, 4)
        r3 = r1 + r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 6.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
