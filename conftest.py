import pytest
from api_clients.users_api_client import UserApiClient
from api_clients.contacts_api_client import ContactsApiClient

@pytest.fixture
def user_api_client():
    """Fixture for the API client"""
    return UserApiClient()

@pytest.fixture
def get_token(user_api_client):
    """Fixture for getting the token for user test2@fake.com"""
    response = user_api_client.login("test2@fake.com", "myNewPassword")
    return response["token"]

@pytest.fixture
def contacts_api_client(get_token):
    """Fixture for the contacts API client with the authentication token"""
    return ContactsApiClient(token=get_token)
