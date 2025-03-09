import json
from unittest.mock import patch, mock_open

from src.utils import outputting_transactions_from_file

@patch("builtins.open", new_callable=mock_open)
def test_outputting_transactions_from_file(mock_open_file):
    mock_data = [{"operationAmount": {"amount": "100", "currency": {"name": "Рубли", "code": "RUB"}}},
                 {"operationAmount": {"amount": "200", "currency": {"name": "Доллары", "code": "USD"}}}]

    mock_open_file.return_value.read.return_value = json.dumps(mock_data)
    expected_result = [{"amount": "100", "currency_name": "Рубли", "currency_code": "RUB"},
                       {"amount": "200", "currency_name": "Доллары", "currency_code": "USD"}]
    result = outputting_transactions_from_file("example.json")
    assert result == expected_result

@patch("builtins.open", new_callable=mock_open)
def test_outputting_transactions_from_file_empty(mock_open_file):
    mock_open_file.return_value.read.return_value = json.dumps([])
    expected_result = []
    result = outputting_transactions_from_file("example.json")
    assert result == expected_result

@patch("builtins.open", new_callable=mock_open)
def test_outputting_transactions_from_file_invalid_data(mock_open_file):
    mock_open_file.return_value.read.return_value = "invalid json"
    expected_result = []
    result = outputting_transactions_from_file("example.json")
    assert result == expected_result
