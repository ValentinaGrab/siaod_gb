#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

x1, x2 = input(), input()

pos1 = ord(x1) - ord('a')
pos2 = ord(x2) - ord('a')

dest = abs(pos1 - pos2)

print(pos1, pos2, dest)
