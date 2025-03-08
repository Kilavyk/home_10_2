from six import print_

from src.file_reader import read_file_scv, read_file_xlsx
from src.processing import filter_by_state, sort_by_date
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


def sorting_transactions(file):
    answer = input("\nОтсортировать операции по дате? Да/Нет").lower()
    if answer == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sorting_order = input("Введите 'по возрастанию' или 'по убыванию'\n").lower()
        if sorting_order == "по возрастанию":
            return sort_by_date(file, sort_order = False) # Сортировка по убыванию
        elif sorting_order == "по убыванию":
            return sort_by_date(file, sort_order = True) # Сортировка по возрастанию
        else: print("Введено некорректное значение")
        sorting_transactions(file)
    elif answer == "нет":
        return file
    else:
        print("Введено некорректное значение")
        return sorting_transactions(file)


if __name__ == "__main__":
    # Начало работы, приветствие
    print("Привет! \nДобро пожаловать в программу работы с банковскими транзакциями.")

    file = selecting_processing_file() # В переменной список транзакций из файла
    # print(file)

    file = sending_file_for_filter(file) # Выполняем фильтрацию
    # print(file)

    file = sorting_transactions(file) # сортировка по дате и в каком порядке
    print(file)
