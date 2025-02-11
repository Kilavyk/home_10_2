from sandbox.sandbox import transactions



def filter_by_currency(items, cur):
    for item in items:
        if cur == item['operationAmount']['currency']['code']:
            yield item


usd_transactions = filter_by_currency(transactions, "RUB")
for operation in range(2):
    print(next(usd_transactions))



def transaction_descriptions(items):
    for item in items:
        yield item['description']



descriptions = transaction_descriptions(transactions)
for operation in range(5):
    print(next(descriptions))


def card_number_generator(start, end):
    for number in range(start, end + 1):
        card_number = str(number).zfill(16)
        formatted_card_number = (card_number[0:4]
                                 + " "
                                 + card_number[4:8]
                                 + " "
                                 + card_number[8:12]
                                 + " "
                                 + card_number[12:16])
        yield formatted_card_number


for card_number in card_number_generator(1, 15):
    print(card_number)