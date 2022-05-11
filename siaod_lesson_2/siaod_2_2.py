"""Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""


def count_numb(n, even=0, odd=0):
    if n == 0:
        return even, odd
    elif n % 2 == 0:
        even += 1
        n = n // 10
        return count_numb(n, even, odd)
    else:
        odd += 1
        n = n // 10
        return count_numb(n, even, odd)


n = int(input("Введите число: "))
print(n)
print("Количество четных и нечетных цифр в числе:", count_numb(n))