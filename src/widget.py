from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция маскирующая счет или номер карты с названием"""
    number, *name = reversed(info.split(" "))
    if name == [""] or name == [" "] or len(number) < 16:
        return "Неверные данные"
    elif name == ["Счет"]:
        return f"{' '.join(name)} {get_mask_account(number)}"
    else:
        return f"{' '.join(name)} {get_mask_card_number(number)}"


def get_date(date_time: str) -> str:
    """Фунция возвращает день, месяц, год"""
    date_time = date_time.split("T")
    year, month, day = date_time[0].split("-")
    return f"{day}.{month}.{year}"


# print(get_date("2024-03-11T02:26:18.671407"))
