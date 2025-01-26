import pytest

NON_EXISTING_CONTACT_ID = "6085a221fcfc72405667c3d5"

def test_add_contact_missing_first_name(contacts_api_client):
    """Test adding a contact with missing the first_name field."""
    response = contacts_api_client.add_contact(
        first_name="",  
        last_name="Malinina",
        birthdate="1996-01-24",
        email="taniamalinina@fake.com",
        phone="19960124",
        street1="Batorego 14",
        street2="Terebelska 5",
        city="Biala Podlaska",
        state_province="LB",
        postal_code="21-500",
        country="PL"
    )
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
    message = response.json().get("message")
    assert message == "Contact validation failed: firstName: Path `firstName` is required.", f"Expected error message: 'Contact validation failed: firstName: Path `firstName` is required.' but got {message}"

def test_add_contact_missing_last_name(contacts_api_client):
    """Test adding a contact with missing the last_name field."""
    response = contacts_api_client.add_contact(
        first_name="Tatiana",  
        last_name="",
        birthdate="1996-01-24",
        email="taniamalinina@fake.com",
        phone="19960124",
        street1="Batorego 14",
        street2="Terebelska 5",
        city="Biala Podlaska",
        state_province="LB",
        postal_code="21-500",
        country="PL"
    )
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
    message = response.json().get("message")
    assert message == "Contact validation failed: lastName: Path `lastName` is required.", f"Expected error message: 'Contact validation failed: lastName: Path `lastName` is required.' but got {message}"

def test_get_non_existing_contact(contacts_api_client):
    """Test getting a non-existing contact."""
    response = contacts_api_client.get_contact_by_id(NON_EXISTING_CONTACT_ID)
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

def test_delete_non_existing_contact(contacts_api_client):
    """Test deleting a non-existing contact."""
    response = contacts_api_client.delete_contact(NON_EXISTING_CONTACT_ID)
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
