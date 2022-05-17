#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
SIZE = 8
MIN_NUM = 0
MAX_NUM = 100


num_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print("Дан массив: ", num_array)
min, max = 0, 0
for i in range(len(num_array)):
    if num_array[i] < num_array[min]:
        min = i
    if num_array[i] > num_array[max]:
        max = i
print(min, max)
num_array[min] , num_array[max] = num_array[max], num_array[min]
print(num_array)
