

def decompression():
    file = open('Seminar5/output.txt', 'r')
    init_str = file.readline()
    file.close

    number_to_str = ''
    enum_chars = ''
    result = []
    prev_symbols_is_char = False

    for i in init_str:
        if i.isalpha():
            enum_chars = enum_chars + i
            prev_symbols_is_char = True
        elif (prev_symbols_is_char and i.isdigit()):
            result.append(number_to_str)
            result.append(enum_chars)
            number_to_str = i
            enum_chars = ''
            prev_symbols_is_char = False
        elif (i == '-' and number_to_str != ''):
            result.append(number_to_str)
            result.append(enum_chars)
            number_to_str = '-'
            enum_chars = ''
            prev_symbols_is_char = False
        else:
            number_to_str = number_to_str + i    
            prev_symbols_is_char = False
        
    result.append(number_to_str)
    result.append(enum_chars)

    finish_result = ''
    count = 1
    for k in result:
        if k.isdigit():
            count = int(k)
        elif (k.find('-')==0):
            continue    
        else:
            finish_result = finish_result + (k * count)
            count = 1

    
    file = open('Seminar5/file.txt', 'w')
    file.write(finish_result)
    file.close

decompression()

# example:
# task: 2s-5nhhgh3s3l3k-1h
# result: ssnhhghssslllkkkh