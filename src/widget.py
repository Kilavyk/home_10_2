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
    find_year = date_time.find("202")
    year = (date_time[find_year:find_year+4])
    month = (date_time[find_year+5:find_year + 7])
    day = (date_time[find_year+8:find_year + 10])
    if year.isdigit() == True and month.isdigit() == True and day.isdigit() == True and int(year) > 2007 and int(month) < 13 and int(day) < 32:
        return f"{day}.{month}.{year}"
    return "Некорректная дата"
