# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

def func(list):

    result = []
    marker = True
        
    for i in list:
        for k in result:
            if i == k:
                marker = False
                break     
        if marker:    
            result.append(i)
        marker = True
    print(result)

list = [1, 1, 2, 3, 7, 9, 3, 7]
func(list)
