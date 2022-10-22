import json
def get_data():
    with open('file.json', 'r', encoding='utf-8') as f: #открыли файл
        text = json.load(f) #загнали все из файла в переменную
        return text #вывели результат на экран
 
# for txt in text['personal']: #создали цикл, который будет работать построчно
#     print(txt['name'], ':', txt['salary']) #и выводим на экран все, что в значении ключей name и salary

