import codecs
import logic

def start():
    action = request_action()
    if action == 1:
        logic.write_data_to_file()
    elif action == 2:
        logic.outputing_all_data(input('input path to file = '))

def request_action():
    return int(input('Enter 1 for inputing data to file or enter 2 for write data from file to concole\n'))

def request_path():
    return input('Input path to file =')    

