# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('input number')
number = int(input())
if (number > 0 and number < 6):
    print('no')
elif(number > 5 and number < 8):
    print('yes')
   
   