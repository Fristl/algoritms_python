from collections import deque
import sys

BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

DEC_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

list_mem = []


def show(x):
    print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}')
    list_mem.append(sys.getsizeof(x))

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
    return list_mem


def sum_hex(first, second):
    """
    Изменяемые объекты передаются по ссылке
    Используем копию, чтобы не ломать оригинал
    """
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    while len(first) != 0:
        first_num = DEC_NUMBERS[first.pop()]
        second_num = DEC_NUMBERS[second.pop()]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result, locals()


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    while len(second) != 0:
        second_num = DEC_NUMBERS[second.pop()]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)[0]

        spam.extend('0' * (len(first) - len(second) - 1))
        result = sum_hex(result, spam)[0]

    return result, locals()


a = deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())
b = deque(input('Введите второе число в hex формате (только цифры от 0 до f): ').upper())

answer_1, l_1 = sum_hex(a, b)[0], sum_hex(a, b)[1]
answer_2, l_2 = mult_hex(a, b)[0], mult_hex(a, b)[1]

print(f'{list(a)} + {list(b)} = {list(answer_1)}')
print(f'{list(a)} * {list(b)} = {list(answer_2)}')

show([BASE, HEX_NUMBERS, DEC_NUMBERS])
print('*' * 50, '\n')
print(l_1, '\n')
print('Суммарно занято памяти: ', sum((show(l_1)[1:])))
print('*' * 50, '\n')

list_mem = []
show([BASE, HEX_NUMBERS, DEC_NUMBERS])
print('*' * 50, '\n')
print(l_2, '\n')
print('Суммарно занято памяти: ', sum((show(l_2)[1:])))
