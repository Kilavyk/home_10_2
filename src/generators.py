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





def card_number_generator():
    pass
