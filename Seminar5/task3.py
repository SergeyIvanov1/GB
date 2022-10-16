# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



file = open('Seminar5/input.txt', 'r')
init_str = file.readline()

intermediate_result = ''
count_positive = 1

char_of_str = init_str[0]

for i in init_str[1:]:
    if i == char_of_str:
        count_positive += 1
    else:
        intermediate_result = intermediate_result + str(count_positive) + char_of_str
        count_positive = 1
        char_of_str = i

intermediate_result = intermediate_result + str(count_positive) + char_of_str

result = ''
count_negative = -1

for k in intermediate_result:
    if k.isdigit():
        digit = int(k)
        if (digit > 1 and ('*' in result)):
            result = result.replace('*', str(count_negative))
            count_negative = -1
            result = result + k
            continue
        elif (digit == 1 and ('*' in result)):
            count_negative -= 1
            continue
        elif (digit == 1):
            result = result + '*'
            continue

    result = result + k

if (count_negative != -1):
    result = result.replace('*', str(count_negative))
if (count_negative == -1 and ('*' in result)):
    result = result.replace('*', str(count_negative))

file = open('Seminar5/output.txt', 'w')
file.write(result)

# example:
# task: ssvbsxdbfghghssslllkkkh2s-5nhhgh3s3l3k-1h
# result: 2s-11vbsxdbfghgh3s3l3k-1h


