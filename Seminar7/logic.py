import codecs
import logger

def choose_format():
    choose = int(input('Choose a format - how to write data:\n 1. Vertical\n 2. Horizontal\n'))
    return choose

def inputing_data():
    data = []
    data.append(input('input last_name = '))
    data.append(input('input first_name = '))
    data.append(input('input patronymic = '))
    data.append(input('input description = '))
    logger.info('inputting data')
    return data    

def write_data_to_file():
    format = choose_format()
    data = inputing_data()
    path1 = 'Seminar7/format1.txt'
    path2 = 'Seminar7/format2.txt'

    if format == 1:
        file = codecs.open(path1, 'a', 'utf-8')
        [file.write(i + '\n') for i in data]
        file.write('\n')
        logger.info('write data to file ' + path1)
    elif format == 2:
        file = codecs.open(path2, 'a', 'utf-8')
        file.write(','.join(data))
        file.write('\n')
        logger.info('write data to file ' + path2)
    file.close()

def outputing_all_data(path):
    file = codecs.open(path, 'r', 'utf-8')
    lines = file.readlines()
    file.close()
    [print(line) for line in lines]
    logger.info('was outputing all data to concole from file by path: ' + path)

