# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('input number = '))

def fibonacci(number):
    arr = []
    a, b  = 1, 1
    
    for i in range(number):
        arr.append(a)
        a, b = b, a + b
    
    a , b = 0, 1
 
    for k in range(0, number + 1):
        arr.insert(0 , a)
        a, b = b, a - b 
    return arr   

print(fibonacci(number))