from datetime import datetime
import json


def operations_reader() -> list:
    '''
    Читаем и возвращаем содержимое файла "operations.json"
    '''
    with open('operations.json', 'r') as file:
        return json.load(file)


def get_last_executed_operations(info: list) -> list:
    '''
    Возвращаем всю доступную информацию за последние 5 операций
    '''
    pattern = '%Y-%m-%dT%H:%M:%S.%f'
    executed_operations = [el for el in info if el and el['state'] == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], pattern))
    return sorted_operations[-1:-6:-1]


def get_date(date: str) -> str:
    '''
    Возвращаем дату в необходимом оформлении
    '''
    pattern = '%Y-%m-%dT%H:%M:%S.%f'
    dt = datetime.strptime(date, pattern)
    return dt.strftime('%d.%m.%Y')


def get_valid_sender(sender: str) -> str:
    '''
    Возвращаем информацию по карте/счету-отправителю в необходимом формате
    '''
    if 'Счет' in sender:
        sender = sender.replace(sender[-20: -4], 2 * '*')
        return sender
    else:
        splitter_by_space = sender.split()
        first_four = splitter_by_space[-1][-16:-12]
        second_four = splitter_by_space[-1][-12:-8]
        third_four = splitter_by_space[-1][-8: -4]
        four_four = splitter_by_space[-1][-4:]
        new_splitter = splitter_by_space[:-1]
        new_splitter.extend([first_four,
                            second_four.replace(second_four[-2:], '**'),
                            third_four.replace(third_four, '****'),
                            four_four])
        return ' '.join(new_splitter)



def get_valid_receiver(receiver: str) -> str:
    '''
    Возвращаем информацию по карте/счету-получателю в необходимом формате
    '''
    if 'Счет' in receiver:
        receiver = receiver.replace(receiver[-20: -4], 2 * '*')
        return receiver
    else:
        splitter_by_space = receiver.split()
        first_four = splitter_by_space[-1][-16:-12]
        second_four = splitter_by_space[-1][-12:-8]
        third_four = splitter_by_space[-1][-8: -4]
        four_four = splitter_by_space[-1][-4:]
        new_splitter = splitter_by_space[:-1]
        new_splitter.extend([first_four,
                            second_four.replace(second_four[-2:], '**'),
                            third_four.replace(third_four, '****'),
                            four_four])
        return ' '.join(new_splitter)




