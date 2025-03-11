from src.masks import get_mask_card_number
from src.masks import get_mask_account

yfpdfybt = "Visa Platinum", "Maestro", "MasterCard", "Visa Classic", "Visa Gold"


def mask_account_card(name_card: str | int) -> str:
    text_card = ""
    nomer_card = ""
    if name_card.startswith(yfpdfybt):
        for ter in name_card:
            if ter.isalpha():
                text_card += ter
            if ter.isdigit():
                nomer_card += ter
        return f"{text_card} {get_mask_card_number(nomer_card)} "
    elif name_card.startswith("Счет"):
        for ter in name_card:
            if ter.isalpha():
                text_card += ter
            if ter.isdigit():
                nomer_card += ter
        return f"{text_card} {get_mask_account(nomer_card)} "
    else:
        return "Не правильно введены значения"
