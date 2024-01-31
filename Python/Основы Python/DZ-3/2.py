"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(name, surname, year_of_birth, city, email, phone_number):
    print \
        (f"name: {name}, surname: {surname}, year_of_birth: {year_of_birth},"
         f"city: {city} , email: {email}, phone_number: {phone_number}")


user_info(name='Ivan', surname='Ivanov', year_of_birth=1990, city='Moscow',
          email='iv@mail.ru', phone_number=8990)
