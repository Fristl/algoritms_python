"""Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],

произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def test1(n1, n2):
    """Функция для проверки правильности операции сложения"""
    return hex(int(n1, 16) + int(n2, 16))


def test2(n1, n2):
    """Функция для проверки правильности операции умножения"""
    return hex(int(n1, 16) * int(n2, 16))


def insignificant_zeros(num1, num2=deque('0')):
    """Функция добавляет незначимые 0 в начало чисел,
    чтобы длины обоих чисел в виде списков были одинаковыми"""
    if len(num1) > len(num2):
        while len(num2) != len(num1):
            num2.appendleft('0')
    elif len(num2) > len(num1):
        while len(num1) != len(num2):
            num1.appendleft('0')
    return num1, num2


def sum_16(num_1, num_2='0'):
    """Функция предназначена для сложения двух
    шестнадцатеричных чисел, где
    num_1 - первое число;
    num_2 - второе число"""
    res_sum = deque()
    in_mind = 0

    for idx in range(-1, -len(num_1) - 1, -1):
        spam = hex_.index(num_1[idx]) + hex_.index(num_2[idx]) + in_mind
        if spam // 16 >= 1:
            in_mind = 1
            d = spam % 16
        else:
            in_mind = 0
            d = spam
        res_sum.appendleft(hex_[d])
    else:
        if in_mind == 1:
            res_sum.appendleft(hex_[in_mind])
    return res_sum


def mult_nums(num_1, num_2):
    """Функция вычисляет максимальную и минимальную длину,
    и переназначает местами введённые числа, если это требуется,
    для удобства при дальнейших операциях.
    После поочерёдно (в столбик) происходит умножение.
    В конце полученные значения складываются с помощью функции сложения
    двух шестнадцатеричных чисел."""

    cpz = 0
    res_mul = deque()

    if len(num_1) < len(num_2):
        min_len = len(num_1)
        max_len = len(num_2)
        num_1, num_2 = num_2, num_1
    else:
        min_len = len(number_2)
        max_len = len(number_1)

    for idx in range(-1, -min_len - 1, -1):
        in_mind = 0
        mult_num = deque()
        for index_ in range(-1, -max_len - 1, -1):
            spam = hex_.index(num_1[index_]) * hex_.index(num_2[idx]) + in_mind
            if spam // 16 >= 1:
                in_mind = spam // 16
                d = spam % 16
            else:
                in_mind = 0
                d = spam
            mult_num.appendleft(hex_[d])
        else:
            if in_mind:
                if in_mind // 16 == 0:
                    mult_num.appendleft(hex_[in_mind])
                else:
                    e = in_mind % 16
                    mult_num.appendleft(hex_[e])
                    in_mind //= 16
                    mult_num.appendleft(hex_[in_mind])
        n = cpz
        while n:
            mult_num.append('0')
            n -= 1
        cpz += 1
        res_mul = sum_16(*insignificant_zeros(mult_num, res_mul))

    return res_mul


hex_ = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
a = (input("Введите первое шестнадцатеричное число: ")).upper()
b = (input("Введите второе шестнадцатеричное число: ")).upper()
number_1 = deque(a)
number_2 = deque(b)
print(number_1)
print(number_2)

answer1 = sum_16(*insignificant_zeros(number_1, number_2))
print(f'Сумма чисел равна: {answer1}')
print(test1(a, b), '- ответ для проверки')

number_1 = deque(a)
number_2 = deque(b)
answer2 = mult_nums(number_1, number_2)
print(f'Произведение чисел равна: {answer2}')
print(test2(a, b), '- ответ для проверки')
