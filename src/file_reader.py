import csv
import os
import pandas as pd


def read_file_scv():
    """Выводит транзакции из файла .csv"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data/transactions.csv")
    with open(data_file) as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)


def read_file_xlsx():
    """Выводит транзакции из файла .xlsx"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data/transactions_excel.xlsx")
    reader = pd.read_excel(data_file)
    return reader


if __name__ == '__main__':
   read_file_scv()
   print(read_file_xlsx())

