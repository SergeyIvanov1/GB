# Задача: предложить улучшения кода для уже решённых задач 
# с помощью использования лямбд, filter, map, zip, enumerate, list comprehension.



# ______________________________________________________________________________________
# Task3. Seminar2. Задайте список из n чисел последовательности (1+ 1/n)^n 
# и выведите на экран их сумму (округляйте до 3 знаков после запятой).

# Пример:

# - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
# Вывод: 14.031 (2 + 2.25 + 2.37 + 2.441 + 2.448 + 2.522)

# import math


# numberN = int(input('input number N = '))
# numbers = list(range(1, numberN + 1)) 
# sum = 0
# result = 0

# for n in numbers:
#     result =  round(((1 + 1/n)**n), 3)
#     sum += result
# print(sum)
   
# ______________________________________________________________________________________
# example with list comprehension

def get_set(numbers):
    return [round(((1 + 1/n)**n), 3) for n in numbers]
    

numberN = int(input('input number N = '))
numbers = list(range(1, numberN + 1)) 

set = get_set(numbers)
print(sum(set))