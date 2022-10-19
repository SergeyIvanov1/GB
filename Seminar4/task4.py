# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint


def func(k):

    s = ""
   
    for i in range(0, k + 1):
        random = str(randint(1,101))
        kf = str(i)
        if i == 0:
            s = random + ' = 0'
        elif i == 1:
            s = random + '*x' + ' + ' + s
        else:     
            s = random + '*x^' + kf + ' + ' + s
        
        file = open('Seminar4/file4.txt','w')  
        file.write(s)
        file.close

k = int(input('input k = '))
func(k)

# result (k = 5): 88*x^5 + 34*x^4 + 55*x^3 + 12*x^2 + 18*x + 98 = 0
