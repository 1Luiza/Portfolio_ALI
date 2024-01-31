"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
"""
with open("4.txt", encoding='utf-8') as text:
    for line in text:
        line = text.readline()
        with open("4.1.txt", "w", encoding='utf-8') as text_out:
            print(f"{line}", file=text_out)
"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('4.1.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
