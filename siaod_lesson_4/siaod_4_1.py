#В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit

def sum_array_without_min_max_v1(num_array):
    min_item, max_item, sum_array = 0, 0, 0
    for i, val in enumerate(num_array, start=0):
        if val > max_item:
            max_item = val
        if val < min_item:
            min_item = val
        sum_array = sum_array + num_array[i]
    return sum_array - max_item - min_item

def sum_array_without_min_max_v2(num_array):
    min_item, max_item, sum_array = 0, 0, 0
    for i in range(len(num_array)):
        if num_array[i] > max_item:
            max_item = num_array[i]
        if num_array[i] < min_item:
            min_item = num_array[i]
        sum_array = sum_array + num_array[i]
    return sum_array - max_item - min_item

def sum_array_without_min_max_v3(num_array):
    min_item, max_item, sum_array = 0, 0, 0
    i = 0
    while i != len(num_array):
        if num_array[i] > max_item:
            max_item = num_array[i]
        if num_array[i] < min_item:
            min_item = num_array[i]
        sum_array = sum_array + num_array[i]
        i += 1
    return sum_array - max_item - min_item

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f'  enumerate,  for,  while\n')
    for size in range(100, 10000, 100):
        num_array = [random.randint(-1000, 1000) for _ in range(size)]
        v1 = timeit.timeit('sum_array_without_min_max_v1(num_array)', number=1000, globals=globals())
        v2 = timeit.timeit('sum_array_without_min_max_v2(num_array)', number=1000, globals=globals())
        v3 = timeit.timeit('sum_array_without_min_max_v1(num_array)', number=1000, globals=globals())
        f.write(f'{size},{v1},{v2},{v3}\n')

print("finished")

