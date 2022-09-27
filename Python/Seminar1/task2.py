# Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('enter values for x, y, z')
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

bool = (not (x or y or z)) == (not x and not y and not z)

if bool:
    print('true')
else:
    print('false')
