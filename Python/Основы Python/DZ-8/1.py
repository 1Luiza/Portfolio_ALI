"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков)
для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, param):
        self.param = param

    def __str__(self):
        result = '\n'.join(map(str, self.param))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        res = self.param
        for i in range(len(self.param)):
            for k in range(len(self.param[i])):
                res[i][k] = self.param[i][k] + other.param[i][k]
        return Matrix(res)


matr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matr_1)
print()
print(matr_2)
print()
print(matr_1 + matr_2)
