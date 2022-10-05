# 3. Задайте список из n чисел последовательности (1+ 1/n)^n 
# и выведите на экран их сумму (округляйте до 3 знаков после запятой).

# Пример:

# - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
# Вывод: 14.031 (2 + 2.25 + 2.37 + 2.441 + 2.448 + 2.522)

numberN = int(input('input number N = '))
numbers = list(range(1, numberN + 1)) 
sum = 0
result = 0

for n in numbers:
    result =  round(((1 + 1/n)**n), 3)
    sum += result
print(sum)
