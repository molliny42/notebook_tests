import allure
from logger_config import setup_logger

logger = setup_logger('contacts_api_tests', 'contacts_api_tests.log')

@allure.feature("Contact Creation and Management")
@allure.story("Test adding a new contact")
def test_add_contact(contacts_api_client):
    """Test adding a new contact."""
    
    with allure.step("Add a new contact"):
        logger.info("Adding a new contact: Ivan Ivanov")
        response = contacts_api_client.add_contact(
            first_name="Ivan",
            last_name="Ivanov",
            birthdate="1990-01-01",
            email="ivanivanov@fake.com",
            phone="1234567890",
            street1="Kirova 5",
            street2="Sovetskaya",
            city="Brest",
            state_province="Brestskaya",
            postal_code="224000",
            country="BY"
        )
    
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    response_data = response.json()
    assert "_id" in response_data, "Expected '_id' to be present in the response"
    assert response_data["firstName"] == "Ivan", f"Expected 'firstName' to be 'Ivan', but got {response_data['firstName']}"
    assert response_data["lastName"] == "Ivanov", f"Expected 'lastName' to be 'Ivanov', but got {response_data['lastName']}"
    assert response_data["email"] == "ivanivanov@fake.com", f"Expected 'email' to be 'ivanivanov@fake.com', but got {response_data['email']}"

@allure.feature("Contact Receiving")
@allure.story("Test getting all contacts")
def test_get_contacts(contacts_api_client):
    """Test getting all contacts."""
    
    with allure.step("Get all contacts"):
        logger.info("Fetching all contacts.")
        response = contacts_api_client.get_contacts()
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    response_data = response.json()
    assert isinstance(response_data, list), "Expected response to be a list of contacts"
    assert len(response_data) > 0, "Expected list of contacts to contain at least one contact"

@allure.feature("Contact Receiving")
@allure.story("Test getting a contact by ID")
def test_get_contact_by_id(contacts_api_client):
    """Test getting a contact by ID."""
    
    with allure.step("Add a new contact for receiving"):
        logger.info("Adding a new contact for receiving: Anna Kowalska")
        add_response = contacts_api_client.add_contact(
            first_name="Anna",
            last_name="Kowalska",
            birthdate="1990-02-02",
            email="annakowalska@fake.com",
            phone="0987654321",
            street1="Brzeska 100",
            street2="Kopernika 7",
            city="Warsaw",
            state_province="Mazowieckie",
            postal_code="00-001",
            country="PL"
        )
    
    contact_id = add_response.json()["_id"]
    
    with allure.step(f"Get contact by ID: {contact_id}"):
        logger.info(f"Fetching contact with ID: {contact_id}")
        get_response = contacts_api_client.get_contact_by_id(contact_id)
    
    assert get_response.status_code == 200, f"Expected status code 200, but got {get_response.status_code}"
    get_response_data = get_response.json()
    assert get_response_data["_id"] == contact_id, f"Expected contact ID to be {contact_id}, but got {get_response_data['_id']}"
    assert get_response_data["firstName"] == "Anna", f"Expected 'firstName' to be 'Anna', but got {get_response_data['firstName']}"
    assert get_response_data["lastName"] == "Kowalska", f"Expected 'lastName' to be 'Kowalska', but got {get_response_data['lastName']}"

@allure.feature("Contact Update")
@allure.story("Test updating a contact")
def test_update_contact(contacts_api_client):
    """Test updating a contact."""
    
    with allure.step("Add a new contact for updating"):
        logger.info("Adding a new contact for updating: Tatiana Malinina")
        add_response = contacts_api_client.add_contact(
            first_name="Tatiana",  
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
    
    contact_id = add_response.json()["_id"]
   
    with allure.step(f"Update contact with ID: {contact_id}"):
        logger.info(f"Updating contact with ID: {contact_id}")
        update_response = contacts_api_client.update_contact(
            contact_id,
            first_name="Tatiana",
            last_name="Kerimova",
            email="taniamakerimova@fake.com",
            phone="1234567890",
            street1="New Address 123",
            street2="Flat 45",
            city="Lublin",
            state_province="Lubelskie",
            postal_code="20-100",
            country="PL"
        )
    
    assert update_response.status_code == 200, f"Expected status code 200, but got {update_response.status_code}"
    update_response_data = update_response.json()
    assert update_response_data["_id"] == contact_id, f"Expected contact ID to be {contact_id}, but got {update_response_data['_id']}"
    assert update_response_data["firstName"] == "Tatiana", f"Expected 'firstName' to be 'Tatiana', but got {update_response_data['firstName']}"
    assert update_response_data["lastName"] == "Kerimova", f"Expected 'lastName' to be 'Kerimova', but got {update_response_data['lastName']}"
    assert update_response_data["email"] == "taniamakerimova@fake.com", f"Expected 'email' to be 'taniamakerimova@fake.com', but got {update_response_data['email']}"

@allure.feature("Contact Deletion")
@allure.story("Test deleting a contact")
def test_delete_contact(contacts_api_client):
    """Test deleting a contact."""
    
    with allure.step("Add a new contact for deletion"):
        logger.info("Adding a new contact for deletion: Tatiana Malinina")
        add_response = contacts_api_client.add_contact(
            first_name="Tatiana",  
            last_name="Malinina",
            birthdate="1996-01-24",
            email="taniamalinina@fake.com",
            phone="19960124",
            street1="Batorego 14",
            street2="Terebelska 5",
            city="Biala Podlaska",
            state_province="LB",
            postal_code="21500",
            country="PL"
        )

    contact_id = add_response.json()["_id"]

    with allure.step(f"Delete contact with ID: {contact_id}"):
        logger.info(f"Deleting contact with ID: {contact_id}")
        delete_response = contacts_api_client.delete_contact(contact_id)
    
    assert delete_response.status_code == 200, f"Expected status code 200, but got {delete_response.status_code}"