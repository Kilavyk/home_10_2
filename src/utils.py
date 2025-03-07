import json
import logging
import os


# Получаем корневую директорию проекта
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_dir = os.path.join(project_root, "logs")
log_file = os.path.join(logs_dir, "utils.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def outputting_transactions_from_file(input_file=None) -> list:
    """Выводит транзакции из файла если найден файл с транзакциями."""
    logger.info("Функция начала работу")
    try:
        logger.info("Построение абсолютного пути к файлу 'operations.json'")
        project_root = os.path.dirname(os.path.dirname(__file__))
        data_file = os.path.join(project_root, "data", input_file)
        logger.info("Чтение файла")
        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            logger.info("Выводим результат")
            return data
        else:
            logger.error("Файл найден, но он пустой или в нём нет списка, вернули пустой список")
            return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Произошла ошибка, вернули пустой список. Файл: {input_file}: {e}")
        return []


# if __name__ == '__main__':
#     input_file = 'operations.json'
#     transactions = outputting_transactions_from_file(input_file)
#     print(transactions)
