import pytest
from api_clients.users_api_client import UserApiClient

@pytest.fixture
def user_api_client():
    """Fixture for the API client"""
    return UserApiClient()

@pytest.fixture
def get_token(user_api_client):
    """Fixture for getting the token for user test2@fake.com"""
    response = user_api_client.login("test2@fake.com", "myNewPassword")
    return response["token"]