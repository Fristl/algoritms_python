"""Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""


def fceod(number, count_e, count_o):
    if number == 0:
        return count_e, count_o
    digit_ = number % 10
    if digit_ % 2 == 0:
        count_e += 1
    else:
        count_o += 1
    return fceod(number // 10, count_e, count_o)


count_even = 0
count_odd = 0

num = int(input("Введите натуральное число: "))

res_even, res_odd = fceod(num, count_even, count_odd)

print(f'Количество чётных цифр: {res_even},\n'
      f'Количество нечётных цифр: {res_odd}')

"""Если нельзя использовать кортэж, тогда 
return f'{count_e} {count_o}'
а вместо res_even и res_odd будет одна переменная res,
которая и пойдёт в принт"""
