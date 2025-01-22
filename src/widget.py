from src.masks import get_mask_card_number
from src.masks import get_mask_account

def mask_account_card(info: str) -> str:
    """Функция маскирующая счет или номер карты с названием"""
    number, *name = reversed(info.split(" "))
    if len(number) == 16:
        return f"{' '.join(name)} {get_mask_card_number(number)}"
    else:
        return f"{' '.join(name)} {get_mask_account(number)}"


print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_time: str) -> str:
    """Фунция возвращает день, месяц, год"""
    date_time = date_time.split("T")
    year, month, day = date_time[0].split("-")
    return f"{day}.{month}.{year}"

print(get_date("2024-03-11T02:26:18.671407"))