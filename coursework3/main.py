from utils import *

for line in get_last_executed_operations(operations_reader()):
    right_date = get_date(line['date'])
    description = line['description']
    if 'from' in line:
        valid_sender = get_valid_sender(line['from'])
    else:
        valid_sender = 'Нет данных об отправителе'
    valid_receiver = get_valid_receiver(line['to'])
    amount = line['operationAmount']['amount']
    currency = line['operationAmount']['currency']['name']
    print(f'''{right_date} {description}
{valid_sender} -> {valid_receiver}
{amount} {currency}
''')

