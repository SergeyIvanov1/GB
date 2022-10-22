from random import randint
import example


def play(data):
    count_sweets = data
    first_player_count = 0
    second_player_count = 0  
    
    choose_first_player = 0
    choose_second_player = 0

    who_move_first = randint(1, 3)

    if who_move_first == 1:

        while count_sweets > 0:
            choose_first_player = int(input('number of first player = '))
            choose_second_player = int(input('number of second player = '))

            first_player_count += choose_first_player
            second_player_count += choose_second_player

            count_sweets -= first_player_count
            if count_sweets <= 0:
                print('first player is winner')
                break
            count_sweets -= second_player_count 
            if count_sweets <= 0:
                print('second player is winner')
                break

            choose_first_player = 0
            choose_second_player = 0

    else:

        while count_sweets > 0:
            choose_second_player = int(input('number of second player = ')) 
            choose_first_player = int(input('number of first player = '))

            second_player_count += choose_second_player
            first_player_count += choose_first_player

            count_sweets -= second_player_count 
            if count_sweets <= 0:
                print('second player is winner')
                break
            count_sweets -= first_player_count
            if count_sweets <= 0:
                print('first player is winner')
                break
            
            choose_second_player = 0
            choose_first_player = 0

data = example.get_data()["initial"]
# print(data)
play(data)

# def play_with_bot(data):
#     count_sweets = data
#     first_player_count = 0
#     bot_count = 0  
    
#     choose_first_player = 0
#     choose_bot = 0

#     who_move_first = randint(1, 3)

#     if who_move_first == 1:

#         while count_sweets > 0:
#             choose_first_player = int(input('number of first player = '))
#             choose_bot = randint(1, 28) 
           
#             print('choose_bot')
#             print(choose_bot)

#             first_player_count += choose_first_player
#             bot_count += choose_bot

#             count_sweets -= first_player_count
#             if count_sweets <= 0:
#                 print('first player is winner')
#                 break
#             count_sweets -= bot_count 
#             if count_sweets <= 0:
#                 print('bot is winner')
#                 break

#             choose_first_player = 0
#             choose_bot = 0

#             print('\nCOUNT_SWEET')
#             print(count_sweets)
#     else:

#         while count_sweets > 0:
#             choose_bot = randint(1, 29) 
#             choose_first_player = randint(1, 29)
            
#             print('choose_bot')
#             print(choose_bot)

#             bot_count += choose_bot
#             first_player_count += choose_first_player

#             count_sweets -= bot_count 
#             if count_sweets <= 0:
#                 print('bot is winner')
#                 break
#             count_sweets -= first_player_count
#             if count_sweets <= 0:
#                 print('first player is winner')
#                 break
            
#             choose_bot = 0
#             choose_first_player = 0

#             print('\nCOUNT_SWEET')
#             print(count_sweets)

# play_with_bot(data)

# number of first player = 28
# choose_bot
# 11

# COUNT_SWEET
# 62
# number of first player = 28
# choose_bot
# 21
# bot is winner