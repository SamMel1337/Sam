# лицевой счет
def get_mask_account(personal_account: int) -> str:
    """Функция маскировки номера счета"""
    personal_account_str = str(personal_account)
    if len(personal_account_str) == 20:
        return f"** {personal_account_str[-4:]}"
    else:
        return "Неправильный номер"


# лицевой счет
def get_mask_card_number(personal_account2: int) -> str:
    """Функция маскировки номера счета"""
    personal_account2_str = str(personal_account2)
    if len(personal_account2_str) == 16:
        return f" {personal_account2_str[0:4]} {personal_account2_str[5:7]}** **** { personal_account2_str[12:]}"
    else:
        return "Неправильный номер"
