import sys


def test1(n1, n2):
    """Функция для проверки правильности операции сложения"""
    answ_1 = hex(int(n1, 16) + int(n2, 16))
    return answ_1, locals()


def test2(n1, n2):
    """Функция для проверки правильности операции умножения"""
    answ_2 = hex(int(n1, 16) * int(n2, 16))
    return answ_2, locals()


def show(x):
    print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}')
    list_mem.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
    return list_mem


list_mem = []
a = (input("Введите первое шестнадцатеричное число: ")).upper()
b = (input("Введите второе шестнадцатеричное число: ")).upper()


answ_1 = test1(a, b)[0]
print(answ_1, '- Сумма чисел')
print('*' * 50, '\n')
sum_mem = sum(show(test1(a, b)[1])[1:])
print(sum_mem)

answ_2 = test2(a, b)[0]
print(answ_2, '- Произведение чисел')
print('*' * 50, '\n')

list_mem = []
sum_mem = sum(show(test2(a, b)[1])[1:])
print(sum_mem)
