import pytest

from transactions.repository.transactions_repository import TransactionsRepository
from transactions.transactions_service.transactions import Transaction
from transactions.transactions_service.transactions_service import TransactionsService


@pytest.fixture(scope="function")
def transactions_service():
    return TransactionsService(TransactionsRepository())


def test_that_transactions_service_creates_transactions(transactions_service):
    transaction = transactions_service.create_transaction()
    assert isinstance(transaction, Transaction)


def test_that_transactions_service_persists_created_transactions(transactions_service):
    transaction1 = transactions_service.create_transaction()
    transaction2 = transactions_service.create_transaction()
    assert transactions_service.list_transactions() == [transaction1, transaction2]
