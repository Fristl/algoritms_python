"""Найти максимальный элемент
среди минимальных элементов столбцов матрицы"""

import random

SIZE_A = 4
SIZE_B = 5
MIN_ITEM = -100
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_A)]
          for _ in range(SIZE_B)]
print(*matrix, '\nНаименьшие элементы в столбцах:', sep='\n')


max_of_the_small = MIN_ITEM

for spam in range(SIZE_A):
    minimal_in_column = matrix[0][spam]
    for eggs in range(1, SIZE_B):
        if matrix[eggs][spam] < minimal_in_column:
            minimal_in_column = matrix[eggs][spam]
    print(minimal_in_column, end='  ')

    if max_of_the_small < minimal_in_column:
        max_of_the_small = minimal_in_column

print(f'\n\nМаксимальный элемент '
      f'среди минимальных элементов столбцов: {max_of_the_small}')
