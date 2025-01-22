def get_mask_card_number(card_number: int) -> str:
    """Маскирует цифры и разбивает на блоки номер карты"""
    card_number_str = str(card_number)
    mask_number = card_number_str[0:6] + "******" + card_number_str[-4:]
    group_cn_str = mask_number[0:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:16]
    return group_cn_str


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счёта"""
    account_number_str = str(account_number)
    mask_account_number_str = "**" + account_number_str[-4:]
    return mask_account_number_str


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
