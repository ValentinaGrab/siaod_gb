"""Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу."""
SIZE_R = 5
SIZE_C = 4
a = []
for i in range(SIZE_C):
    sum = 0
    input_ = []
    for j in range(SIZE_R-1):
        input_.append((input()))
        sum = sum + int(input_[-1])
    print(sum)
    input_.append(sum)
    print(input_)
    a.append(input_)

for i in range(len(a)):
    print(a[i])



