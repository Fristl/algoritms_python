"""В массиве случайных целых чисел
поменять местами минимальный и максимальный элементы."""

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_el = float('inf')      # MAX_ITEM
max_el = -float('inf')     # MIN_ITEM
idx_min = 0
idx_max = len(array) - 1   # SIZE - 1

for idx, item in enumerate(array):
    if item > max_el:
        max_el = item
        idx_max = idx

    if item < min_el:
        min_el = item
        idx_min = idx
else:
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]

print(f'{min_el=}, {max_el=}')
print(array)
