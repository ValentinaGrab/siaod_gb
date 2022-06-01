"""Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import Counter
base_companies = Counter()
n = int(input('Count companies: '))

for i in range(n):
    company = input('Name company: ')
    for y in range(4):
        sum_company = int(input('inc from ' + str(y+1) + ' quart: '))
        base_companies[company] += sum_company
avrg_s = sum(base_companies.values())/n

print(base_companies)

case_1 = ', '.join(list(filter(lambda key: base_companies[key] > avrg_s, base_companies.keys())))
case_2 = ', '.join(list(filter(lambda key: base_companies[key] < avrg_s, base_companies.keys())))

print('Best companies: ', case_1)
print('Unprof companies: ', case_2)