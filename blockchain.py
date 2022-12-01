blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


add_value(2)
add_value(transaction_amount=0.9, last_transaction=get_last_blockchain_value())
add_value(10.89, get_last_blockchain_value())

print(blockchain)
