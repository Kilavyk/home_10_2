import logging
import os

# Получаем корневую директорию проекта
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_dir = os.path.join(project_root, "logs")
log_file = os.path.join(logs_dir, "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует цифры и разбивает на блоки номер карты"""
    logger.info(f"Функция приняла значение - {card_number}")
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        logger.error("Неверный номер карты")
        return "Неверный номер карты"
    mask_number = card_number[0:6] + "******" + card_number[-4:]
    logger.info(f"Замаскировали 6 цифр - {mask_number}")
    group = mask_number[0:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:16]
    logger.info(f"Разделили 16 цифр на группы по 4 цифры и вернули значение - {group}")
    return group


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта"""
    logger.info(f"Функция приняла значение - {account_number}")
    account_number = account_number.replace(" ", "")
    if len(account_number) != 20:
        logger.error("Неверный номер счета")
        return "Неверный номер счета"
    logger.info(f"Вернули замаскированный номер счёта - {'**' + account_number[-4:]}")
    return "**" + account_number[-4:]


# if __name__ == '__main__':
#     print(get_mask_account('73654108430135874305'))
#     print(get_mask_card_number('7 0 007 9 22 89 606 361'))
