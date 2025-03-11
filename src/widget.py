from src.masks import get_mask_card_number
from src.masks import get_mask_account
import datetime

sam0 = "Счет"


def mask_account_card(name_card: str | int) -> str:
    sam1 = ""
    sam2 = ""
    if "Счет" in name_card:
        for ter in name_card:
            if ter.isalpha():
                sam1 += ter
            if ter.isdigit():
                sam2 += ter
        return f"{sam1} {get_mask_account(sam2)}"
    else:
        for ter in name_card:
            if ter.isalpha():
                sam1 += ter
            if ter.isdigit():
                sam2 += ter
        return f"{sam1} {get_mask_card_number(sam2)}"


def get_date(sam3):
    date_format = datetime.datetime.strptime(sam3, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
