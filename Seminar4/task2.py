# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def func(number):

    result = []
    div = number
    
    while div != 1:
        for i in range(2, div + 1):
            if (div % i == 0):
                result.append(i)
                div = int(div / i)
                break         
                
    print(result)

number = int(input('input number = '))
func(number)
