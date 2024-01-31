"""
Напишите функцию группового переименования файлов в папке test_folder под
названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце
имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно
работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=
None):
    new_names = []

    # Получаем список файлов в текущей директории
    files = os.listdir('test_folder')

    # Фильтруем только нужные файлы с указанным расширением
    filtered_files = [file for file in files if file.endswith(source_ext)]

    # Сортируем файлы по имени
    filtered_files.sort()

    # Задаем начальный номер для порядкового номера
    num = 1

    # Переименовываем файлы
    for file in filtered_files:
        # Получаем имя файла без расширения
        name = os.path.splitext(file)[0]

        # Если задан диапазон, обрезаем имя файла
        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        # Переименовываем файл
        path_old = os.path.join(os.getcwd(), folder_name, file)
        path_new = os.path.join(os.getcwd(), folder_name, new_name)
        os.rename(path_old, path_new)

        # Увеличиваем порядковый номер
        num += 1
"""
import os
import shutil


def rename_files(desired_name, num_digits, source_ext, target_ext,
                 name_range=None):
    # Получить текущую рабочую директорию
    folder_path = os.path.join(os.getcwd(), "test_folder")

    # Получить список всех файлов в директории
    files = os.listdir(folder_path)

    # Инициализировать счетчик файлов
    count = 1

    # Перебрать все файлы в директории
    for file_name in sorted(files):
        # Если расширение файла соответствует source_ext
        if file_name.endswith(f".{source_ext}"):
            # Создать новое имя файла
            new_file_name = f"{desired_name}{str(count).zfill(num_digits)}.{target_ext}"

            # Переименовать файл
            os.rename(os.path.join(folder_path, file_name),
                      os.path.join(folder_path, new_file_name))

            # Увеличить счетчик
            count += 1


# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
file_name = "test1.txt"
file_path = os.path.join(folder_path, file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()

rename_files(desired_name="file_", num_digits=4, source_ext="txt",
             target_ext="txt")

folder_content = ""
files = os.listdir(folder_path)
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)
