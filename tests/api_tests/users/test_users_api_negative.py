import allure
from logger_config import setup_logger

users_logger = setup_logger('user_api_tests', 'user_api_tests.log')

@allure.feature('User Authentication')
@allure.story('Login with Invalid Credentials')
def test_invalid_login(user_api_client):
    """Test login with incorrect email and password."""
    
    with allure.step("Attempting to log in with invalid credentials"):
        login_response = user_api_client.login("invalid_email@example.com", "wrongpassword")

    # Check that login fails with an error
    with allure.step("Checking if login response has the correct status code (401)"):
        assert login_response.status_code == 401, \
            f"Expected status code 401 but got {login_response.status_code}"
        
        users_logger.info(f"Test passed: login failed as expected with invalid credentials, response status code: {login_response.status_code}")

        
@allure.feature('User Management')
@allure.story('Add Existing User')
def test_add_existing_user(user_api_client):
    """Test adding a user with an already used email."""
    
    used_email = "test2@fake.com"  # Email is already used
    users_logger.info(f"Attempting to add a user with an already used email: {used_email}")
    
    with allure.step("Attempting to add user with existing email"):
        response = user_api_client.add_user(
            first_name="Updated",
            last_name="Username",
            email=used_email,
            password="1234567890"
        )
    
    with allure.step("Checking for email duplication error"):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        users_logger.info(f"Test passed: email address {used_email} is already in use.")
