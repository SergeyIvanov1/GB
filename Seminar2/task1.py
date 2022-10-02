# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

text = input('input number N = ')
sum = 0

for k in text:
    if (k.isdigit()):
        sum += int(k)
print(sum)