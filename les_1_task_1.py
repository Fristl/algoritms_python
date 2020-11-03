"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

# При просмотре надо нажать на "карандаш"(редактирование), тогда появятся и названия листов.
# Через Google Drive не работает
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson_1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1ic0z1B_u-4pw6tmXUQ1uqDvF6i4OswSr%26export%3Ddownload

print("Введите трёхзначное целое число:")

num = int(input())

first_digit = num % 10
second_digit = num // 10 % 10
third_digit = num // 100

sum_ = first_digit + second_digit + third_digit
multiplication = first_digit * second_digit * third_digit

print(f'{sum_=}, {multiplication=}')

"""Можно и без переменных sum_, multiplication.
Тогда вычисление будет прям в print().
Да и без переменных для каждой цифры тоже можно обойтись."""
