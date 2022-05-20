"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""
import random

SIZE = 15
MIN_NUM = -10
MAX_NUM = 10
num_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
k = MIN_NUM # вроде так нельзя

print(num_array)
for i, val in enumerate(num_array, start = 0):
    if (val > k) and (val < 0):
        k, min_index = val, i
print(f"Максимальное минимальное число: {k}/ индекс  массиве : {min_index}")


