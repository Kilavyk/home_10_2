import pytest
from unittest.mock import mock_open, patch
import os
import json
from src.utils import outputting_transactions_from_file  # Импорт функции

# Фикстура для мокирования путей
@pytest.fixture
def mock_paths(mocker):
    # Мокируем os.path.abspath и os.path.dirname
    mocker.patch("os.path.abspath", return_value="/fake/path/to/module.py")
    mocker.patch("os.path.dirname", side_effect=["/fake/path/to", "/fake/path"])

# Тесты
def test_file_exists_and_valid_json_list(mock_paths, mocker):
    mocker.patch("builtins.open", mock_open(read_data=json.dumps([{"id": 1}, {"id": 2}])))

    result = outputting_transactions_from_file("operations.json")
    assert result == [{"id": 1}, {"id": 2}]


def test_file_exists_but_empty(mock_paths, mocker):
    mocker.patch("builtins.open", mock_open(read_data=""))

    result = outputting_transactions_from_file("operations.json")
    assert result == []