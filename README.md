# Описание проекта

Этот проект предоставляет набор функций для работы с банковскими транзакциями, включая фильтрацию, сортировку, маскировку данных и генерацию номеров карт. В проекте также реализованы тесты для проверки корректности работы функций.

---

## Структура проекта

Проект состоит из нескольких модулей, каждый из которых отвечает за определённый функционал:

1. **`generators.py`** — содержит функции для работы с транзакциями и генерации номеров карт.
2. **`masks.py`** — предоставляет функции для маскировки номеров карт и счетов.
3. **`processing.py`** — содержит функции для фильтрации и сортировки транзакций.
4. **`widget.py`** — предоставляет функции для маскировки данных и работы с датами.

---

## Основные функции

### 1. Маскировка номеров карт
Функция `get_mask_card_number` маскирует номер карты, оставляя видимыми 
первые 6 и последние 4 цифры.

**Пример кода**
```
  def get_mask_card_number(card_number: str) -> str:
      """Маскирует цифры и разбивает на блоки номер карты"""
      card_number = card_number.replace(" ", "")
      if len(card_number) != 16:
          return "Неверный номер карты"
      mask_number = card_number[0:6] + "******" + card_number[-4:]
      group = mask_number[0:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:16]
      return group
```

### 2. Маскировка номеров счетов
Функция `get_mask_account` маскирует номер счёта, оставляя видимыми 
последние 4 цифры.

**Пример кода**
```
  def get_mask_account(account_number: str) -> str:
      """Маскирует номер счёта"""
      account_number = account_number.replace(" ", "")
      if len(account_number) != 20:
          return "Неверный номер счета"
      return "**" + account_number[-4:]
```


### 3. Маскировка данных
Функция `get_date` извлекает дату из строки и возвращает её в формате дд.мм.гггг.

**Пример кода**
```
  def get_date(date_time: str) -> str:
      """Функция возвращает день, месяц, год"""
      find_year = date_time.find("202")
      year = date_time[find_year:find_year + 4]
      month = date_time[find_year + 5:find_year + 7]
      day = date_time[find_year + 8:find_year + 10]
      if (
          year.isdigit()
          and month.isdigit()
          and day.isdigit()
          and int(year) > 2007
          and int(month) < 13
          and int(day) < 32
      ):
          return f"{day}.{month}.{year}"
      return "Некорректная дата"
```

### 4. Фильтрация и сортировка транзакций
Функция `filter_by_state` фильтрует транзакции по статусу (например, "EXECUTED").

**Пример кода**
```
  def filter_by_state(transactions: list, state: str ="EXECUTED") -> list:
      """Фильтрует список словарей по значению ключа 'state'"""
      new_list = []
      for transaction in transactions:
          if transaction.get("state") == state:
              new_list.append(transaction)
      return new_list
```

Функция `sort_by_date` сортирует транзакции по дате.

**Пример кода**
```
  def sort_by_date(info: list, sort_order: bool =True) -> list:
      """Сортирует список словарей по дате операции"""
      return sorted(info, key=lambda x: x["date"], reverse=sort_order)
```

### 5. Фильтрация транзакций по валюте
Функция `filter_by_currency` фильтрует список
транзакций по указанной валюте

**Пример кода:**
```
  def filter_by_currency(items: list, cur: str):
      """ Фильтрует транзакции по валюте 'RUB' """
      for item in items:
          if ("operationAmount" in item
                  and "currency" in item["operationAmount"]
                  and "code" in item["operationAmount"]["currency"]):
              if cur == item["operationAmount"]["currency"]["code"]:
                  yield item
  
  usd_transactions = filter_by_currency(transactions, "USD")
  for operation in range(3):
      print(next(usd_transactions))
```

### 6. Получение описаний транзакций
Функция `transaction_descriptions` возвращает описания пяти транзакций из списка.

**Пример кода:**
```
  def transaction_descriptions(items: list[dict[str, object]]):
      """ Возвращает описание транзакции """
      for item in items:
          yield item["description"]
  
  
  descriptions = transaction_descriptions(transactions)
  for operation in range(5):
      print(next(descriptions))
```

### 7. Генерация номеров банковских карт 
Функция `card_number_generator` генерирует номера банковских карт 
в формате XXXX XXXX XXXX XXXX.

**Пример кода:**
```
  def card_number_generator(start: int, stop: int):
      """ Генератор, выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ """
      if start > stop:
          raise ValueError("значение start должно быть меньше или равно значению stop")
      for number in range(start, stop + 1):
          number_card = str(number).zfill(16)
          formatted_card_number = (number_card[0:4]
                                   + " "
                                   + number_card[4:8]
                                   + " "
                                   + number_card[8:12]
                                   + " "
                                   + number_card[12:16])
          yield formatted_card_number
  
  
  for card_number in card_number_generator(100, 999):
      print(card_number)
```




---

## Добавленные тесты
В проект были добавлены тесты для проверки корректности работы функций. 
### Примеры тестов
#### Для `get_mask_card_number`
```
  def test_get_mask_card_number():
      assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
      assert get_mask_card_number('1234 5678 9012 3456') == '1234 56** **** 3456'
      assert get_mask_card_number('7 0 007 9 22 89 606 361') == '7000 79** **** 6361'
      assert get_mask_card_number(' ') == 'Неверный номер карты'
      assert get_mask_card_number('abcd') == 'Неверный номер карты'
```
#### Для `get_mask_account`
```
  def test_get_mask_account():
      assert get_mask_account('73654108430135874305') == '**4305'
      assert get_mask_account('73654108430135874305123') == 'Неверный номер счета'
      assert get_mask_account('73654108') == 'Неверный номер счета'
      assert get_mask_account('7365 410 843 013 587 43 05') == '**4305'
  ```
