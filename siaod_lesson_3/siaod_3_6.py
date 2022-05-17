#В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 15
MIN_NUM = -10
MAX_NUM = 10
num_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(num_array)

# решение
min_item, max_item, sum_array = 0, 0, 0
for i, val in enumerate(num_array, start=0):
    if val > max_item:
        max_item = val
    if val < min_item:
        min_item = val
    sum_array = sum_array + num_array[i]

print(sum_array, max_item, min_item)
sum_array = sum_array - max_item - min_item
print("Сумма элементов массива без максимального и минимального:", sum_array)
