import allure
from logger_config import setup_logger

users_logger = setup_logger('users_api_tests', 'users_api_tests.log')

@allure.feature("User Creation and Management")
@allure.story("Test logging in, creating, logging out, logging in with a new created user and deleting a new user.")
def test_user_creation_workflow(user_api_client, get_token):
    """Test creating a new user with a unique email."""
    
    # 1. Log in with test2@fake.com (Check that the token was received from the get_token fixture)
    with allure.step("Checking that token for test2@fake.com was received"):
        assert get_token, "Error: No token in response or token is invalid"
        users_logger.info(f"Token for test2@fake.com received successfully: {get_token}")
    
    user_api_client.token = get_token
    users_logger.info(f"Logged in with token: {get_token}")
        
    # 2. Add a new user Tatiana Malinina
    with allure.step("Adding new user Tatiana Malinina"):         # убрать хардкод
        users_logger.info("Adding new user: Tatiana Malinina")
        response = user_api_client.add_user(
            first_name="Tatiana",
            last_name="Malinina",
            email="tatianamalinina@fake.com",
            password="1234567890"
        )
        
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    response_data = response.json()

    assert 'user' in response_data, "Error: No 'user' key in the response."
    new_user = response_data['user']
    
    assert '_id' in new_user, "Error: No '_id' key in the response."
    assert new_user['firstName'] == "Tatiana", f"Expected 'firstName' to be 'Tatiana', but got {new_user['firstName']}" # хардкод хардкод везде 
    assert new_user['lastName'] == "Malinina", f"Expected 'lastName' to be 'Malinina', but got {new_user['lastName']}"
    new_user_email = new_user['email']
    assert new_user_email == "tatianamalinina@fake.com", f"Expected email to be 'tatianamalinina@fake.com', but got {new_user_email}"
    
    users_logger.info(f"New user created successfully, response status code: {response.status_code}")
    
    # 3. Log out from test2@fake.com (just reset the token)
    with allure.step("Logging out from test2@fake.com"):
        response = user_api_client.logout()
        
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        users_logger.info(f"Logged out from test2@fake.com successfully, response status code: {response.status_code}")

    # 4. Get profile of the new user Tatiana Malinina
    with allure.step("Log in with new user and get profile"):
        users_logger.info(f"Logging in with new user: {new_user_email}")
        token_new_user = user_api_client.login(new_user_email, "1234567890")
        user_api_client.token = token_new_user.get("token")

        users_logger.info("Getting profile for the new user")
        user_profile_response = user_api_client.get_user_profile()

        assert user_profile_response.status_code == 200, f"Expected status code 200 but got {user_profile_response.status_code}"

        user_data = user_profile_response.json()
        assert '_id' in user_data, "Error: No _id in the response"
        assert user_data['firstName'] == "Tatiana", f"Expected 'firstName' to be 'Tatiana', but got {user_data['firstName']}"
        assert user_data['lastName'] == "Malinina", f"Expected 'lastName' to be 'Malinina', but got {user_data['lastName']}"
        assert user_data['email'] == new_user_email, f"Expected email to be '{new_user_email}', but got {user_data['email']}"
        
        users_logger.info(f"User profile received successfully, response status code: {user_profile_response.status_code}")
        
        
    # 5. Delete the new user Tatiana Malinina
    with allure.step("Delete the new user Tatiana Malinina"):
        users_logger.info("Deleting new user: Tatiana Malinina")
        delete_response = user_api_client.delete_user()
        
        assert delete_response.status_code == 200, f"Expected status code 200 for user deletion, but got {delete_response.status_code}"
        
        users_logger.info(f"User deleted successfully, response status code: {delete_response.status_code}")

    # 6. Try to log in with the deleted user
    with allure.step(f"Attempting to log in with deleted user: {new_user_email}"):
        users_logger.info(f"Attempting to log in with deleted user: {new_user_email}")
        
        login_response = user_api_client.login(new_user_email, "1234567890")

        assert login_response.status_code == 401, f"Expected status code 401 when logging in with a deleted user, but got {login_response.status_code}"
    
        users_logger.info(f"Login failed as expected for deleted user, response status code: {login_response.status_code}")