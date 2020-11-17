"""Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего."""

import collections


n = int(input('Введите количество предприятий: '))
info_about_company = collections.defaultdict(list)

for i in range(n):
    i = input(f"Введите название {i + 1}-ой фирмы: ")
    for item in range(4):
        item = int(input(f"Введите её прибыль в {item + 1}-ом квартале: "))
        info_about_company[i].append(item)


general_avg_profit = 0

for profit in info_about_company.values():
    general_avg_profit += sum(profit)
else:
    general_avg_profit /= n
    print(f"Средняя прибыль (за год для всех предприятий): {general_avg_profit}")


profit_for_the_year = {}

for company, _profit in info_about_company.items():
    profit_for_the_year[company] = sum(_profit)


status_avg_profit = collections.defaultdict(list)  # создал только для красивого вывода

for name_company, profit_company in profit_for_the_year.items():
    if profit_company > general_avg_profit:
        status_avg_profit['above_avg'].append(name_company)
    elif profit_company < general_avg_profit:
        status_avg_profit['below_avg'].append(name_company)

print('Компании чья прибыль выше средней: ')
for _company in status_avg_profit['above_avg']:
    print(_company)
print('Компании чья прибыль ниже средней: ')
for _company_ in status_avg_profit['below_avg']:
    print(_company_)
