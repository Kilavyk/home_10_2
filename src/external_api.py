import json
import os

import requests
from dotenv import load_dotenv

from src.utils import outputting_transactions_from_file

load_dotenv(".env")

def currency_converter(cur_input: str, cer_output: str, value: float) -> float:
    """ Функция конвертирует валюту в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={cer_output}&from={cur_input}&amount={value}"
    payload = {}
    headers= {
      # "apikey": "qj9eHxTwpTwI4inokeaXkyOtBW1pnEg6"
        "apikey": os.getenv("API_KEY")
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.text
    value = json.loads(result)["result"]
    return value






if __name__ == '__main__':
    # result = currency_converter("eur", "rub", 100)
    # print(result)
    # print(outputting_transactions_from_file('operations.json'))
    # print(sum_amount(outputting_transactions_from_file('operations.json')))
    print(sum_amount())

