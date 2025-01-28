import pytest
import allure
from api_clients.users_api_client import UsersApiClient
from api_clients.contacts_api_client import ContactsApiClient
from logger_config import setup_logger

users_logger = setup_logger('user_api_tests', 'user_api_tests.log')
contacts_logger = setup_logger('contacts_api_tests', 'contacts_api_tests.log')

@pytest.fixture
@allure.step("Initializing UserApiClient fixture")
def user_api_client():
    """Fixture for the API client"""
    users_logger.info("Initializing UserApiClient fixture")
    return UsersApiClient()

@pytest.fixture
@allure.step("Getting token for user: test2@fake.com")
def get_token(user_api_client, email="test2@fake.com", password="myNewPassword"):
    """Fixture for getting the token for a specific user"""
    users_logger.info(f"Getting token for user: {email}")
    response = user_api_client.login(email, password)
    token = response.get("token")
    if token:
        users_logger.info("Token received successfully")
    else:
        users_logger.error("Failed to receive token")
    return token

@pytest.fixture
@allure.step("Creating ContactsApiClient instance with the retrieved token")
def contacts_api_client(get_token):
    """Fixture for the contacts API client with the authentication token"""
    contacts_logger.info("Creating ContactsApiClient instance with the retrieved token")
    return ContactsApiClient(token=get_token)
