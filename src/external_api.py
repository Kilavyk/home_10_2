import json
import os
from typing import Union, List, Dict, Any

import requests
from dotenv import load_dotenv

from src.utils import outputting_transactions_from_file

load_dotenv(".env")


def currency_converter(cur_input: str, cer_output: str, value: float) -> float:
    """Функция конвертирует валюту в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={cer_output}&from={cur_input}&amount={value}"
    payload = {}
    headers = {"apikey": os.getenv("API_KEY")}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.text
    value = json.loads(result)["result"]
    return value


def return_amount_from_json(file: List[Dict[str, Any]]) -> Union[str, None]:
    """Функция принимает файл JSON и возвращает из файла значение транзакций в рублях"""
    try:
        for item in file:
            code = item.get("operationAmount", {}).get("currency", {}).get("code")
            amount = float(item["operationAmount"]["amount"])
            if code != "RUB":
                print(f"{amount} {code} = {currency_converter(code, "RUB", amount)} RUB")
            else:
                print(f"{amount} {code}")
    except (Exception) as e:
        print(f"Ошибка данных {e}")
    return


# if __name__ == '__main__':
#     converter = currency_converter("USD", "RUB", 100)
#     print(converter)
#     return_amount_from_json(outputting_transactions_from_file('operations.json'))
