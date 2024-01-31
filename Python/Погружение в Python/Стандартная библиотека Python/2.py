"""
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
"""

import logging
import sys

# Настройка логирования
logging.basicConfig(filename='rectangle.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime}, {levelname}: {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# 1
class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(
                f'NegativeValueError: Ширина должна быть положительной, а не {width}')
            raise NegativeValueError(
                f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(
                    f'NegativeValueError: Высота должна быть положительной, а не {height}')
                raise NegativeValueError(
                    f'Высота должна быть положительной, а не {height}')
            self._height = height
        logger.info(
            f'Создан прямоугольник: ширина {self._width}, высота {self._height}')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            logger.error(
                f'NegativeValueError: Ширина должна быть положительной, а не {value}')
            raise NegativeValueError(
                f'Ширина должна быть положительной, а не {value}')
        logger.info(f'Установлена ширина прямоугольника: {self._width}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            logger.error(
                f'NegativeValueError: Высота должна быть положительной, а не {value}')
            raise NegativeValueError(
                f'Высота должна быть положительной, а не {value}')
        logger.info(f'Установлена высота прямоугольника: {self._height}')

    def perimeter(self):
        p = 2 * (self._width + self._height)
        logger.info(f'Периметр прямоугольника: {p}')
        return p

    def area(self):
        a = self._width * self._height
        logger.info(f'Площадь прямоугольника: {a}')
        return a

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


if __name__ == "__main__":
    # Получение ширины и высоты из аргументов командной строки
    if len(sys.argv) != 3:
        print("Usage: python script.py <width> <height>")
        sys.exit(1)

    width = float(sys.argv[1])
    height = float(sys.argv[2])
    r = Rectangle(width, height)


# 2
class InvalidTextError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid text: {self.text}. Text should be a non-empty string.'


class InvalidNumberError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number: {self.number}. Number should be a positive ' \
               f'integer or float.'


class Archive:
    """Документация для класса Архив"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        if not isinstance(text, str) or len(text.strip()) == 0:
            logger.error(
                f"InvalidTextError: Invalid text: {self.text}. Text should be "
                f"a non-empty string.")
            raise InvalidTextError(text)
        if not (isinstance(number, int) or isinstance(number,
                                                      float)) or number <= 0:
            logger.error(f"InvalidNumberError: Invalid number: {self.number}. "
                         f"Number should be a positive integer or float.")
            raise InvalidNumberError(number)
        self.text = text
        self.number = number
        logger.info(f'Создан текст: {self.text},  число: {self.number}')

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. ' \
               f'Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'
