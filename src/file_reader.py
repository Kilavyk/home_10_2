import csv
import os
import pandas as pd


def read_file_scv(input_file):
    """Выводит транзакции из файла .csv в виде списка словарей"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data", input_file)
    with open(data_file) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)


def read_file_xlsx(input_file):
    """Выводит транзакции из файла .xlsx в виде словарей"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data", input_file)
    df = pd.read_excel(data_file)
    reader = df.to_dict(orient="records")
    return reader


# if __name__ == '__main__':
#    read_file_scv("transactions.csv")
#    print(read_file_xlsx("transactions_excel.xlsx"))

