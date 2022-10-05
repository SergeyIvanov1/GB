#  2. Напишите программу, которая принимает на вход число N 
#  и выдает набор произведений чисел от 1 до N.

#  Пример:

#  - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

numberN = int(input('input number N = '))
numbers = list(range(1, numberN + 1)) 
result = 1
output = []

for i in numbers:
    values = list(range(1, i + 1))
    for k in values:
        result *= k
    output.append(result)
    result = 1

print(output)
