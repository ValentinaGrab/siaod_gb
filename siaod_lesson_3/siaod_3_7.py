"""В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
import random

SIZE = 15
MIN_NUM = -10
MAX_NUM = 10
num_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(num_array)

# решение
min_list = [num_array[0],num_array[0]]
for i, val in enumerate(num_array, start=0):
    if val < min_list[0]:
        min_list[1] = min_list[0]
        min_list[0] = val
    elif val < min_list[1]:
        min_list[1] = val
print("Два наименьших элемента", *min_list)
