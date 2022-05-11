"""Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

def chars(args,n):
    if args == 127:
        return f"127 -{chr(args)}"
    else:
        if n < 10:
            return str(args)+"-" + str(chr(args)) +str(chars(args+1,n+1))
        elif n == 10:
            return str(args) + "-" + "\n" + str(chr(args)) + str(chars(args + 1, 0))

print(chars(32,0))