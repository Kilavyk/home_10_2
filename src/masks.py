def get_mask_card_number(card_number: str) -> str:
    """Маскирует цифры и разбивает на блоки номер карты"""
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        return "Неверный номер карты"
    mask_number = card_number[0:6] + "******" + card_number[-4:]
    group = mask_number[0:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:16]
    return group


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта"""
    account_number = account_number.replace(" ", "")
    if len(account_number) != 20:
        return "Неверный номер счета"
    return "**" + account_number[-4:]


# print(get_mask_card_number("7 0 007 9 22 89 606 361"))
# print(get_mask_account("73654108430135874305"))
