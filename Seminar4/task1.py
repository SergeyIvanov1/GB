# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

import math

def func(d, pi):
    count = str(len(d.split('.')[1]))
    accuracy = "." + count + 'f'

    print(format(pi, accuracy))
  

pi = math.pi
d = input('input d = ')
func(d, pi)

# result: 
# input d = 0.00001
# output: 3.14159