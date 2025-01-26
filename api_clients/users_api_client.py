import requests

class UserApiClient:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

    def __init__(self):
        self.token = None

    def login(self, email, password):
        """Log in with email and password."""
        response = requests.post(
            f"{self.BASE_URL}/users/login",
            json={"email": email, "password": password}
        )
        
        # Check if login failed
        if response.status_code == 401:
            return {"error": "Invalid email or password"}
    
        if response.status_code == 404:
            return {"error": "User not found"}
        
        response.raise_for_status()
        
        response_data = response.json()
        
        if 'token' not in response_data:
            raise ValueError("Error: No token in response.")
        
        token = response_data['token']
        
        if not isinstance(token, str):
            raise ValueError("Error: Token must be string.")
        
        if len(token) == 0:
            raise ValueError("Error: Token is empty.")
        
        self.token = token
        
        return response_data

    def add_user(self, first_name, last_name, email, password):
        """Method to add new user."""
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.post(
            f"{self.BASE_URL}/users",
            json={"firstName": first_name, "lastName": last_name, "email": email, "password": password},
            headers=headers
        )
        
        response.raise_for_status()
        
        return response.json()
    
    def get_user_profile(self):
        """Method to get user profile."""
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        print("headers")
        print(headers)
        response = requests.get(f"{self.BASE_URL}/users/me", headers=headers)
        
        response.raise_for_status()
        
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
        
        response.raise_for_status()
        
        return response
    
    def logout(self):
        """Method to log out user."""
        if not self.token:
            raise ValueError("Error: Token not found. Log in first.")
        
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(f"{self.BASE_URL}/users/logout", headers=headers)
        
        response.raise_for_status()
        
        self.token = None
        
        return response