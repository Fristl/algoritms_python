"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random


ARRAY = [random.randint(-100, 99) for _ in range(10)]


def buble(arr):
    arr = arr.copy()
    k = 1
    count_step = 0
    for spam in range(len(arr)):
        flag = False
        for i in range(0, len(arr) - k):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
                count_step += 1
        if not flag:
            return f'{arr} {count_step=} - количество действий'
        k += 1


print(ARRAY, 'original')
print(buble(ARRAY))
print(sorted(ARRAY.copy(), reverse=True), 'test')
