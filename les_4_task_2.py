"""Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

import cProfile
import timeit


def sieve_f1(m):
    n = m * 10
    index = -1

    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            index += 1
            if index == m:
                return i
            while j < n:
                sieve[j] = 0
                j += i


##############################################


def sieve_f2(m):
    n = m * 10
    sieve = [2]

    for i in range(3, n):
        for item in sieve:
            if i % item == 0:
                break
            elif i % item != 0 and item != sieve[-1]:
                continue
            else:
                sieve.append(i)

    return sieve[m]

##############################################


idx = 5
print(sieve_f1(idx))
print(sieve_f2(idx))

cProfile.run('sieve_f1(idx)')
# Всё идеально 0.000

cProfile.run('sieve_f2(idx)')
# Всё идеально 0.000

print(timeit.timeit('sieve_f1(idx)', number=100, globals=globals()))    # 0.0015459999999999918
print(timeit.timeit('sieve_f2(idx)', number=100, globals=globals()))    # 0.0035118999999999845
print('**************')
print('\n\n\n\n\n')


idx = 25
print(sieve_f1(idx))
print(sieve_f2(idx))

cProfile.run('sieve_f1(idx)')
# Всё идеально 0.000

cProfile.run('sieve_f2(idx)')
# Всё идеально 0.000

print(timeit.timeit('sieve_f1(idx)', number=100, globals=globals()))    # 0.008563399999999999
print(timeit.timeit('sieve_f2(idx)', number=100, globals=globals()))    # 0.03307840000000001
print('**************')
print('\n\n\n\n\n')


idx = 125
print(sieve_f1(idx))
print(sieve_f2(idx))

cProfile.run('sieve_f1(idx)')
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}

cProfile.run('sieve_f2(idx)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#     1    0.005    0.005    0.005    0.005 les_4_task_2.py:38(sieve_f2)
#     1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#   203    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('sieve_f1(idx)', number=100, globals=globals()))    # 0.0593601
print(timeit.timeit('sieve_f2(idx)', number=100, globals=globals()))    # 0.48213940000000005
print('**************')
print('\n\n\n\n\n')


idx = 625
print(sieve_f1(idx))
print(sieve_f2(idx))

cProfile.run('sieve_f1(idx)')
# 5 function calls in 0.003 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#     1    0.002    0.002    0.003    0.003 les_4_task_2.py:17(sieve_f1)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:21(<listcomp>)
#     1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve_f2(idx)')
# 815 function calls in 0.073 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.073    0.073 <string>:1(<module>)
#     1    0.073    0.073    0.073    0.073 les_4_task_2.py:38(sieve_f2)
#     1    0.000    0.000    0.073    0.073 {built-in method builtins.exec}
#   811    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('sieve_f1(idx)', number=100, globals=globals()))    # 0.3077023
print(timeit.timeit('sieve_f2(idx)', number=100, globals=globals()))    # 7.7634395000000005
print('**************')
print('\n\n\n\n\n')


idx = 3125
print(sieve_f1(idx))
print(sieve_f2(idx))

cProfile.run('sieve_f1(idx)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#     1    0.014    0.014    0.015    0.015 les_4_task_2.py:17(sieve_f1)
#     1    0.002    0.002    0.002    0.002 les_4_task_2.py:21(<listcomp>)
#     1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve_f2(idx)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    1.333    1.333 <string>:1(<module>)
#     1    1.332    1.332    1.333    1.333 les_4_task_2.py:38(sieve_f2)
#     1    0.000    0.000    1.333    1.333 {built-in method builtins.exec}
#  3367    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('sieve_f1(idx)', number=100, globals=globals()))    # 1.5843229999999995
print(timeit.timeit('sieve_f2(idx)', number=100, globals=globals()))    # 135.07800780000002


"""В первом варианте с решетом Эротосфена алгоритм работает при O(n).
Особо плохих участков в коде не обнаружено.
Во втором же варианте зависимость O(2n) (если конечно так можно выразиться,
на самом деле с каждым увеличением n в 5 раз зависимость увеличивается, чем больше,
тем больше зависимость). Большая часть времени тратится на проверки условий.
При этом второй вариант менее читаемый
"""
