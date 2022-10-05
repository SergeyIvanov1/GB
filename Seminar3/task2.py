# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
import numbers

def func(list):
    result = []

    pos = 0
    neg = -1
    mul = 0
    count_actions = math.ceil(len(list)/2)
    
    for i in range(count_actions):
        mul = list[pos] * list[neg]
        result.append(mul)
        pos += 1
        neg -= 1
    print(result)

list = [6, 2, 4, 3, 5, 7, 3, 9, 1]
func(list)
