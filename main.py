from src.file_reader import read_file_scv, read_file_xlsx
from src.generators import filter_by_currency
from src.operations_filter import filter_transactions_by_description, count_transactions_by_category
from src.processing import filter_by_state, sort_by_date
from src.utils import outputting_transactions_from_file
from src.widget import get_date, mask_account_card


def main():
    """ Запускаем основную логику проекта """
    print("Привет! \nДобро пожаловать в программу работы с банковскими транзакциями.")
    return selecting_processing_file()


def selecting_processing_file():
    """ Выбираем с каким файлом будем работать"""
    while True:
        menu = ("Выберите необходимый пункт меню:"
                "\n 1 - Получить информацию о транзакциях из JSON-файла"
                "\n 2 - Получить информацию о транзакциях из CSV-файла"
                "\n 3 - Получить информацию о транзакциях из XLSX-файла")
        print(menu)
        menu_item = input()

        if menu_item == "1":
            print("\nДля обработки выбран JSON-файл")
            return outputting_transactions_from_file("operations.json") # Открытие файла JSON, модуль utils.py
        elif menu_item == "2":
            print("\nДля обработки выбран CSV-файл")
            return read_file_scv("transactions.csv") # Открытие файла CSV, модуль file_reader.py
        elif menu_item == "3":
            print("\nДля обработки выбран XLSX-файл")
            return read_file_xlsx("transactions_excel.xlsx") # Открытие файла XLSX, модуль file_reader.py
        else:
            print("Некорректно указан пункт меню")


def sending_file_for_filter(file: list) -> list:
    """ Отправляем файл на сортировку по статусу """
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию."
              "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Введите статус: ")

        if state.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            return filter_by_state(file, state)  # Модуль processing.py
        else:
            print(f"\nСтатус операции {state} недоступен.")


def sorting_transactions(file: list) -> list:
    """ Отправляем файл на сортировку по дате """
    while True:
        answer = input("\nОтсортировать операции по дате? Да/Нет\n")

        if answer.lower() == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            sorting_order = input("Введите 'по возрастанию' или 'по убыванию'\n")
            if sorting_order.lower() == "по возрастанию":
                return sort_by_date(file, sort_order=False)  # Сортировка по убыванию, модуль processing.py
            elif sorting_order.lower() == "по убыванию":
                return sort_by_date(file, sort_order=True)  # Сортировка по возрастанию, модуль processing.py
            else:
                print(f"Введено некорректное значение: {sorting_order}")
        elif answer.lower() == "нет":
            return file  # Возвращает исходный файл
        else:
            print(f"Введено некорректное значение: {answer}")


def show_rub_transactions(file: list) -> list:
    """ Отправляем файл на сортировку рублёвых операций"""
    while True:
        answer = input("\nВыводить только рублевые транзакции? Да/Нет\n")
        if answer.lower() == "да":
            return filter_by_currency(file, cur="RUB")  # Модуль generators.py
        elif answer.lower() == "нет":
            return file  # Возвращает исходный файл
        else:
            print(f"Введено некорректное значение: {answer}")


def filter_by_word_and_count(file: list) -> tuple[list, dict]:
    """ Отправляем файл на сортировку по определенному слову"""
    while True:
        answer = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if answer.lower() == "да":
            search_string = input("Варианты фильтрации:\nПеревод организации \nПеревод с карты на карту"
                                 "\nПеревод со счета на счет \nОткрытие вклада \nПеревод с карты на счет\n")
            filter = filter_transactions_by_description(file, search_string)  # Модуль operations_file.py
            count = count_transactions_by_category(filter, search_string)  # Модуль operations_file.py
            return filter, count
        elif answer.lower() == "нет":
            count = count_transactions_by_category(file)  # Модуль operations_file.py
            return file, count  # Возвращает исходный файл
        else:
            print(f"Введено некорректное значение: {answer}")


def final_list(file: list, count: dict):
    """ Распечатываем отфильтрованный список"""
    if not file:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("\nРаспечатываю итоговый список транзакций...")
        total_sum = sum(count.values())
        print(f"Всего банковских операций в выборке: {total_sum}")

        for item in file:
            if not item:
                continue
            else:
                date_str = get_date(item["date"]) # Модуль widget.py

                if "to" in item:
                    to_ = mask_account_card(item["to"])
                else:
                    to_ = ""

                if item.get("from") and item["from"] != "nan":
                    from_ = mask_account_card(item["from"]) + " -> "
                else:
                    from_ = ""

                print(f"\n{date_str} {item["description"]}")
                print(f"{from_}{to_}")
                print(f"Сумма: {item["amount"]} {item["currency_code"]}")


if __name__ == "__main__":
    # Начало работы, приветствие
    file = main() # В переменной список транзакций из файла
    # print(file)

    file = sending_file_for_filter(file) # Выполняем фильтрацию
    # print(file)

    file = sorting_transactions(file) # Сортировка по дате и в каком порядке
    # print(file)

    file = show_rub_transactions(file) # Выводим только рублёвые операции или все
    # print(file)

    file, count = filter_by_word_and_count(file) # Сортируем по ключевому слову
    # print(file, count)

    final_list(file, count) # Выводим итоговый список

