"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(arr):
    if len(arr) > 2:
        part_l = merge_sort(arr[:len(arr) // 2])
        part_r = merge_sort(arr[len(arr) // 2:])
        arr = part_l + part_r
        last_index = len(arr) - 1

        for i in range(last_index):
            min_value = arr[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > arr[j]:
                    min_value = arr[j]
                    min_index = j

            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

    elif len(arr) > 1 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]

    return arr


array = [random.uniform(0, 50) for _ in range(7)]
print(array, 'original')
print(merge_sort(array), 'sorted')

"""Честно стырено с вики =|.
Час с листом и карандашом разбирался как работает реализация.
Сложно..."""
