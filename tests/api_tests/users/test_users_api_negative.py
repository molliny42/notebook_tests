import pytest

def test_invalid_login(user_api_client):
    # Try to log in with wrong email and password
    login_response = user_api_client.login("invalid_email@example.com", "wrongpassword")

    # Check that login fails with an error
    assert "error" in login_response, "Login should fail with invalid credentials"
    assert login_response["error"] == "Invalid email or password", "The error message should show invalid credentials"

def test_add_existing_user(user_api_client):
    # Try to add a user with an already existing email
    response = user_api_client.add_user(
        first_name="Updated",
        last_name="Username",
        email="test2@fake.com", # This email is already used
        password="1234567890"
    )
    
    assert response.get("error") == "Email address is already in use", "The error message should indicate that the email is already in use"