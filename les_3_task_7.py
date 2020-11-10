"""В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться."""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_el_1 = float('inf')    # MAX_ITEM
min_el_2 = float('inf')    # MAX_ITEM

for item in array:
    if item < min_el_1:
        min_el_2 = min_el_1
        min_el_1 = item
    elif item < min_el_2:
        min_el_2 = item

print(f'{min_el_1=}, {min_el_2=}')
