from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card
from src.widget import get_date

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Счет 25090112312345644545"))
print(get_mask_account(23030012312345645601))
print(get_mask_account(25090112312345645601))
print(get_mask_card_number(2303200025092001))
print(get_mask_card_number(2509200123032000))
