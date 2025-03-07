from src.file_reader import read_file_scv, read_file_xlsx
from src.utils import outputting_transactions_from_file


def selecting_processing_file():
    menu = ("Выберите необходимый пункт меню:"
            "\n 1 - Получить информацию о транзакциях из JSON-файла"
            "\n 2 - Получить информацию о транзакциях из CSV-файла"
            "\n 3 - Получить информацию о транзакциях из XLSX-файла")
    print(menu)
    menu_item = (input())
    if menu_item == "1":
        print("Для обработки выбран JSON-файл")
        return outputting_transactions_from_file("operations.json") # Открытие файла JSON
    elif menu_item == "2":
        print("Для обработки выбран CSV-файл")
        return read_file_scv("transactions.csv") # Открытие файла CSV
    elif menu_item == "3":
        print("Для обработки выбран XLSX-файл")
        return read_file_xlsx("transactions_excel.xlsx") # Открытие файлаXLSX
    else:
        print("")
        selecting_processing_file()


if __name__ == "__main__":
    print("Привет! \nДобро пожаловать в программу работы с банковскими транзакциями.")
    # print(selecting_processing_file())
    selecting_processing_file()
    print("\nВведите статус, по которому необходимо выполнить фильтрацию." 
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")