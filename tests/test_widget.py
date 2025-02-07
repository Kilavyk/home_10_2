import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize('value, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Classic Visa 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Platinum Visa 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Gold Visa 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('', 'Неверные данные'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('MasterCard 7158300734', 'Неверные данные'),
    ('Visa Platinum 7158300734', 'Неверные данные')

])

def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected