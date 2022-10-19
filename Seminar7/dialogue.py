def choose_format():
    # print()
    choose = int(input('Choose a format - how to write data:\n 1. Vertical\n 2. Horizontal\n'))
    return choose

def inputing_data():
    data = []
    data.append(input('input first_name ='))
    data.append(input('input last_name ='))
    data.append(input('input patronymic ='))
    data.append(input('input description ='))
    return data    

def write_data_to_file():
    format = choose_format()
    data = inputing_data()
    
    if format == 1:
        file = open('Seminar7/format1.txt', 'a')
        [file.write(i + '\n') for i in data]
        file.write('\n')
    elif format == 2:
        file = open('format2.txt', 'a')
        file.write(','.join(data))
        file.write('\n')
    file.close

# choose_format()
# inputing_data()
# write_data_to_file()


# def a():
#     file = open('format1.txt', 'w')
#     file.write('geas')
#     file.close

# a()
