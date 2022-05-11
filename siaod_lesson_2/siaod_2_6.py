"""В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ."""

import random

def guess_func(secret_num, count = 0,user_num=-1):
    if count == 11:
        return f"Попыток больше нет, загадано {secret_num}"
    else:
        if user_num == -1:
            user_num = int(input("Угадайте число: "))
            return guess_func(secret_num, count + 1, user_num)
        elif user_num > secret_num:
            print("Загаданное число меньше, попробуйте еще раз")
            user_num = int(input())
            return guess_func(secret_num, count+1, user_num)
        elif user_num < secret_num:
            print("Загаданное число больше, попробуйте еще раз")
            user_num = int(input())
            return guess_func(secret_num, count+1, user_num)
        elif user_num == secret_num:
            return f"Отгадали!"

secret_num = random.randint(1, 100)
#print(secret_num)
print(guess_func(secret_num))