#### Для `mask_account_card`
```
  @pytest.mark.parametrize('value, expected', [
      ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
      ('Счет 64686473678894779589', 'Счет **9589'),
      ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
      ('Счет 35383033474447895560', 'Счет **5560'),
      ('Visa Classic 6831982476737658', 'Classic Visa 6831 98** **** 7658'),
      ('Visa Platinum 8990922113665229', 'Platinum Visa 8990 92** **** 5229'),
      ('Visa Gold 5999414228426353', 'Gold Visa 5999 41** **** 6353'),
      ('Счет 73654108430135874305', 'Счет **4305'),
      ('', 'Неверные данные'),
      ('Счет 73654108430135874305', 'Счет **4305'),
      ('Счет 73654108430135874305', 'Счет **4305'),
      ('MasterCard 7158300734', 'Неверные данные'),
      ('Visa Platinum 7158300734', 'Неверные данные')
  ])
  def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
```
### Для `get_date`
```
  @pytest.mark.parametrize('data, get_data', [
      ('2024-03-11T02:26:18.671407', '11.03.2024'),
      ('2024-03-11T02:26:', '11.03.2024'),
      ('2024:26:', "Некорректная дата"),
      ('2024-03-11T02:26:18.671407', '11.03.2024'),
      ('2024    6 11 0226:18.671407', "Некорректная дата"),
      ('Т:18.202  03 110226Т:18.671407', "Некорректная дата"),
      ('2024-13-11T02:26:18.671407', "Некорректная дата"),
      ('2024-13-32T02:26:18.671407', "Некорректная дата"),
      ('2:26:18.6714072024-03-71 02:26:18.671407', "Некорректная дата"),
      ('2:26:18.67:26:18.6714072024-03-11 02:26:18.671407', '11.03.2024'),
      ('2:.6714072024-03-11 02:26:18.671407', '11.03.2024'),
  ])
  def test_get_date(data, get_data):
      assert get_date(data) == get_data

```
### Для `filter_by_state`
```
def test_filter_by_state(standart):
    assert filter_by_state(standart) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
### Для `sort_by_date`
```
  def test_sort_by_date(standart):
      assert sort_by_date(standart) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 615064591, 'state': ' ', 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T'},
                                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                        {'id': '', 'state': '', 'date': ''}]
```
### Для `filter_by_currency`
```
def test_filter_by_currency_usd(transac):
    usd_transactions = list(filter_by_currency(transac, "USD"))
    assert len(usd_transactions) == 3

def test_filter_by_currency_rub(transac):
    rub_transactions = list(filter_by_currency(transac, "RUB"))
    assert len(rub_transactions) == 2

def test_filter_by_currency_no_currency(transac):
    no_currency_transactions = list(filter_by_currency(transac, "none"))
    assert len(no_currency_transactions) == 0

def test_filter_by_currency_invalid_structure():
    invalid_transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "operationAmount": {"amount": "100.00"}},
        {"id": 3, "state": "EXECUTED", "operationAmount": {"currency": {"name": "USD"}}},
    ]
    filtered_transactions = list(filter_by_currency(invalid_transactions, "RUB"))
    assert len(filtered_transactions) == 0

def test_filter_by_currency_empty_list():
    empty_transactions = []
    filtered_transactions = list(filter_by_currency(empty_transactions, "RUB"))
    assert len(filtered_transactions) == 0
```
### Для `transaction_descriptions`
```
def test_transaction_descriptions_all(transac):
    descriptions = list(transaction_descriptions(transac))
    assert len(descriptions) == 7
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод без указания валюты"
    ]

def test_transaction_descriptions_first_five(transac):
    descriptions = transaction_descriptions(transac)
    first_five = [next(descriptions) for i in range(5)]
    assert first_five == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

def test_transaction_descriptions_empty_list():
    empty_transactions = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert len(descriptions) == 0

```
### Для `card_number_generator`
```
@pytest.mark.parametrize(
    "start, stop, results",
    [
        (1, 5, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"
        ]),
        (9999999999999990, 9999999999999995, [
            "9999 9999 9999 9990",
            "9999 9999 9999 9991",
            "9999 9999 9999 9992",
            "9999 9999 9999 9993",
            "9999 9999 9999 9994",
            "9999 9999 9999 9995"
        ]),
        (1234567890123456, 1234567890123456, [
            "1234 5678 9012 3456"
        ]),
        (0, 2, [
            "0000 0000 0000 0000",
            "0000 0000 0000 0001",
            "0000 0000 0000 0002"
        ]),
    ]
)
def test_card_number_generator(start, stop, results):
    generator = card_number_generator(start, stop)
    for expected, actual in zip(results, generator):
        assert actual == expected
```



### Запуск тестов
Для запуска тестов используйте команду:
```python
    pytest tests/
```

## Установка и использование
1. Склонируйте репозиторий:

```git clone https://github.com/Kilavyk/home_10_2.git```

2. Перейдите в ветку с домашней работой:

```git checkout develop```

3. Запустите код в вашей среде разработки или через командную строку.

## Ссылка на GitHub
Проект доступен на GitHub: [Kilavyk/home_10_2.](https://github.com/Kilavyk/home_10_2/)

## Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной:

GitHub: [Kilavyk](https://github.com/Kilavyk)
