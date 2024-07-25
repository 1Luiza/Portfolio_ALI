"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для
работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files
"""

# Функция rename_files, которую мы хотим записать в файл
rename_files_function = """
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []
    files = os.listdir('test_folder')
    filtered_files = [file for file in files if file.endswith(source_ext)]
    filtered_files.sort()
    num = 1
    for file in filtered_files:
        name = os.path.splitext(file)[0]
        if name_range:
            name = name[name_range[0]-1:name_range[1]]
        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
        path_old = os.path.join(os.getcwd(), 'test_folder', file)
        path_new = os.path.join(os.getcwd(), 'test_folder', new_name)
        os.rename(path_old, path_new)
        num += 1
"""

# Записываем функцию в файл
with open("__init__.py", "w") as file:
    file.write(rename_files_function)
