import pytest
from src.decorators import log


@log()
def successful_function(x, y):
    return x + y


@log()
def error_function(x, y):
    return x / y


def test_successful_function(capsys):
    result = successful_function(3, 4)

    # Перехватываем вывод
    captured = capsys.readouterr()

    assert result == 7
    assert "successful_function ok" in captured.out


def test_error_function(capsys):
    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)

    # Перехватываем вывод
    captured = capsys.readouterr()

    assert "error_function error: division by zero. Inputs: (1, 0), {}" in captured.err


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log()
    def test_function(x, y):
        return x + y

    test_function(5, 7)

    # Проверяем содержание файла
    with open(log_file, "r") as f:
        logs = f.read()

    assert "test_function ok" in logs
