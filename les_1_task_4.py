"""Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число, ● случайное вещественное число, ● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

import random

print("Введите границы интервалов для каждого случая")

int_int_a = int(input("Введите целое число - левую границу интервала для целых чисел: "))
int_int_b = int(input("Введите целое число - правую границу интервала для целых чисел: "))
int_float_a = float(input("Введите число - левую границу интервала для вещественных чисел: "))
int_float_b = float(input("Введите число - правую границу интервала для вещественных чисел: "))
int_symbol_a = ord(input("Введите букву латинского алфавита - левую границу интервала для букв: "))
int_symbol_b = ord(input("Введите букву латинского алфавита - левую границу интервала для букв: "))

res_int_int = random.randint(int_int_a, int_int_b)
res_int_float = random.uniform(int_float_a, int_float_b)
res_int_symbol = chr(random.randint(int_symbol_a, int_symbol_b))

print(res_int_int, res_int_float, res_int_symbol)
