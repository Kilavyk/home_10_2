
def filter_by_state(transactions: list, state="EXECUTED") -> list:
    """Фильтрует список словарей по значению ключа 'state'"""
    new_list = []
    for transaction in transactions:
        if transaction.get("state") == state:
            new_list.append(transaction)
    return new_list



def sort_by_date(info: list, sort_order=True) -> list:
    """Сортирует список словарей по дате операции"""
    return sorted(info, key=lambda x: x["date"], reverse=sort_order)


