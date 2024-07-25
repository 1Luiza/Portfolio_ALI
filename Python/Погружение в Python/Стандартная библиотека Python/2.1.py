import logging
import sys

# Настройка логирования
logging.basicConfig(filename='archive.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime}, {levelname}: {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


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
        logger.info(f'Создан текст: {self.text} и число: {self.number}')

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. ' \
               f'Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == "__main__":
    # Получение аргументов из командной строки
    if len(sys.argv) != 3:
        print("Usage: python script.py <text> <number>")
        sys.exit(1)

    text = sys.argv[1]
    number = float(sys.argv[2])
    a = Archive(text, number)
