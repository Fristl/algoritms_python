"""В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

for digit in range(2, 9 + 1):
    res_ = 0
    for _ in range(digit, 99 + 1, digit):
        res_ += 1
    print(digit, ':', res_)
