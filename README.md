# Описание проекта

Этот проект предоставляет набор функций для работы с 
банковскими транзакциями, включая фильтрацию, сортировку, 
маскировку данных и генерацию номеров карт. 
Добавлен декоратор для логирования выполнения функций и проверки аргументов.
Добавлен функционал для чтений файлов json, csv, xlsx, и конвертации валюты 
в рубли по средствам API из выполненных транзакций.
А так же выполнено логирование функций.
В проекте реализованы тесты для проверки корректности работы функций.

---

## Структура проекта

Проект состоит из нескольких модулей, каждый из которых отвечает за определённый функционал:

1. **`generators.py`** — содержит функции для работы с транзакциями и генерации номеров карт.
2. **`masks.py`** — предоставляет функции для маскировки номеров карт и счетов.
3. **`processing.py`** — содержит функции для фильтрации и сортировки транзакций.
4. **`widget.py`** — предоставляет функции для маскировки данных и работы с датами.
5. **`decorators.py`** — декоратор `log` используется для логирования успешного выполнения функции или возникших ошибок. Логи могут записываться в файл или выводиться в консоль.
6. **`utils.py`** — реализована функция для чтений файла формата json
7. **`external_api.py`** — функция конвертирует валюты по средствам API
8. **`file_reader.py`** — содержит функции для чтения файлов csv, xlsx.

## Описание проекта

Проект включает две основные функции:
1. **`filter_by_state`** — фильтрует список транзакций по значению ключа `state`. По умолчанию возвращает только транзакции со статусом `EXECUTED`.
2. **`sort_by_date`** — сортирует список транзакций по дате операции. По умолчанию сортировка выполняется в порядке убывания (от новых к старым).

### Пример кода

```python
def filter_by_state(transactions: list, state='EXECUTED') -> list:
    """ Фильтрует список словарей по значению ключа 'state' """
    new_list = []
    for transaction in transactions:
        if transaction.get('state') == state:
            new_list.append(transaction)
    return new_list


def sort_by_date(info: list, sort_order=True) -> list:
    """Сортирует список словарей по дате операции"""
    return sorted(info, key=lambda x: x['date'], reverse=sort_order)
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
### 8. Логирования функции
Декоратор `log` используется для логирования успешного выполнения функции или возникших ошибок. Логи могут записываться в файл или выводиться в консоль.

**Пример кода:**
```
@log(filename="log.txt")
def my_function(x, y):
    return x + y
```
#### Декоратор `check_that_agr_is`
проверяет аргументы функции с помощью предиката. Если аргументы не удовлетворяют условию, выбрасывается исключение ValueError.

**Пример кода:**
```
@check_that_agr_is(predicate_is_int, "Значения должны быть целыми числами")
def my_function(x, y):
    return x + y
```

#### Функция `predicate_is_int`
проверяет, являются ли все переданные значения целыми числами.

**Пример кода:**
```
def predicate_is_int(*values):
    return all(isinstance(value, int) for value in values)
```

#### Функция `my_function` 
возвращает сумму двух чисел. Она использует декораторы log и check_that_agr_is для логирования и проверки аргументов.

**Пример кода:**
```
@log(filename="log.txt")
@check_that_agr_is(predicate_is_int, "Значения должны быть числом")
def my_function(x: int, y: int) -> int:
    return x + y
```
### 9. Чтение файла json
#### Функция `outputting_transactions_from_file`
строит путь к файлу и выводит содержимое файла, если файл не найден или он пустой возвращает пустой список.

**Пример кода:**
```
def outputting_transactions_from_file(input_file=None) -> list:
    """Выводит транзакции из файла если найден файл с транзакциями."""
    try:
        project_root = os.path.dirname(os.path.dirname(__file__))
        data_file = os.path.join(project_root, "data", input_file)
        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return []
    except (Exception) as e:
        return []
```

### 9. Чтение файла csv и xlsx

#### Функция `read_file_scv`
читает данные из CSV-файла и возвращает их в виде списка словарей

**Пример кода:**
```
def read_file_scv(input_file: str) -> list:
    """Выводит транзакции из файла .csv в виде списка словарей"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data", input_file)
    with open(data_file, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)
```

#### Функция `read_file_xlsx`
читает данные из Excel-файла и возвращает их в виде списка словарей

**Пример кода:**
```
def read_file_xlsx(input_file: str) -> list:
    """Выводит транзакции из файла .xlsx в виде словарей"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(project_root, "data", input_file)
    df = pd.read_excel(data_file)
    reader = df.to_dict(orient="records")
    return reader
```



---

### Добавленные тесты
В проект были добавлены тесты для проверки корректности
работы функций. Тесты охватывают следующие функции:


### Примеры тестов
#### Для `get_mask_card_number`
```python
assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
assert get_mask_card_number('1234 5678 9012 3456') == '1234 56** **** 3456'
assert get_mask_card_number(' ') == 'Неверный номер карты'
```
#### Для `get_mask_account`
```python
assert get_mask_account('73654108430135874305') == '**4305'
assert get_mask_account('73654108') == 'Неверный номер счета'
```
#### Для `mask_account_card`
```python
assert mask_account_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'
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


### Для `my_function` 
```
def test_log_file_errors():

    @log(filename="log.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("log.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        messag = all_lines[-1]
    assert "".join(messag.split("-->")[-2:]) == " my_function  OK\n"
```

### Для `read_file_scv` 
```
@patch("builtins.open")
@patch("csv.DictReader")
def test_read_file_scv(mock_dictreader, mock_open_file):
    mock_open_file.new = mock_open()
    mock_dictreader.return_value = [{"id": 123}, {"id": 321}]
    result = read_file_scv("")
    assert result == [{"id": 123}, {"id": 321}]
```

### Для `read_file_xlsx` 
```
@patch("pandas.read_excel")
def test_read_file_xlsx(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 123}, {"id": 321}]
    mock_read_excel.return_value = mock_df

    result = read_file_xlsx("")
    assert result == [{"id": 123}, {"id": 321}]
```



### Запуск тестов
#### Для запуска тестов используйте команду:
```
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