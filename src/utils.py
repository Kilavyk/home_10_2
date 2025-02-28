import json
import os


def outputting_transactions_from_file(input_file=None) -> list:
    """Выводит транзакции из файла если найден файл с транзакциями."""
    try:
        current_file = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(current_file))
        data_file = os.path.join(project_root, "data", input_file)

        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return []
    except:
        return []


# if __name__ == '__main__':
#     input_file = 'operations.json'
#     transactions = outputting_transactions_from_file(input_file)
#     print(transactions)
