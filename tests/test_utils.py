from coursework3.utils import (operations_reader,
                               get_executed_operations,
                               sort_operations_by_date,
                               last_operations,
                               get_date,
                               get_valid_card_info,
                               get_info_by_operation)
import pytest
from datetime import datetime


def test_operations_reader():
    with pytest.raises(FileNotFoundError):
        operations_reader('gcadjdacd.txt')


def test__get_executed_operations():
    operations = [
        {},
        {'state': 'EXECUTED'},
        {'state': 'fghahiiufh'}
    ]
    expected_operations = [
        {'state': 'EXECUTED'}
    ]
    executed_oper = get_executed_operations(operations)
    assert isinstance(executed_oper, list)
    assert len(executed_oper) == 1
    assert executed_oper == expected_operations
    assert isinstance(executed_oper[0], dict)


def test__sort_operations_by_date():
    operations = [
        {"date": "2019-08-26T10:50:58.294041"},
        {"date": "2018-08-26T10:50:58.294041"},
        {"date": "2020-08-26T10:50:58.294041"}
    ]
    expected_operations = [
        {"date": "2020-08-26T10:50:58.294041"},
        {"date": "2019-08-26T10:50:58.294041"},
        {"date": "2018-08-26T10:50:58.294041"}
    ]
    sort_operations = sort_operations_by_date(operations)
    assert sort_operations == expected_operations
    assert isinstance(sort_operations, list)
    assert isinstance(sort_operations[0], dict)
    assert len(sort_operations) == 3


def test__last_operations():
    operations = [
        {1: 1},
        {2: 2},
        {3: 3},
        {4: 4},
        {5: 5}
    ]
    expected_operations = [
        {1: 1},
        {2: 2}
    ]
    count_of_operations = 2
    last_operations_2 = last_operations(operations, count_of_operations)
    assert len(last_operations_2) == count_of_operations
    assert isinstance(last_operations_2, list)
    assert isinstance(last_operations_2[1], dict)
    assert last_operations_2 == expected_operations


def test__get_info_by_operation():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    expected_operation = (
        '26.08.2019 Перевод организации\n'
        'Maestro 1596 83** **** 5199 -> Счет **9589\n'
        '31957.58 руб.\n'
    )
    operation_info = get_info_by_operation(operation)
    assert operation_info == expected_operation
    assert isinstance(operation_info, str)


def test__get_date():
    assert get_date('2019-04-04T23:20:05.206878') == '04.04.2019'
    assert isinstance(get_date('2019-04-04T23:20:05.206878'), str)


def test__get_valid_card_info():
    info = [
        {'to': 'Счет 75651667383060284188'},
        {'from': 'Visa Platinum 8990922113665229'}
    ]
    expected_info1 = 'Счет **4188'
    expected_info2 = 'Visa Platinum 8990 92** **** 5229'
    assert get_valid_card_info(info[0]['to']) == expected_info1
    assert get_valid_card_info(info[1]['from']) == expected_info2






# def test_get_date():
#     assert get_date('2001-06-23T00:00:27.000000') == '23.06.2001'
#     assert get_date('7777-12-31T01:00:29.675683') == '31.12.7777'
#     assert get_date('2024-05-24T16:41:00.675683') == '24.05.2024'
#
#
# def test_get_valid_card_info():
#     assert get_valid_card_info('Visa Classic 2747493856472064') == 'Visa Classic 2747 49** **** 2064'
#     assert get_valid_card_info('Счет 67483906574839265789') == 'Счет **5789'
#     assert get_valid_card_info('Счет 84638965374503265647') == 'Счет **5647'
#     assert get_valid_card_info('Master Card 4856397584036274') == 'Master Card 4856 39** **** 6274'
#
#
# @pytest.mark.parametrize('exception1, filename', [
#     (FileNotFoundError, 'efegje.txt')
# ])
# def test_operations_reader(exception1, filename):
#     with pytest.raises(exception1):
#         operations_reader(filename)
#
#
# @pytest.mark.parametrize('exception, example', [
#     (TypeError, [1, 2, 3, 4, 5]),
#     (KeyError, [{'states': 'EXECUTED', 'id': 246455}]),
#     (ValueError, [{'state': 'EXECUTED', 'date': '23.06.2001'}]),
#     (ValueError, [{'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878py'}])
# ])
# def test_get_last_executed_operations(exception, example):
#     with pytest.raises(exception):
#         assert get_last_executed_operations(example)





