from unittest.mock import mock_open, patch
import json
import logging
from src.utils import load_transactions


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
        mock_file.side_effect = Exception("File error")

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

    with patch("builtins.open", side_effect=Exception("Error")):
        with caplog.at_level(logging.ERROR):
            load_transactions("error.json")
            assert "пустой список" in caplog.text
