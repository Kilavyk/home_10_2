import csv
import os
import pandas as pd


def read_file_scv(input_file):
    """Выводит транзакции из файла .csv в виде списка словарей"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data", input_file)
    with open(data_file, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)


def read_file_xlsx(input_file):
    """Выводит транзакции из файла .xlsx в виде словарей"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data", input_file)
    df = pd.read_excel(data_file)
    reader = df.to_dict(orient="records")
    return reader


# if __name__ == '__main__':
#    print(read_file_scv("transactions.csv"))
#    print(read_file_xlsx("transactions_excel.xlsx"))

