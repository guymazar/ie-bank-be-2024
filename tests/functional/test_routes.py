from iebank_api import app
from iebank_api.models import Account
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'belgium'})
    assert response.status_code == 200


def test_account_balance_update():
    """
    GIVEN an Account model
    WHEN the balance is updated
    THEN check if the new balance is reflected correctly
    """
    account = Account('John Doe', '€', 'belgium')
    account.balance = 250.0
    assert account.balance == 250.0

def test_invalid_country(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is invalid for a country containing numbers
    """
    # Test with an invalid country (containing numbers)
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Belgium123'})
    assert response.status_code == 400
    assert b'Invalid country: Country name should not contain numbers' in response.data




