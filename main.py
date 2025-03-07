from src.file_reader import read_file_scv, read_file_xlsx
from src.processing import filter_by_state
from src.utils import outputting_transactions_from_file


def selecting_processing_file():
    """ Выбираем с каким файлом будем работать"""
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
        print("Некорректно указан пункт меню")
        selecting_processing_file()


def sending_file_for_filter(file):
    print("\nВведите статус, по которому необходимо выполнить фильтрацию."
          "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    state = input("Введите статус: ").upper()

    if state in ["EXECUTED", "CANCELED", "PENDING"]:
        return filter_by_state(file, state)
    else:
        print(f"\nСтатус операции {state} недоступен.")
        sending_file_for_filter(file)



if __name__ == "__main__":
    # Начало работы, приветствие
    print("Привет! \nДобро пожаловать в программу работы с банковскими транзакциями.")

    file = selecting_processing_file() # В переменной список транзакций из файла
    # print(selecting_processing_file())

    sending_file_for_filter(file) # Выполняем фильтрацию
    # print(sending_file_for_filtering(file))

