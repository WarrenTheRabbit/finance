from transactions.repository.transactions_repository import TransactionsRepository
from transactions.transactions_service.transactions import Transaction

class TransactionsService:
    def __init__(self, transactions_repository: TransactionsRepository):
        self.transactions_repository = transactions_repository
    
    def get_transaction(self):
        pass
    
    def create_transaction(self) -> Transaction:
        return self.transactions_repository.add()
    
    def list_transactions(self):
        return self.transactions_repository.list()
    
    