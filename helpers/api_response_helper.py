class ApiResponseHelper:
    """Helper class for API response validations"""
    
    @staticmethod
    def check_response(response, expected_status_code, logger):
        """Helper to check the response status code."""
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {response.status_code}"
        logger.info(f"Response status code: {response.status_code}")

    @staticmethod
    def check_user_data(expected_data, actual_data, logger):
        """Helper to check user data in the response"""
        assert '_id' in actual_data, "Error: No '_id' key in the response."
        assert actual_data['firstName'] == expected_data.first_name, \
            f"Expected 'firstName' to be {expected_data.first_name}, but got {actual_data['firstName']}"
        assert actual_data['lastName'] == expected_data.last_name, \
            f"Expected 'lastName' to be {expected_data.last_name}, but got {actual_data['lastName']}"
        assert actual_data['email'] == expected_data.email, \
            f"Expected email to be {expected_data.email}, but got {actual_data['email']}"
        logger.info(f"User data matches for {expected_data.email}")
