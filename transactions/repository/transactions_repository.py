from transactions.transactions_service.transactions import Transaction


class TransactionsRepository:
    def __init__(self):
        self.database = []

    def add(self) -> Transaction:
        transaction = Transaction()
        self.database.append(transaction)
        return transaction
