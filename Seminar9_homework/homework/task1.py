# Создайте программу для игры 
# в "Крестики-нолики" при помощи виртуального окружения и PIP

import json
from .is_odd import isOdd

def get_data():
    with open('file.json', 'r', encoding='utf-8') as f: 
        text = json.load(f) 
        return text 


def make_field(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-' * 13)

def take_input(symbol):
    valid = False
    while not valid:
        response = input('There will be ' + symbol + ' ?')
        try:
            response = int(response)
        except:
            print('enter digit from 1 to 9')
            continue
        if 1 <= response <= 9:
            if str(field[response - 1]) not in 'XO':    
                field[response - 1] = symbol
                valid = True
            else:
                print('this cell is bysy')   
        else:
            print('enter digit from 1 to 9')

def verification(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))         
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False        

def main(field):
    counter = 0
    win = False
    while not win:
        make_field(field)
        if isOdd(counter):
            take_input('0')
        else:
            take_input('X')
        counter += 1
        if counter > 4:
            tmp = verification(field)
            if tmp:
                print(tmp, 'win')
                win = True
                break
        if counter == 9:
            print('equals')
            break
    make_field(field)

if __name__ == '__main__':
    field = list(range(1,10))

    main(field)
    
