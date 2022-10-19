# Создайте программу для игры в "Крестики-нолики".

from re import T


def drow_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input('There will be ' + player_token + ' ?')
        try:
            player_answer = int(player_answer)
        except:
            print('input numbwer from 1 to 9')
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in 'XO':    
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('this cell is bysy')   
        else:
            print('input numbwer from 1 to 9')

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))         
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False        

def main(board):
    counter = 0
    win = False
    while not win:
        drow_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('0')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'win')
                win = True
                break
        if counter == 9:
            print('equals')
            break
    drow_board(board)

if __name__ == '__main__':
    print('play')    
    board = list(range(1,10))

    main(board)
    print('input enter')


