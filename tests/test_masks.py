from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('1234 5678 9012 3456') == '1234 56** **** 3456'
    assert get_mask_card_number('7 0 007 9 22 89 606 361') == '7000 79** **** 6361'
    assert get_mask_card_number(' ') == 'Неверный номер карты'
    assert get_mask_card_number('abcd') == 'Неверный номер карты'


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('73654108430135874305123') == 'Неверный номер счета'
    assert get_mask_account('73654108') == 'Неверный номер счета'
    assert get_mask_account('7365 410 843 013 587 43 05') == '**4305'
