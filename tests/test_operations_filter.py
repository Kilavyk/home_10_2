import pytest
from unittest.mock import patch
from src.operations_filter import filter_transactions_by_description, count_transactions_by_category

@pytest.fixture
def transactions():
    return [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Перевод с карты на карту", "amount": 200},
        {"description": "Открытие вклада", "amount": 50},
        {"description": "Перевод с карты на счет", "amount": 300},
    ]

@patch("builtins.open")
def test_filter_transactions(mock_open, transactions):
    mock_file = mock_open(read_data=str(transactions))
    search_string = "Перевод"
    filtered_transactions = filter_transactions_by_description(transactions, search_string)
    assert len(filtered_transactions) == 3
    assert filtered_transactions[0]["description"] == "Перевод организации"


@patch("builtins.open")
def test_count_transactions_by_category(mock_open, transactions):
    categories = "перевод", "вклад"
    expected_result = {
        "Перевод организации": 1,
        "Перевод с карты на карту": 1,
        "Открытие вклада": 1,
        "Перевод с карты на счет": 1
    }
    mock_file = mock_open(read_data=str(transactions))
    result = count_transactions_by_category(transactions, categories)
    assert result == expected_result