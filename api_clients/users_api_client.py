import requests
from logger_config import setup_logger

logger = setup_logger(__name__, "users_api_client.log")

class UsersApiClient:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

    def __init__(self):
        self.token = None
        logger.info("UserApiClient initialized.")

    def login(self, email, password):
        """Log in with email and password."""
        logger.info(f"Trying to log in with email: {email}")
        response = requests.post(
            f"{self.BASE_URL}/users/login",
            json={"email": email, "password": password}
        )
        
        if response.status_code == 401:
            logger.info("Login failed: Invalid email or password.")
            return response

        if response.status_code == 404:
            logger.info("Login failed: User not found.")
            return response

        response_data = response.json()

        if 'token' not in response_data:
            logger.info("Error: No token in response.")
            return response

        token = response_data['token']

        if not isinstance(token, str):
            logger.info("Error: Token is not a string.")
            return response

        if len(token) == 0:
            logger.info("Error: Token is empty.")
            return response

        self.token = token
        
        return response_data

    def add_user(self, first_name, last_name, email, password):
        """Method to add new user."""
        logger.info(f"Adding new user: {first_name} {last_name}, Email: {email}")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.post(
            f"{self.BASE_URL}/users",
            json={"firstName": first_name, "lastName": last_name, "email": email, "password": password},
            headers=headers
        )
    
        return response
    
    def get_user_profile(self):
        """Method to get user profile."""
        logger.info("Getting user profile.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.BASE_URL}/users/me", headers=headers)
        
        return response

    def delete_user(self):
        """Method to delete logged in user."""
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.delete(
            f"{self.BASE_URL}/users/me",
            headers=headers
        )
                
        return response
    
    def logout(self):
        """Method to log out user."""
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.post(f"{self.BASE_URL}/users/logout", headers=headers)
        
        self.token = None
        return response