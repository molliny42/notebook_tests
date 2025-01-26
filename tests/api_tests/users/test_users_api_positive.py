
import pytest

def test_user_creation_workflow(user_api_client, get_token):
    """Test creating a new user with a unique email."""
    
    # 1. Log in with test2@fake.com (from the get_token fixture)
    token_test2 = get_token
    user_api_client.token = token_test2
    print(f"Token for test2@fake.com: {token_test2}")

    # 2. Add a new user Tania Malinina
    response = user_api_client.add_user(
        first_name="Tania",
        last_name="Malinina",
        email="taniamalinina@fake.com",
        password="1234567890"
    )
    
    assert 'user' in response, "Error: No 'user' key in the response."
    new_user = response['user']
    assert '_id' in new_user, "Error: No '_id' key in the response."
    assert new_user['firstName'] == "Tania", f"Error: firstName {new_user['firstName']} doesn't match the expected."
    assert new_user['lastName'] == "Malinina", f"Error: lastName {new_user['lastName']} doesn't match the expected."
    new_user_email = new_user['email']
    assert new_user_email == "taniamalinina@fake.com", f"Error: Email {new_user['email']} doesn't match the expected."

    # 3. Log out from test2@fake.com (just reset the token)
    user_api_client.logout()
    print("Logged out from test2@fake.com")

    # 4. Get profile of the new user Tania Malinina
    token_new_user = user_api_client.login(new_user_email, "1234567890")
    user_api_client.token = token_new_user.get("token")

    user_profile = user_api_client.get_user_profile()
    print(user_profile)
    
    user_data = user_profile.json()
    assert '_id' in user_data, "Error: No _id in the response."
    assert user_data['firstName'] == "Tania", f"Error: firstName {user_data['firstName']} doesn't match the expected."
    assert user_data['lastName'] == "Malinina", f"Error: lastName {user_data['lastName']} doesn't match the expected."
    assert user_data['email'] == new_user_email, f"Error: Email {user_data['email']} doesn't match the expected."


    # 5. Delete the new user Tania Malinina
    delete_response = user_api_client.delete_user()
    assert delete_response.status_code == 200
    print(f"Deleted user response: {delete_response.status_code}")
    
    # 6. Try to log in with the deleted user
    login_response = user_api_client.login(new_user_email, "1234567890")

    # Ensure login fails with a proper error
    assert "error" in login_response, "Login should fail with deleted user"
    assert login_response["error"] in ["Invalid email or password", "User not found"]