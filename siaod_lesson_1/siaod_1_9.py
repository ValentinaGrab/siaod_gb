#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a, b, c = float(input("Первое число")), float(input("Второе число")), float(input("Третье число"))
if a < min(b,c) and b != c:
    print('Среднее число', min(b,c))
elif b < min(a,c) and a != c:
    print('Среднее число', min(a, c))
elif c < min(a,b) and a != b:
    print('Среднее число', min(a, b))
else:
    print("Числа больше одного и меньше другого нет")
