import datetime
import view

def log_cash(mod):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Выбранный режим: {mod}. Время запроса: {str(datetime.datetime.now())} \n')
