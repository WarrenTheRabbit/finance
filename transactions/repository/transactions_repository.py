from typing import List
from transactions.transactions_service.transactions import Transaction

class TransactionsRepository:
    def __init__(self):
        self.database = []
    
    def add(self) -> Transaction:
        transaction = Transaction()
        self.database.append(transaction)
        return transaction
    
    def list(self) -> List[Transaction]:
        return self.database