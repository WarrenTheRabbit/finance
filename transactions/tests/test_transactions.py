import pytest

from transactions.transactions_service.transactions_service import TransactionsService
from transactions.transactions_service.transactions import Transaction
from transactions.repository.transactions_repository import TransactionsRepository

@pytest.fixture(scope="function")
def transactions_service():
    return TransactionsService(TransactionsRepository())

def test_that_transactions_service_creates_transactions(transactions_service):
    transaction = transactions_service.create_transaction()
    assert isinstance(transaction, Transaction)
