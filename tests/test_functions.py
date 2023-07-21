from utils.functions import sign_substitution_from, last_operation_exe, sing_substitution_to

def test_sign_substitution_from():
    assert sign_substitution_from('Visa Gold 1234567890123456') == 'Visa Gold 1234 56** **** 3456'
    assert sign_substitution_from('Visa 1234567890123457') == 'Visa 1234 56** **** 3457'
    assert sign_substitution_from('Счет 12345678901234567890') == 'Счет 1234 56** **** **** 7890'

def test_sing_substitution_to():
    assert sing_substitution_to('Счет 12345678901234567890') == 'Счет **7890'

def test_last_operation_exe():
    assert last_operation_exe([{"state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"}, {"state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}, {"state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572"}, {"state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075"}, {"state": "CANCELED",
    "date": "2019-04-04T23:20:05.206878"}, {"state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404"}, {"state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246"}]) == [{'date': '20190826105058294041', 'state': 'EXECUTED'},
                                                {'date': '20190703183529512364', 'state': 'EXECUTED'},
                                                {'date': '20190323010946296404', 'state': 'EXECUTED'},
                                                {'date': '20181220164326929246', 'state': 'EXECUTED'},
                                                {'date': '20180630020858425572', 'state': 'EXECUTED'}]