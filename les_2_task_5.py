"""Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

code_st = 32
code_end = 127
spam = 0

for idx in range(code_st, code_end + 1):
    if spam == 10:
        spam = 0
        print()
    symbol = chr(idx)
    print(f'{idx:>3} : {symbol}', end='\t\t')
    spam += 1
