#По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
if b > 0:
    print('y = ', k,'x +',b)
else:
    print('y = ', k, 'x', b)