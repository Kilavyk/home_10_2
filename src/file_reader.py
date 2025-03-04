import csv
import os


def read_file_scv():
    """Выводит транзакции из файла если найден файл с транзакциями."""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data/transactions.csv")
    with open(data_file) as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)


if __name__ == '__main__':
   print(read_file_scv())

