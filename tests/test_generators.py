import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_usd(transac):
    usd_transactions = list(filter_by_currency(transac, "USD"))
    assert len(usd_transactions) == 0


def test_filter_by_currency_rub(transac):
    rub_transactions = list(filter_by_currency(transac, "RUB"))
    assert len(rub_transactions) == 0


def test_filter_by_currency_no_currency(transac):
    no_currency_transactions = list(filter_by_currency(transac, "none"))
    assert len(no_currency_transactions) == 0


def test_filter_by_currency_invalid_structure():
    invalid_transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "operationAmount": {"amount": "100.00"}},
        {"id": 3, "state": "EXECUTED", "operationAmount": {"currency": {"name": "USD"}}},
    ]
    filtered_transactions = list(filter_by_currency(invalid_transactions, "RUB"))
    assert len(filtered_transactions) == 0


def test_filter_by_currency_empty_list():
    empty_transactions = []
    filtered_transactions = list(filter_by_currency(empty_transactions, "RUB"))
    assert len(filtered_transactions) == 0


def test_transaction_descriptions_all(transac):
    descriptions = list(transaction_descriptions(transac))
    assert len(descriptions) == 7
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод без указания валюты"
    ]

def test_transaction_descriptions_empty_list():
    empty_transactions = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert len(descriptions) == 0


def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError, match="значение start должно быть меньше или равно значению stop"):
        next(card_number_generator(10, 5))


@pytest.mark.parametrize(
    "start, stop, results",
    [
        (1, 5, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"
        ]),
        (9999999999999990, 9999999999999995, [
            "9999 9999 9999 9990",
            "9999 9999 9999 9991",
            "9999 9999 9999 9992",
            "9999 9999 9999 9993",
            "9999 9999 9999 9994",
            "9999 9999 9999 9995"
        ]),
        (1234567890123456, 1234567890123456, [
            "1234 5678 9012 3456"
        ]),
        (0, 2, [
            "0000 0000 0000 0000",
            "0000 0000 0000 0001",
            "0000 0000 0000 0002"
        ]),
    ]
)
def test_card_number_generator(start, stop, results):
    generator = card_number_generator(start, stop)
    for expected, actual in zip(results, generator):
        assert actual == expected