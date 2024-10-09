from iebank_api.models import Account
import pytest


def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status, country and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'belgium')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == 'belgium'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active' 

def test_account_number_uniqueness():
    account1 = Account('John Doe', '€', 'belgium')
    account2 = Account('Jane Smith', '€', 'belgium')
    assert account1.account_number != account2.account_number

def test_status_value():
    account = Account('John Doe', '€', 'belgium')
    assert account.status in ['Active', 'Inactive', 'Closed']