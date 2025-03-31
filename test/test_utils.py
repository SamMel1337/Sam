import pytest
from unittest.mock import mock_open, patch
import json
import logging
from src.utils import load_transactions
ex = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }

# Тест для успешной загрузки данных
def test_load_transactions_success():
    test_data = {"transactions": [{"id": 1, "amount": 100}]}
    json_data = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=json_data)) as mock_file:
        result = load_transactions("test.json")

        # Проверяем что файл был открыт
        mock_file.assert_called_once_with("test.json", "r", encoding="utf-8")
        # Проверяем результат
        assert result == test_data

# Тест для случая с пустым путем (bar=None)
def test_load_transactions_empty_path():
    result = load_transactions()
    assert result == []

# Тест для обработки ошибки при чтении файла
def test_load_transactions_file_error():
    with patch("builtins.open", mock_open()) as mock_file:

        result = load_transactions("invalid.json")
        assert result == []

# Тест для кривого JSON
def test_load_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")) as mock_file:
        result = load_transactions("bad.json")
        assert result == []

# Проверка логов
def test_load_transactions_logging(caplog):
    test_data = {"transactions": [{"id": 1, "amount": 100}]}
    json_data = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=json_data)):
        with caplog.at_level(logging.INFO):
            load_transactions("test.json")
            assert "пустой список" not in caplog.text
            assert str(test_data) in caplog.text