# 5. Реализуйте алгоритм перемешивания списка.

from random import randint

def func():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = []
    for i in range(len(arr)):
        index = randint(0, len(arr) - 1)

        result.append(arr[index])
        arr.remove(arr[index])
    print(result)

# N = int(input("input N = "))
func()