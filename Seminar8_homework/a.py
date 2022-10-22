import csv
import codecs


def read_last_id(file_csv): 
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line.strip().split(',')
        last_id = last_line[0]
        if last_id.isdigit() == False:
            last_id = 0
        else:
            last_id = int(last_id)
        return last_id + 1

def new_contact_keyboard_input(file_csv, fieldnames):
    print('')
    print('Введите данные ученика')
    new_contact = []
    for i in range(1, len(fieldnames)):
        new_contact.append(str(input(f'{fieldnames[i]} : ')))
    if new_contact == '':
        new_contact.append('NONE')
    add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames)
    print('')


def add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames):
    new_contact.insert(0, read_last_id(file_csv))
    with open(file_csv, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames, restval=None)
            writer.writerow({fieldnames[i]: new_contact[i] for i in range(len(fieldnames))})
            # dict = {}
            # for i in range(0, len(fieldnames) - 1):
            #     dict[fieldnames[i]] = new_contact[i]
            # writer.writerow(dict)
            
         


file_csv = 'Seminar8_homework/class.csv'
# file_csv = 'Seminar8_homework/text.txt'

fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Литера', 'Дата_рождения', 'Номер_телефона', 'Пометка_перевода']
# new_contact = ['Сергеев', 'Сергей', 'Сергеевич', '7', 'а', '08-04-2010', '89632541236', 'NONE']
# add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames)
new_contact_keyboard_input(file_csv, fieldnames)
