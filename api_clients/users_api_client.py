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
        
        # Check if login failed
        if response.status_code == 401:
            logger.error("Login failed: Invalid email or password.")
            return {"error": "Invalid email or password"}
    
        if response.status_code == 404:
            logger.error("Login failed: User not found.")
            return {"error": "User not found"}
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            raise
                
        response_data = response.json()
        
        if 'token' not in response_data:
            logger.error("Error: No token in response.")
            raise ValueError("Error: No token in response.")
        
        token = response_data['token']
        
        if not isinstance(token, str):
            logger.error("Error: Token is not a string.")
            raise ValueError("Error: Token must be string.")
        
        if len(token) == 0:
            logger.error("Error: Token is empty.")
            raise ValueError("Error: Token is empty.")
        
        self.token = token
        logger.info("Login successful. Token received.")
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
        
        if response.status_code == 400 and "Email address is already in use" in response.text:
            return {"error": "Email address is already in use"}

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred while adding user: {e}")
            raise
        
        logger.info(f"User {first_name} {last_name} added successfully.")        
        return response.json()
    
    def get_user_profile(self):
        """Method to get user profile."""
        logger.info("Getting user profile.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        print("headers")
        print(headers)
        response = requests.get(f"{self.BASE_URL}/users/me", headers=headers)
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"Error getting user profile: {e}")
            raise
        
        logger.info("User profile received successfully.")
        return response

    def delete_user(self):
        """Method to delete logged-in user."""
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        print("headers for deleting")
        print(headers)
        response = requests.delete(
            f"{self.BASE_URL}/users/me",
            headers=headers
        )
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"Error deleting user: {e}")
            raise
        
        logger.info("User deleted successfully.")
        return response
    
    def logout(self):
        """Method to log out user."""
        if not self.token:
            logger.error("Error: Token not found. Please log in first.")
            raise ValueError("Error: Token not found. Log in first.")
        
        logger.info("Logging out user.")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(f"{self.BASE_URL}/users/logout", headers=headers)
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"Error logging out: {e}")
            raise
        
        self.token = None
        logger.info("User logged out successfully.")
        return response