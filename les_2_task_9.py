"""Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


def f_sum(number, sum_=0):
    if number // 10 == 0:
        sum_ += number
        return sum_
    else:
        sum_ += number % 10
        return f_sum(number // 10, sum_)


num_max = 1
sum_num_max = 1

while True:
    num = int(input("Введите натуральное число: "))

    if num != 0:
        sum_num = f_sum(num)
        if sum_num > sum_num_max:
            sum_num_max = sum_num
            num_max = num
    else:
        print(f'{num_max} : {sum_num_max}')
        break
