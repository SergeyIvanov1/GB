# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

file = open('Seminar4/file.txt','r')
a = file.readline()
print(a)

file.close

file = open('Seminar4/file2.txt','r')
b = file.readline()
print(b)

file.close

s = ""
s = a + ' + ' +  b

file = open('Seminar4/file3.txt','w')
file.write(s)

file.close