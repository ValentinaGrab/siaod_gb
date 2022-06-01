""" Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque
d_to = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
d_out = list(d_to)

def create_len(a, b):  ## Дополнение нулями до одинаковой длины
    n = len(a) - len(b)
    if n > 0:
        b.extendleft(['0']*n)
    else:
        n = n * -1
        a.extendleft(['0']*n)
    return a, b

def sum_AB(a, b):  ## Суммирование двух коллекций
    create_len(a, b)
    c = deque()
    div_s = 0
    for i in range(-1, -(len(a))-1, -1):
        s = d_to[a[i]] + d_to[b[i]] + div_s
        c.appendleft(d_out[s % 16])
        div_s = s//16
    if div_s > 0:
        c.appendleft(str(div_s))
    return c

def mult_AB(a, b, l_a, l_b):  ## Произведение двух коллекций
    res_mult = deque()

    for i in range(-1,-l_b - 1,-1):
        c = deque()
        div_s = 0
        for j in range(-1, -l_a - 1, -1):
            s = d_to[a[j]] * d_to[b[i]] + div_s
            c.appendleft(d_out[s % 16])
            div_s = s // 16
        if div_s > 0:
            c.appendleft(str(div_s))
        c.extend(['0']*(-1*i-1))
        x = sum_AB(res_mult, c)
        res_mult = x
    return res_mult

a = deque(input('Введите A:  '))
b = deque(input('Введите B:  '))
operand = input('Для выбора операции введите + или *:  ')
if operand == '+':
    print('Сумма A и B:  ', list(sum_AB(a, b)))
else:
    print('Произведение А и В:  ', list(mult_AB(a, b, len(a), len(b))))


