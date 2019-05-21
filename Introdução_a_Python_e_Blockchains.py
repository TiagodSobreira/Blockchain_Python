blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount,last_transaction = [1]):
    blockchain.append([last_transaction, transaction_amount])
    print(transaction_amount)

add_value(8.9)
add_value(5.5,get_last_blockchain_value())
add_value(4,get_last_blockchain_value())

print(blockchain)
