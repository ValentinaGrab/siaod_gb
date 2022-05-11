"""Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""

def convert(num):
    if len(num) == 0:
        return ""
    else:
        return num[-1] + convert(num[:-1])

a = input()
print(convert(a))