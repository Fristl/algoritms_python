"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

M = 3
SIZE = 2 * M + 1

ARRAY = [random.randint(1, 10) for _ in range(SIZE)]
print(ARRAY)
print(sorted(ARRAY), 'test')


def f(arr):
    for i in range(len(arr)):
        more_or_eq = 0
        less_or_eq = 0
        eq = -1
        spam = arr[i]
        median = None
        for item in arr:
            if spam >= item:
                more_or_eq += 1
            if spam <= item:
                less_or_eq += 1
            if spam == item:
                eq += 1
            median = spam

        if eq > -1:
            if more_or_eq > less_or_eq:
                more_or_eq -= eq
            elif more_or_eq < less_or_eq:
                less_or_eq -= eq
        if more_or_eq == less_or_eq:
            return median


print(f(ARRAY))
