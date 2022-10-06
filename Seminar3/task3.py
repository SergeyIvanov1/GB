# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func(list):
    new_list = []
    result_list = []

    for h in list:
        new_list.append(float(h))
    
    for i in new_list:
        number = float('0.' + str(i).split('.')[1])
        result_list.append(number)

    max = result_list[0]
    min = result_list[0]

    for k in result_list:
        if k > 0:     
            if k > max:
                max = k
            if k < min:
                min = k

    print(max - min)    
       

list = [1.1, 1.2, 3.1, 5, 10.01]
func(list)
