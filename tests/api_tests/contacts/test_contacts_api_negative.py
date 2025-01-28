import allure
from logger_config import setup_logger
from helpers.api_response_helper import ApiResponseHelper  # Импортируем ApiResponseHelper

logger = setup_logger('contacts_api_tests', 'contacts_api_tests.log')

NON_EXISTING_CONTACT_ID = "6085a221fcfc72405667c3d5"

@allure.feature("Contact Management")
@allure.story("Test adding a contact with missing first name")
def test_add_contact_missing_first_name(contacts_api_client):
    """Test adding a contact with missing the first_name field"""
    logger.info("Attempting to add contact with missing first_name")
    
    contact_data = {
        "first_name": "",
        "last_name": "Malinina",
        "birthdate": "1996-01-24",
        "email": "taniamalinina@fake.com",
        "phone": "19960124",
        "street1": "Batorego 14",
        "street2": "Terebelska 5",
        "city": "Biala Podlaska",
        "state_province": "LB",
        "postal_code": "21-500",
        "country": "PL"
    }

    with allure.step("Add contact with missing first name"):
        response = contacts_api_client.add_contact(contact_data)
    
    ApiResponseHelper.check_response(response, 400, logger)  # Проверяем статус код
    message = response.json().get("message")
    assert message == "Contact validation failed: firstName: Path `firstName` is required.", \
        f"Expected error message: 'Contact validation failed: firstName: Path `firstName` is required.', but got {message}"
    logger.info("Test passed: validation failed as expected due to missing first name.")

@allure.feature("Contact Management")
@allure.story("Test adding a contact with missing last name")
def test_add_contact_missing_last_name(contacts_api_client):
    """Test adding a contact with missing the last_name field."""
    logger.info("Attempting to add contact with missing last_name.")
    
    contact_data = {
        "first_name": "Tatiana",
        "last_name": "",
        "birthdate": "1996-01-24",
        "email": "taniamalinina@fake.com",
        "phone": "19960124",
        "street1": "Batorego 14",
        "street2": "Terebelska 5",
        "city": "Biala Podlaska",
        "state_province": "LB",
        "postal_code": "21-500",
        "country": "PL"
    }

    with allure.step("Add contact with missing last name"):
        response = contacts_api_client.add_contact(contact_data)
    
    ApiResponseHelper.check_response(response, 400, logger)
    message = response.json().get("message")
    assert message == "Contact validation failed: lastName: Path `lastName` is required.", \
        f"Expected error message: 'Contact validation failed: lastName: Path `lastName` is required.' but got {message}"
    logger.info("Test passed: validation failed as expected due to missing last name")

@allure.feature("Contact Management")
@allure.story("Test getting a non-existing contact")    
def test_get_non_existing_contact(contacts_api_client):
    """Test getting a non-existing contact."""
    logger.info(f"Attempting to fetch non-existing contact with ID {NON_EXISTING_CONTACT_ID}")
    
    with allure.step("Get contact by non-existing ID"):
        response = contacts_api_client.get_contact_by_id(NON_EXISTING_CONTACT_ID)
    
    ApiResponseHelper.check_response(response, 404, logger)
    logger.info(f"Test passed: contact with ID {NON_EXISTING_CONTACT_ID} does not exist.")

@allure.feature("Contact Management")
@allure.story("Test deleting a non-existing contact")    
def test_delete_non_existing_contact(contacts_api_client):
    """Test deleting a non-existing contact."""
    logger.info(f"Attempting to delete non-existing contact with ID {NON_EXISTING_CONTACT_ID}")
    
    with allure.step("Delete contact by non-existing ID"):
        response = contacts_api_client.delete_contact(NON_EXISTING_CONTACT_ID)
    
    ApiResponseHelper.check_response(response, 404, logger)
    logger.info(f"Test passed: contact with ID {NON_EXISTING_CONTACT_ID} does not exist")
