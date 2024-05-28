from datetime import datetime
import json
import os


def operations_reader(path=os.path.abspath('operations.json')) -> list:
    '''
    Читаем и возвращаем содержимое файла "operations.json"
    '''
    with open(path, 'r') as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    return [operation for operation in operations if operation.get('state') == 'EXECUTED']


def sort_operations_by_date(executed_operations: list[dict]) -> list[dict]:
    pattern = '%Y-%m-%dT%H:%M:%S.%f'
    return sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], pattern), reverse=True)


def last_operations(sorted_operations: list[dict], n: int) -> list[dict]:
    '''
    Возвращает n последних "executed" операций
    '''
    return sorted_operations[:n]


def get_date(date: str) -> str:
    '''
    Возвращаем дату в необходимом оформлении
    '''
    pattern = '%Y-%m-%dT%H:%M:%S.%f'
    dt = datetime.strptime(date, pattern)
    return dt.strftime('%d.%m.%Y')


def get_valid_card_info(info: str) -> str:
    '''
    Возвращаем информацию по карте/счету-отправителю в необходимом формате
    '''
    if 'Счет' in info:
        sender = info.replace(info[-20: -4], 2 * '*')
        return sender
    else:
        splitter_by_space = info.split()
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


def get_info_by_operation(operation: dict):
    date = get_date(operation['date'])
    description = operation['description']
    if 'from' not in operation:
        outgoing = 'Нет данных об отправителе'
    else:
        outgoing = get_valid_card_info(operation['from'])
    incoming = get_valid_card_info(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    return f'''{date} {description}
{outgoing} -> {incoming}
{amount} {currency}
'''

# def get_last_executed_operations(info: list) -> list:
#     '''
#     Возвращаем всю доступную информацию за последние 5 операций
#     '''
#     pattern = '%Y-%m-%dT%H:%M:%S.%f'
#     executed_operations = [el for el in info if el and el['state'] == 'EXECUTED']
#     sorted_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], pattern))
#     return sorted_operations[-1:-6:-1]
#
#
# def get_date(date: str) -> str:
#     '''
#     Возвращаем дату в необходимом оформлении
#     '''
#     pattern = '%Y-%m-%dT%H:%M:%S.%f'
#     dt = datetime.strptime(date, pattern)
#     return dt.strftime('%d.%m.%Y')
#
#
# def get_valid_card_info(info: str) -> str:
#     '''
#     Возвращаем информацию по карте/счету-отправителю в необходимом формате
#     '''
#     if 'Счет' in info:
#         sender = info.replace(info[-20: -4], 2 * '*')
#         return sender
#     else:
#         splitter_by_space = info.split()
#         first_four = splitter_by_space[-1][-16:-12]
#         second_four = splitter_by_space[-1][-12:-8]
#         third_four = splitter_by_space[-1][-8: -4]
#         four_four = splitter_by_space[-1][-4:]
#         new_splitter = splitter_by_space[:-1]
#         new_splitter.extend([first_four,
#                             second_four.replace(second_four[-2:], '**'),
#                             third_four.replace(third_four, '****'),
#                             four_four])
#         return ' '.join(new_splitter)


