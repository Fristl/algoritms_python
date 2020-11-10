"""В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_el = MAX_ITEM
max_el = MIN_ITEM
idx_min = 0
idx_max = SIZE - 1
sum_ = 0

for idx, item in enumerate(array):
    if item > max_el:
        max_el = item
        idx_max = idx

    if item < min_el:
        min_el = item
        idx_min = idx

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

for index in range(idx_min + 1, idx_max):
    sum_ += array[index]

print(f'{min_el=}, {max_el=}')
print(sum_)
