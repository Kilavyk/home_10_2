import pytest
from unittest.mock import patch, Mock
import json
import requests

from src.external_api import currency_converter, return_amount_from_json


def test_currency_converter():
    with patch("requests.request") as mock_request:
        mock_response = Mock()
        mock_response.text = json.dumps({"result": 7500.0})
        mock_request.return_value = mock_response

        result = currency_converter("USD", "RUB", 100.0)
        assert result == 7500.0

def test_currency_converter_error():
    with patch("requests.request") as mock_request:
        mock_request.side_effect = requests.exceptions.RequestException("Ошибка сети")

        with pytest.raises(requests.exceptions.RequestException):
            currency_converter("USD", "RUB", 100.0)

def test_sum_amount_with_conversion(rub_transaction, usd_transaction):
    with patch("src.external_api.currency_converter", return_value=616602.75) as mock_converter:
        return_amount_from_json([usd_transaction])
        mock_converter.assert_called_once_with("USD", "RUB", 8221.37)

def test_sum_amount_without_conversion(rub_transaction):
    with patch("src.external_api.currency_converter") as mock_converter:
        return_amount_from_json([rub_transaction])
        mock_converter.assert_not_called()

def test_sum_amount_invalid_data(invalid_transaction):
    with patch("builtins.print") as mock_print:
        return_amount_from_json([invalid_transaction])
        mock_print.assert_called_with("Ошибка данных")