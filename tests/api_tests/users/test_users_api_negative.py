import pytest

def test_invalid_login(user_api_client):
    # Try to log in with wrong email and password
    login_response = user_api_client.login("invalid_email@example.com", "wrongpassword")

    # Check that login fails with an error
    assert "error" in login_response, "Login should fail with wrong credentials"
    assert login_response["error"] == "Invalid email or password", "The error message should show invalid credentials"
