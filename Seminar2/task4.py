# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

from random import randint


def func(N):
    arr = []
    multiply = 1

    for i in range(N):
        arr.append(randint(-N, N))

    file = open('Seminar2/file.txt', 'r')

    for k in file:
        multiply = multiply * arr[int(k)]

    file.close()    
    
    print(multiply)


N = int(input('input N = '))
func(N)
