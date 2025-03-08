from src.file_reader import read_file_scv, read_file_xlsx
from src.generators import filter_by_currency
from src.operations_filter import filter_transactions_by_description, search_description
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
        return outputting_transactions_from_file("operations.json") # Открытие файла JSON, модуль utils.py
    elif menu_item == "2":
        print("Для обработки выбран CSV-файл")
        return read_file_scv("transactions.csv") # Открытие файла CSV, модуль file_reader.py
    elif menu_item == "3":
        print("Для обработки выбран XLSX-файл")
        return read_file_xlsx("transactions_excel.xlsx") # Открытие файла XLSX, модуль file_reader.py
    else:
        print("Некорректно указан пункт меню")
        selecting_processing_file() # Запускаем функцию заново


def sending_file_for_filter(file):
    print("\nВведите статус, по которому необходимо выполнить фильтрацию."
          "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    state = input("Введите статус: ")

    if state.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
        return filter_by_state(file, state) # Модуль processing.py
    else:
        print(f"\nСтатус операции {state} недоступен.")
        sending_file_for_filter(file) # Запускаем функцию заново


def sorting_transactions(file):
    answer = input("\nОтсортировать операции по дате? Да/Нет\n")
    if answer.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sorting_order = input("Введите 'по возрастанию' или 'по убыванию'\n")
        if sorting_order.lower() == "по возрастанию":
            return sort_by_date(file, sort_order = False) # Сортировка по убыванию, модуль processing.py
        elif sorting_order.lower() == "по убыванию":
            return sort_by_date(file, sort_order = True) # Сортировка по возрастанию, модуль processing.py
        else: print(f"Введено некорректное значение: {sorting_order}")
        sorting_transactions(file) # Запускаем функцию заново
    elif answer.lower() == "нет":
        return file # Возвращает исходный файл
    else:
        print(f"Введено некорректное значение: {answer}")
        return sorting_transactions(file) # Запускаем функцию заново


def show_rub_transactions(file):
    answer = input("\nВыводить только рублевые транзакции? Да/Нет\n")
    if answer.lower() == "да":
        return filter_by_currency(file, cur="RUB") # Модуль generators.py
    elif answer.lower() == "нет":
        return file # Возвращает исходный файл
    else:
        print(f"Введено некорректное значение: {answer}")
        return show_rub_transactions(file) # Запускаем функцию заново


def filter_by_word(file):
    answer = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if answer.lower() == "да":
        search_string = input("Варианты фильтрации:\nПеревод организации \nПеревод с карты на карту"
                              "\nПеревод со счета на счет \nОткрытие вклада \nПеревод с карты на счет\n")
        return filter_transactions_by_description(file, search_string) # Модуль operations_file.py
    elif answer.lower() == "нет":
        return file # Возвращает исходный файл
    else:
        print(f"Введено некорректное значение: {answer}")
        return filter_by_word(file) # Запускаем функцию заново



if __name__ == "__main__":
    # Начало работы, приветствие
    print("Привет! \nДобро пожаловать в программу работы с банковскими транзакциями.")

    file = selecting_processing_file() # В переменной список транзакций из файла
    # print(file)

    file = sending_file_for_filter(file) # Выполняем фильтрацию
    print(file)

    file = sorting_transactions(file) # Сортировка по дате и в каком порядке
    print(file)

    file = show_rub_transactions(file) # Выводим только рублёвые операции или все
    print(file)

    file = filter_by_word(file) # Сортируем по ключевому слову
    print(file)
