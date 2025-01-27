import allure
from logger_config import setup_logger

logger = setup_logger('user_api_tests', 'user_api_tests.log')

@allure.feature("User Creation and Management")
@allure.story("Test logging in, creating, logging out, logging in with a new created user and deleting a new user.")
def test_user_creation_workflow(user_api_client, get_token):
    """Test creating a new user with a unique email."""
    
    # 1. Log in with test2@fake.com (from the get_token fixture)
    with allure.step("Log in with existing user test2@fake.com"):
        token_test2 = get_token
        user_api_client.token = token_test2
        logger.info(f"Token for test2@fake.com: {token_test2}")
        logger.info("Logging in with test2@fake.com")

    # 2. Add a new user Tatiana Malinina
    with allure.step("Add new user Tatiana Malinina"):
        logger.info("Adding new user: Tatiana Malinina")
        response = user_api_client.add_user(
            first_name="Tatiana",
            last_name="Malinina",
            email="tatianamalinina@fake.com",
            password="1234567890"
        )
    
    assert 'user' in response, "Error: No 'user' key in the response."
    new_user = response['user']
    assert '_id' in new_user, "Error: No '_id' key in the response."
    assert new_user['firstName'] == "Tatiana", f"Expected 'firstName' to be 'Tatiana', but got {new_user['firstName']}."
    assert new_user['lastName'] == "Malinina", f"Expected 'lastName' to be 'Malinina', but got {new_user['lastName']}."
    new_user_email = new_user['email']
    assert new_user_email == "tatianamalinina@fake.com", f"Expected email to be 'tatianamalinina@fake.com', but got {new_user_email}."
    
    logger.info(f"New user created with email: {new_user_email}")
    
    # 3. Log out from test2@fake.com (just reset the token)
    with allure.step("Log out from test2@fake.com"):
        user_api_client.logout()
        logger.info("Logged out from test2@fake.com")

    # 4. Get profile of the new user Tatiana Malinina
    with allure.step("Log in with new user and get profile"):
        logger.info(f"Logging in with new user: {new_user_email}")
        token_new_user = user_api_client.login(new_user_email, "1234567890")
        user_api_client.token = token_new_user.get("token")

        logger.info("Getting profile for the new user.")
        user_profile = user_api_client.get_user_profile()
        
        user_data = user_profile.json()
        assert '_id' in user_data, "Error: No _id in the response."
        assert user_data['firstName'] == "Tatiana", f"Expected 'firstName' to be 'Tatiana', but got {user_data['firstName']}."
        assert user_data['lastName'] == "Malinina", f"Expected 'lastName' to be 'Malinina', but got {user_data['lastName']}."
        assert user_data['email'] == new_user_email, f"Expected email to be '{new_user_email}', but got {user_data['email']}."
        
    # 5. Delete the new user Tatiana Malinina
    with allure.step("Delete the new user Tatiana Malinina"):
        logger.info("Deleting new user: Tatiana Malinina")
        delete_response = user_api_client.delete_user()
        assert delete_response.status_code == 200, f"Expected status code 200 for user deletion, but got {delete_response.status_code}."
        logger.info(f"User deleted, response status code: {delete_response.status_code}")
    
    # 6. Try to log in with the deleted user
    with allure.step(f"Attempting to log in with deleted user: {new_user_email}"):
        logger.info(f"Attempting to log in with deleted user: {new_user_email}")
        login_response = user_api_client.login(new_user_email, "1234567890")

    # Ensure login fails with a proper error
    assert "error" in login_response, "Expected an error message when logging in with a deleted user."
    assert login_response["error"] in ["Invalid email or password", "User not found"], \
        f"Expected 'Invalid email or password' or 'User not found' error, but got {login_response['error']}."
    logger.info("Login failed as expected with a deleted user.")