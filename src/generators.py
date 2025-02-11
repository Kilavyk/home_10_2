from sandbox.sandbox import transactions



def filter_by_currency(items, cur):
    for item in items:
        if cur == item['operationAmount']['currency']['code']:
            yield item


usd_transactions = filter_by_currency(transactions, "RUB")
for operation in range(2):
    print(next(usd_transactions))





def transaction_descriptions():
    pass


def card_number_generator():
    pass
