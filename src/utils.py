import json
import os
import requests
from dotenv import load_dotenv
import logging

load_dotenv()  # Загружаем переменные окружения из .env
API_KEY = os.getenv("EXCHANGE_API_KEY")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def load_transactions(bar: str = None) -> list[dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(bar, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info(data)
            return data
    except FileNotFoundError:
        logging.error("Файл не найден")
        return []
    except Exception:
        logging.error("Непредвиденная ошибка")
        return []


def convert_transaction_to_rub(transaction: dict) -> float:
    """
    DOCSTRING!
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        logging.info("Валюта ОК")
        return float(amount)
    else:
        headers = {"apikey": API_KEY}
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["rates"]["RUB"]
            amount_in_rub = amount * exchange_rate
            logging.info("Валюта ОКK")
            return float(amount_in_rub)
        else:
            logging.error("НЕ ОКК")
            raise ValueError("При запросе произошла ошибка")
