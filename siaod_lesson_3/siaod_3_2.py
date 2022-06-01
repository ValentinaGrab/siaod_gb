"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random
SIZE = 8
MIN_NUM = 0
MAX_NUM = 100
res_array = []

num_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print("Дан массив: ",num_array)

for i in range(len(num_array)):
    if num_array[i] % 2 == 0:
        res_array.append(i)
print("Четные элементы", res_array)

