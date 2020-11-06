"""Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""


def rev_n(number):
    if number // 10 == 0:
        return number

    print(number % 10, end='')
    return rev_n(number // 10)


num = int(input("Введите натуральное число: "))

while num % 10 == 0:
    num //= 10

reverse_num = rev_n(num)

print(reverse_num)
