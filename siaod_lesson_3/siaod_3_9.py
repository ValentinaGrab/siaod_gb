#Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
SIZE_R = 5
SIZE_C = 4
array = [[random.randint(0,100) for _ in range(SIZE_C)] for j in range(SIZE_R)]
for i in range(len(array)):
    print(array[i])

min_array = []

for i in range(len(array[0])):
    min = array[i][0]
    for j in range(len(array)):
        if array[j][i] < min:
            min = array[j][i]
    min_array.append(min)

print("Минимальные элементы столбцов", min_array)
max = min_array[0]
for i in range(len(min_array)):
    if min_array[i] > max:
        max = min_array[i]

print("Максимальный элемент среди минимальных элементов столбцов:", max)




