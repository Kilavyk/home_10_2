import json
import os

def outputting_transactions_from_file(input_file="None") -> list:
    """Фильтрует транзакции по валюте и сохраняет результат в новый файл."""
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(current_file))
    data_file = os.path.join(project_root, "data", input_file)
    try:
        with open(data_file, "r", encoding="utf-8") as file:
           data = json.load(file)
    except:
        data = []
    return data




if __name__ == '__main__':
    input_file = 'operations.json'
    transactions = outputting_transactions_from_file(input_file)
    print(transactions)

