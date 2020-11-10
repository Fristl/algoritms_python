"""В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте
«минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


max_negative_el = MIN_ITEM

for item in array:
    if max_negative_el < item < 0:
        max_negative_el = item

print(max_negative_el if max_negative_el < 0 else 'В массиве нет отрицательных чисел!')
