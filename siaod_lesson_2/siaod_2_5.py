"""Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

def chars(arg=32,n=0):
    if arg == 127:
        return f"127 -{chr(arg)}"
    else:
        if n < 10:
            return f"{str(arg)} - {str(chr(arg))} {str(chars(arg+1, n+1))}"
        elif n == 10:
            return str(arg) + "-" + "\n" + str(chr(arg)) + str(chars(arg + 1, 0))

print(chars())