import re
from collections import Counter
from typing import List, Dict

from src.utils import outputting_transactions_from_file


def filter_transactions_by_description(transactions: List, search_string: str) -> List:
    """ Возвращать список словарей, у которых в описании есть строка 'описание' (description) """
    filtered_transactions = []

    for transaction in transactions:
        description = transaction.get("description", "")
        if re.search(search_string, description, re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_transactions_by_category(transactions: List, categories=None) -> Dict:
    """ Считает количество операций для указанной категории """
    descriptions = [transaction.get("description", "") for transaction in transactions]

    # Если категории не переданы
    if not categories:
        category_count = Counter(descriptions)
        return dict(category_count)

    # Фильтруем описания по категориям
    filtered_descriptions = [
        desc for desc in descriptions
        if any(re.search(cat, desc, re.IGNORECASE) for cat in categories)]

    category_count = Counter(filtered_descriptions)
    return dict(category_count)


# if __name__ == "__main__":
#     # Загружаем файла
#     transactions = outputting_transactions_from_file("operations.json")
#
#
#     # Фильтруем транзакций по строке 'описание' (description)
#     # Возможные варианты поиска (Перевод организации, Перевод с карты на карту, Перевод со счета на счет,
#     #                            Открытие вклада, Перевод с карты на счет)
#     filtered = filter_transactions_by_description(transactions, "Открытие вклада")
#     print(filtered)
#     #Высодим список построчно
#     for transaction in filtered:
#         print(transaction)
#
#
#     # Подсчет операций по категориям
#     categories = [
#         "вклад"
#     ]
#     counts = count_transactions_by_category(transactions, categories)
#     print(counts)
#     #Высодим список построчно
#     for category, count in counts.items():
#         print(f"{category}: {count}")
