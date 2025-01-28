import allure
from logger_config import setup_logger
from models.contact_data import ContactData
from helpers.api_response_helper import ApiResponseHelper  # импортируем ApiResponseHelper

logger = setup_logger('contacts_api_tests', 'contacts_api_tests.log')

@allure.feature("Contact Creation and Management")
@allure.story("Test adding a new contact")
def test_add_contact(contacts_api_client):
    """Test adding a new contact."""
    
    contact_data = ContactData(
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

    with allure.step(f"Add a new contact: {contact_data}"):
        logger.info(f"Adding a new contact: {contact_data}")
        response = contacts_api_client.add_contact(contact_data.to_dict())

    ApiResponseHelper.check_response(response, 201, logger)
    response_data = response.json()
    ApiResponseHelper.check_user_data(contact_data, response_data, logger)

@allure.feature("Contact Receiving")
@allure.story("Test getting all contacts")
def test_get_contacts(contacts_api_client):
    """Test getting all contacts."""
    
    with allure.step("Get all contacts"):
        logger.info("Fetching all contacts.")
        response = contacts_api_client.get_contacts()
    
    ApiResponseHelper.check_response(response, 200, logger)
    response_data = response.json()
    assert isinstance(response_data, list), "Expected response to be a list of contacts"
    assert len(response_data) > 0, "Expected list of contacts to contain at least one contact"

@allure.feature("Contact Receiving")
@allure.story("Test getting a contact by ID")
def test_get_contact_by_id(contacts_api_client):
    """Test getting a contact by ID."""
    
    contact_data = ContactData(
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

    with allure.step("Add a new contact for receiving"):
        logger.info("Adding a new contact for receiving: Anna Kowalska")
        add_response = contacts_api_client.add_contact(contact_data.to_dict())
    
    contact_id = add_response.json()["_id"]
    
    with allure.step(f"Get contact by ID: {contact_id}"):
        logger.info(f"Fetching contact with ID: {contact_id}")
        get_response = contacts_api_client.get_contact_by_id(contact_id)
    
    ApiResponseHelper.check_response(get_response, 200, logger)
    get_response_data = get_response.json()
    assert get_response_data["_id"] == contact_id, f"Expected contact ID to be {contact_id}, but got {get_response_data['_id']}"
    ApiResponseHelper.check_user_data(contact_data, get_response_data, logger)

@allure.feature("Contact Update")
@allure.story("Test updating a contact")
def test_update_contact(contacts_api_client):
    """Test updating a contact."""
    
    contact_data = ContactData(
        first_name="Tatiana",  
        last_name="Rinina",
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

    with allure.step("Add a new contact for updating"):
        logger.info(f"Adding a new contact for updating: {contact_data}")
        add_response = contacts_api_client.add_contact(contact_data.to_dict())
        assert add_response.status_code == 201
    
    contact_id = add_response.json()["_id"]
   
    updated_contact_data = ContactData(
        first_name="Tatiana",
        last_name="Maximova",
        birthdate="1996-01-24",
        email="taniamakerimova@fake.com",
        phone="1234567890",
        street1="New Address 123",
        street2="Flat 45",
        city="Lublin",
        state_province="Lubelskie",
        postal_code="20-100",
        country="PL"
    )
    
    with allure.step(f"Update contact with ID: {contact_id}"):
        logger.info(f"Updating contact with ID: {contact_id}")
        update_response = contacts_api_client.update_contact(contact_id, updated_contact_data)
    logger.info(f"Response body: {update_response.text}")
        
    ApiResponseHelper.check_response(update_response, 200, logger)
    update_response_data = update_response.json()
    assert update_response_data["_id"] == contact_id, f"Expected contact ID to be {contact_id}, but got {update_response_data['_id']}"
    ApiResponseHelper.check_user_data(updated_contact_data, update_response_data, logger)

@allure.feature("Contact Deletion")
@allure.story("Test deleting a contact")
def test_delete_contact(contacts_api_client):
    """Test deleting a contact."""
    
    contact_data = ContactData(
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

    with allure.step("Add a new contact for deletion"):
        logger.info(f"Adding a new contact for deletion: {contact_data}")
        add_response = contacts_api_client.add_contact(contact_data.to_dict())

    contact_id = add_response.json()["_id"]

    with allure.step(f"Delete contact with ID: {contact_id}"):
        logger.info(f"Deleting contact with ID: {contact_id}")
        delete_response = contacts_api_client.delete_contact(contact_id)
    
    ApiResponseHelper.check_response(delete_response, 200, logger)
