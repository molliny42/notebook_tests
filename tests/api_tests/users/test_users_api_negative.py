import allure
from logger_config import setup_logger

logger = setup_logger('user_api_tests', 'user_api_tests.log')

@allure.feature('User Authentication')
@allure.story('Login with Invalid Credentials')
def test_invalid_login(user_api_client):
    """Test login with incorrect email and password."""
    
    with allure.step("Attempting to log in with invalid credentials"):
        login_response = user_api_client.login("invalid_email@example.com", "wrongpassword")

    # Check that login fails with an error
    with allure.step("Checking for error in the login response"):
        assert "error" in login_response, "Expected an error message when login fails with invalid credentials."
        assert login_response["error"] == "Invalid email or password", \
            f"Expected 'Invalid email or password', but got {login_response['error']}"
        
        logger.info("Login failed as expected with error: %s", login_response["error"])
        
@allure.feature('User Management')
@allure.story('Add Existing User')
def test_add_existing_user(user_api_client):
    """Test adding a user with an already used email."""
    
    with allure.step("Attempting to add a user with an already used email"):
        response = user_api_client.add_user(
            first_name="Updated",
            last_name="Username",
            email="test2@fake.com", # Email is already used
            password="1234567890"
        )
    
    with allure.step("Checking for email duplication error in the response"):
        assert response.get("error") == "Email address is already in use", \
            f"Expected error 'Email address is already in use', but got {response.get('error')}"
        logger.info("Failed to add user as expected with error: %s", response.get("error"))