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
    """Функция возвращает день, месяц, год"""
    try:
        date_part = date_time.split('T')[0]
        year, month, day = date_part.split('-')

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Некорректная дата"

        return f"{day}.{month}.{year}"
    except (IndexError, ValueError):
        return "Некорректная дата"
