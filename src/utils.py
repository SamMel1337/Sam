import json
import os
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs.log", encoding="utf-8")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

load_dotenv()  # Загружаем переменные окружения из .env
API_KEY = os.getenv("EXCHANGE_API_KEY")


def load_transactions(bar: str = None) -> list[dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(bar, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(data)
            return data
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except Exception:
        logger.error("Непредвиденная ошибка")
        return []


def convert_transaction_to_rub(transaction: dict) -> float:
    """
    DOCSTRING!
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        logger.info("Валюта ОК")
        return float(amount)
    else:
        headers = {"apikey": API_KEY}
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["rates"]["RUB"]
            amount_in_rub = amount * exchange_rate
            logger.info("Валюта ОКK")
            return float(amount_in_rub)
        else:
            logger.error("НЕ ОКК")
            raise ValueError("При запросе произошла ошибка")
