from sys import argv

name_script, time, rate, bonus = argv

time = float(time)
rate = float(rate)
bonus = float(bonus)
salary = time * rate + bonus
print(f"заработная плата сотрудника: {salary}")
