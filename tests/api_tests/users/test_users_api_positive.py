import allure
from logger_config import setup_logger
from models.user_data import UserData
from helpers.api_response_helper import ApiResponseHelper

users_logger = setup_logger('users_api_tests', 'users_api_tests.log')

@allure.feature("User Creation and Management")
@allure.story("Test logging in, creating, logging out, logging in with a new created user and deleting a new user.")
def test_user_creation_workflow(user_api_client, get_token):
    """Test creating a new user with a unique email."""
    
    # 1. Log in with test2@fake.com
    with allure.step("Checking that token for test2@fake.com was received"):
        assert get_token, "Error: No token in response or token is invalid"
        users_logger.info(f"Token for test2@fake.com received successfully: {get_token}")
    
    user_api_client.token = get_token
    users_logger.info(f"Logged in with token: {get_token}")
        
    # 2. Add a new user
    new_user_data = UserData(first_name="Tatiana", last_name="Malinina", email="tatianamalinina@fake.com", password="1234567890")
    
    with allure.step(f"Adding new user {new_user_data.first_name} {new_user_data.last_name}"):
        users_logger.info(f"Adding new user: {new_user_data.first_name} {new_user_data.last_name}")
        response = user_api_client.add_user(
            first_name=new_user_data.first_name,  
            last_name=new_user_data.last_name, 
            email=new_user_data.email,
            password=new_user_data.password
        )
        
    ApiResponseHelper.check_response(response, 201, users_logger)

    response_data = response.json()
    ApiResponseHelper.check_user_data(new_user_data, response_data['user'], users_logger)
    
    # 3. Log out from test2@fake.com
    with allure.step("Logging out from test2@fake.com"):
        response = user_api_client.logout()
        ApiResponseHelper.check_response(response, 200, users_logger)

    # 4. Get profile of the new user
    with allure.step(f"Log in with new user {new_user_data.first_name} {new_user_data.last_name} and get profile"):
        users_logger.info(f"Logging in with new user: {new_user_data.email}")
        token_new_user = user_api_client.login(new_user_data.email, new_user_data.password)
        user_api_client.token = token_new_user.get("token")

        users_logger.info("Getting profile for the new user")
        user_profile_response = user_api_client.get_user_profile()

        ApiResponseHelper.check_response(user_profile_response, 200, users_logger)

        user_profile_data = user_profile_response.json()
        ApiResponseHelper.check_user_data(new_user_data, user_profile_data, users_logger)
        
    # 5. Delete the new user
    with allure.step(f"Delete the new user {new_user_data.first_name} {new_user_data.last_name}"):
        users_logger.info(f"Deleting new user: {new_user_data.first_name} {new_user_data.last_name}")
        delete_response = user_api_client.delete_user()
        
        ApiResponseHelper.check_response(delete_response, 200, users_logger)

    # 6. Try to log in with the deleted user
    with allure.step(f"Attempting to log in with deleted user: {new_user_data.email}"):
        users_logger.info(f"Attempting to log in with deleted user: {new_user_data.email}")
        login_response = user_api_client.login(new_user_data.email, new_user_data.password)

        ApiResponseHelper.check_response(login_response, 401, users_logger)