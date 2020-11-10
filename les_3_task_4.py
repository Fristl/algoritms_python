"""Определить, какое число в массиве встречается чаще всего"""

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


help_dict = {}
count_num = 0
num = None

for num_ in array:
    if num_ in help_dict:
        help_dict[num_] += 1
    else:
        help_dict[num_] = 1

for key_, values in help_dict.items():
    if count_num < values:
        count_num = values
        num = key_

print(f'Число {num} встретилось больше всего : {count_num} раз(а)')

#######################################################


def wer(array_, digit, count_num_):
    b = array.copy()
    if len(array_) > 0:
        w = array_[0]
        while True:
            if w in array_:
                array_.remove(w)
            else:
                if len(b) - len(array_) > count_num_:
                    count_num_ = len(b) - len(array_)
                    digit = w
                break
        return wer(array_, digit, count_num_)
    return f'Число {digit} встретилось {count_num_} раз(а)'


count_num_1 = 0
num_1 = None

print(array)
print(wer(array, num_1, count_num_1))

"""Задумка с рекурсией не моя, но стало интерсно реализовать.
Так сказать поработать с тем, что дали =) Мой код - первая реализация"""
