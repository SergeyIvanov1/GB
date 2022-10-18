# Task2. Seminar2. Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

#  Пример:

#  - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# numberN = int(input('input number N = '))
# numbers = list(range(1, numberN + 1))
# result = 1
# output = []

# for i in numbers:
#     values = list(range(1, i + 1))
#     for k in values:
#         result *= k
#     output.append(result)
#     result = 1

# print(output)

# __________________________________________________________________________________________


def get_result(f, numbers):
   
    return [f(x) for x in range(1, numberN + 1)]

def f(x):
    result = 1
    
    for k in list(range(1, x + 1)):
        result *= k
    return result
  
if __name__ == '__main__':
    numberN = int(input('input number N = '))
       
    print(get_result(f, numberN))

# task: N = 4
# result: [ 1, 2, 6, 24 ] 
