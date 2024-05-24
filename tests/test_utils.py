from coursework3.utils import operations_reader, get_valid_card_info, get_date, get_last_executed_operations


def test_get_date():
    assert get_date('2001-06-23T00:00:27.000000') == '23.06.2001'
    assert get_date('7777-12-31T01:00:29.675683') == '31.12.7777'
    assert get_date('2024-05-24T16:41:00.675683') == '24.05.2024'


def test_get_valid_card_info():
    assert get_valid_card_info('Visa Classic 2747493856472064') == 'Visa Classic 2747 49** **** 2064'
    assert get_valid_card_info('Счет 67483906574839265789') == 'Счет **5789'
    assert get_valid_card_info('Счет 84638965374503265647') == 'Счет **5647'
    assert get_valid_card_info('Master Card 4856397584036274') == 'Master Card 4856 39** **** 6274'


def test_operations_reader():
    assert operations_reader()[0]['id'] == 441945886
    assert operations_reader()[1]['date'] == '2019-07-03T18:35:29.512364'
    assert operations_reader()[2]['state'] == 'EXECUTED'


def test_get_last_executed_operations():
    assert get_last_executed_operations(operations_reader())[0]['id'] == 863064926
    assert get_last_executed_operations(operations_reader())[4]['description'] == 'Открытие вклада'
    assert get_last_executed_operations(operations_reader())[2]['date']  == '2019-11-19T09:22:25.899614'


