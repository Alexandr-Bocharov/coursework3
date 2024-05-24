from utils import *

for line in get_last_executed_operations(operations_reader()):
    print(f'''{get_date(line)} {get_description(line)}
{get_sender(line)} -> {get_receiver(line)}
{get_amount(line)} {get_currency(line)}
''')

