#Определить, какое число в массиве встречается чаще всего.
import random
SIZE = 15
MIN_NUM = 0
MAX_NUM = 10
num_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]


print("Дан массив: ", num_array)
dict = {}
print(dict)

for i in range(len(num_array)):
    if num_array[i] in dict.keys():
        dict[num_array[i]] += 1
    else:
        dict[num_array[i]] = 1
print(dict)
max = 0
max_key = 0
for key in dict:
    if dict[key] > max:
        max = dict[key]
        max_key = key
print("Чаще всего в массиве встречается:", max_key)