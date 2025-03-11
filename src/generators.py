from typing import List, Dict


def filter_by_currency(transaction, name="USD"):
    return (i for i in transaction if i["operationAmount"]["currency"]["name"] == name)


def transaction_descriptions(transactions: List[Dict]):
    if not transactions:
        raise ValueError("Список транзакций пуст")
    if "description" not in ["description" for x in transactions if "description" in x]:
        raise ValueError("Описание транзакции отсутствует")
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        formatted_number = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
        yield formatted_number
