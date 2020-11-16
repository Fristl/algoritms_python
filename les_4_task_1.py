"""Определить, какое число в массиве встречается чаще всего"""

import cProfile
import timeit
import random


def gen_ar(size_):
    SIZE = size_
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array


s = """
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
"""


#######################################################


s1 = """
def wer(array_, digit, count_num_):
    b = len(array_copy_.copy())
    if len(array_) > 0:
        w = array_[0]
        while True:
            if w in array_:
                array_.remove(w)
            else:
                l_a = len(array_)
                if b - l_a > count_num_:
                    count_num_ = b - l_a
                    digit = w
                break
        return wer(array_, digit, count_num_)
    return f'Число {digit} встретилось {count_num_} раз(а)'


array_copy_ = array.copy()
count_num_1 = 0
num_1 = None

wer(array_copy_, num_1, count_num_1)
"""


#######################################################


s2 = """
array_copy_2 = array.copy()
count_num_2 = 0
num_2 = None

while array_copy_2:
    item = array_copy_2[0]
    c = array_copy_2.count(item)
    if c > count_num_2:
        count_num_2 = c
        num_2 = item
    while item in array_copy_2:
        array_copy_2.remove(item)
"""

print('****************')

array = gen_ar(10)
print(timeit.timeit(s, number=100, globals=globals()))       # 0.00037769999999998083
cProfile.run(s)
# Всё идеально 0.000

array = gen_ar(100)
print(timeit.timeit(s, number=100, globals=globals()))       # 0.0028831999999999747
cProfile.run(s)
# Всё идеально 0.000

array = gen_ar(1000)
print(timeit.timeit(s, number=100, globals=globals()))       # 0.01987
cProfile.run(s)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}

array = gen_ar(10_000)
print(timeit.timeit(s, number=100, globals=globals()))       # 0.19604009999999994
cProfile.run(s)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}

"""При реализации со словарём всё работает быстро.
Зависимость от количества элементов не хуже O(n)"""
print('\n\n\n\n\n')
#######################################################

array = gen_ar(10)
print(timeit.timeit(s1, number=100, globals=globals()))      # 0.0010658000000000056
cProfile.run(s1)
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:2(<module>)
#    8/1    0.000    0.000    0.000    0.000 <string>:2(wer)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     23    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      9    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

array = gen_ar(100)
print(timeit.timeit(s1, number=100, globals=globals()))      # 0.024874000000000063
cProfile.run(s1)
# 443 function calls (376 primitive calls) in 0.001 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:2(<module>)
#   68/1    0.000    0.000    0.000    0.000 <string>:2(wer)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    203    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     69    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    100    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

array = gen_ar(1000)
print(timeit.timeit(s1, number=100, globals=globals()))      # 1.3989762
cProfile.run(s1)
# 1513 function calls (1412 primitive calls) in 0.015 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.015    0.015 <string>:2(<module>)
#  102/1    0.009    0.000    0.015    0.015 <string>:2(wer)
#      1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#    305    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    103    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1000    0.006    0.000    0.006    0.000 {method 'remove' of 'list' objects}

array = gen_ar(10_000)
print(timeit.timeit(s1, number=100, globals=globals()))      # 124.30215079999999
cProfile.run(s1)
# 10513 function calls (10412 primitive calls) in 1.265 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    1.263    1.263 <string>:2(<module>)
# 102/1    0.650    0.006    1.262    1.262 <string>:2(wer)
#     1    0.002    0.002    1.265    1.265 {built-in method builtins.exec}
#   305    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   103    0.002    0.000    0.002    0.000 {method 'copy' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 10000    0.610    0.000    0.610    0.000 {method 'remove' of 'list' objects}

"""При реализации через рекурсию время выполнения
от количества элементов заметно увеличивается.
Это связано с тем, что удаление элементов из масива
достаточно затратная в сумме по времени операция,
так как происходит очень много вызовов
метода уделения элемента в этой реализации.

Однако на малых количествах данных, всё работает быстро.
Но это связано лишь с малым количеством данных.
Зависимость от количества элементов не хуже O(n^2)"""
print('\n\n\n\n\n')
#######################################################

array = gen_ar(10)
print(timeit.timeit(s2, number=100, globals=globals()))      # 0.0007296999999999998
cProfile.run(s2)
#  1    0.000    0.000    0.000    0.000 <string>:2(<module>)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
# 10    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 10    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

array = gen_ar(100)
print(timeit.timeit(s2, number=100, globals=globals()))      # 0.02599020000000002
cProfile.run(s2)
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:2(<module>)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#    62    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   100    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

array = gen_ar(1000)
print(timeit.timeit(s2, number=100, globals=globals()))      # 1.4282355999999998
cProfile.run(s2)
# 1105 function calls in 0.014 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.007    0.007    0.014    0.014 <string>:2(<module>)
#     1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#   101    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  1000    0.005    0.000    0.005    0.000 {method 'remove' of 'list' objects}


array = gen_ar(10_000)
print(timeit.timeit(s2, number=100, globals=globals()))      # 123.6928081
cProfile.run(s2)
# 10105 function calls in 1.197 seconds
#     1    0.614    0.614    1.197    1.197 <string>:2(<module>)
#     1    0.000    0.000    1.197    1.197 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#   101    0.012    0.000    0.012    0.000 {method 'count' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 10000    0.572    0.000    0.572    0.000 {method 'remove' of 'list' objects}
"""При реализации через циклы время выполнения
от количества элементов кратно увеличивается.
Это связано с тем, что происходит многократное прохождение по массиву: цикл в цикле.
Также метод удаления элементов из массива суммарно занимает много времени.
Зависимость от количества элементов не хуже O(n^2)"""
