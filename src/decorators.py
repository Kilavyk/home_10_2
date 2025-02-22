from datetime import datetime
from functools import wraps


def log(filename=None):
    """Формирование текст об успешном выполнении функции и возникшие ошибки"""

    def decorator(func):
        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def wrapper(*args, **kwargs):
            # Получаем текущую дату и время
            data_now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_messeng = f"{data_now} --> {func.__name__} --> OK"
                write_log(log_messeng, filename)
                return result
            except Exception as error:
                error_masseng = f"{data_now} --> error: {type(error).__name__}: {error} --> {args}, {kwargs}"
                write_log(error_masseng, filename)
                raise error
        return wrapper
    return decorator


def write_log(messeng, filename):
    """Записывает сообщение в файл или выводит его в консоль"""
    if filename:
        with open(filename, "a", encoding="utf-8",) as file:
            file.write(f"{messeng}\n")
    else:
        print(messeng)


def check_that_agr_is(predicate, error_message):
    """Декоратор для проверки аргументов функции с помощью предиката"""

    def wrapper(function):
        @wraps(function)  # Сохраняем метаданные оригинальной функции
        def inner(a, b):
            if not predicate(a, b):
                raise ValueError(error_message)
            return function(a, b)
        return inner
    return wrapper


def predicate_is_int(*values):
    """Проверяет, являются ли оба переданных значения целыми числами"""
    return all(isinstance(value, int) for value in values)


@log(filename="log.txt")
@check_that_agr_is(predicate_is_int, "Значения должны быть числом")
def my_function(x: int, y: int) -> int:
    """Возвращает сумму двух чисел"""
    return x + y


if __name__ == "__main__":
    my_function(1, 2)
    my_function(1, "2")
    my_function(4, 2)
