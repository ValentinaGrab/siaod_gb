"""В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

MIN_NUM = 2
MAX_NUM = 99
MIN_DIV = 2
MAX_DIV = 9

# Решение
dict = {}
for i in range(MIN_DIV,MAX_DIV+1):
    dict[i] = 0
    for j in range(MIN_NUM, MAX_NUM+1):
        if j % i == 0:
            dict[i] += 1
print("{:<5} {:<5}".format("Div","Count"))
for key in dict.items():
    name, val  = key
    print("{:<5} {:<5}".format(name,val))

