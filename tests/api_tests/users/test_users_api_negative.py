import pytest

def test_invalid_login(user_api_client):
    """Test login with incorrect email and password."""
    login_response = user_api_client.login("invalid_email@example.com", "wrongpassword")

    # Check that login fails with an error
    assert "error" in login_response, "Expected an error message when login fails with invalid credentials."
    assert login_response["error"] == "Invalid email or password", f"Expected 'Invalid email or password', but got {login_response['error']}"

def test_add_existing_user(user_api_client):
    """Test adding a user with an already used email."""
    response = user_api_client.add_user(
        first_name="Updated",
        last_name="Username",
        email="test2@fake.com", # Email is already used
        password="1234567890"
    )
    
    assert response.get("error") == "Email address is already in use", f"Expected error 'Email address is already in use', but got {response.get('error')}"