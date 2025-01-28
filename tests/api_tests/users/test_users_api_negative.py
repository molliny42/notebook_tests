import allure
from logger_config import setup_logger
from models.user_data import UserData
from helpers.api_response_helper import ApiResponseHelper

users_logger = setup_logger('users_api_tests', 'users_api_tests.log')

invalid_credentials = UserData(first_name="Test", last_name="Test", email="invalid_email@fake.com", password="wrongpassword")
existing_user_data = UserData(first_name="Updated", last_name="Username", email="test2@fake.com", password="1234567890")

@allure.feature('User Authentication')
@allure.story('Login with Invalid Credentials')
def test_invalid_login(user_api_client):
    """Test login with incorrect email and password."""
    
    with allure.step(f"Attempting to log in with invalid credentials for {invalid_credentials.email}"):
        login_response = user_api_client.login(invalid_credentials.email, invalid_credentials.password)

    ApiResponseHelper.check_response(login_response, 401, users_logger)
    
    users_logger.info(f"Test passed: login failed as expected with invalid credentials for {invalid_credentials.email}, response status code: {login_response.status_code}")
        
@allure.feature('User Management')
@allure.story('Add Existing User')
def test_add_existing_user(user_api_client):
    """Test adding a user with an already used email."""
    
    used_email = existing_user_data.email
    users_logger.info(f"Attempting to add user with an already used email: {used_email}")
    
    with allure.step(f"Attempting to add user with existing email {used_email}"):
        response = user_api_client.add_user(
            first_name=existing_user_data.first_name,
            last_name=existing_user_data.last_name,
            email=used_email,
            password=existing_user_data.password
        )
    
    ApiResponseHelper.check_response(response, 400, users_logger)
    
    users_logger.info(f"Test passed: email address {used_email} is already in use")