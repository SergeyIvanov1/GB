# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def func(number):

    result = []
    while number != 0:
        result.append(str(number % 2))
        number = int(number / 2)
       
    result.reverse()
    string = ''
    for i in result:
        string = string + i
    
    print(string)

number = int(input('input number = '))
func(number)


