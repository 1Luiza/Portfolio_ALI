"""
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import os
import logging
from collections import namedtuple
import sys

# Настройка логирования
logging.basicConfig(filename='file_info.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime}, {levelname}: {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Создание namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory',
                                   'parent_directory'])
# Получение пути к директории из аргументов командной строки
path = sys.argv[1]

try:
    # Проверка наличия директории
    if not os.path.exists(path):
        logger.error(f"Directory '{path}' does not exist.")

    # Проход по всем элементам в директории
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        is_directory = os.path.isdir(entry_path)

        # Получение информации о родительской директории
        parent_directory = os.path.basename(
            path) if is_directory else os.path.basename(
            os.path.dirname(path))

        # Получение имени файла без расширения
        name, extension = os.path.splitext(
            entry) if not is_directory else (entry, '')

        # Создание объекта FileInfo
        file_info = FileInfo(name=name, extension=extension,
                             is_directory=is_directory,
                             parent_directory=parent_directory)

        # Логирование информации
        logger.info(f"{file_info}")

except Exception as e:
    logger.error(f"Error: {str(e)}")
