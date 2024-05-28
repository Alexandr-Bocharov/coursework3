from utils import (operations_reader,
                   get_executed_operations,
                   sort_operations_by_date,
                   last_operations,
                   get_info_by_operation)


def main():
    exec_operations = get_executed_operations(operations_reader())
    last_five_operations = last_operations(sort_operations_by_date(exec_operations), 5)
    for line in last_five_operations:
        print(get_info_by_operation(line))


if __name__ == '__main__':
    main()