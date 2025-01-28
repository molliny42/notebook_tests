import requests
from logger_config import setup_logger
from models.contact_data import ContactData

logger = setup_logger(__name__, "contacts_api_client.log")

class ContactsApiClient:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

    def __init__(self, token=None):
        self.token = token
        logger.info("ContactsApiClient initialized.")

    def add_contact(self, contact_data: dict):
        """Method to add a new contact."""
        logger.info(f"Adding contact: {contact_data}")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.post(
            f"{self.BASE_URL}/contacts",
            json={
                "firstName": contact_data.get("first_name"),
                "lastName": contact_data.get("last_name"),
                "birthdate": contact_data.get("birthdate"),
                "email": contact_data.get("email"),
                "phone": contact_data.get("phone"),
                "street1": contact_data.get("street1"),
                "street2": contact_data.get("street2"),
                "city": contact_data.get("city"),
                "stateProvince": contact_data.get("state_province"),
                "postalCode": contact_data.get("postal_code"),
                "country": contact_data.get("country")
            },
            headers=headers
        )
        return response

    def get_contacts(self):
        """Method to get all contacts."""
        logger.info("Getting all contacts.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.BASE_URL}/contacts", headers=headers)
        
        return response

    def get_contact_by_id(self, contact_id):
        """Method to get a contact by ID."""
        logger.info(f"Getting contact with ID: {contact_id}.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.BASE_URL}/contacts/{contact_id}", headers=headers)
        
        return response

    def update_contact(self, contact_id, contact):
        """Method to update an existing contact."""
        logger.info(f"Updating contact with ID: {contact_id}.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        contact_data = {
            "firstName": contact.first_name,
            "lastName": contact.last_name,
            "birthdate": contact.birthdate,
            "email": contact.email,
            "phone": contact.phone,
            "street1": contact.street1,
            "street2": contact.street2,
            "city": contact.city,
            "stateProvince": contact.state_province,
            "postalCode": contact.postal_code,
            "country": contact.country
        }
        
        contact_data = {key: value for key, value in contact_data.items() if value is not None}
        
        response = requests.put(
            f"{self.BASE_URL}/contacts/{contact_id}",
            json=contact_data,
            headers=headers
        )
        
        return response

    def delete_contact(self, contact_id):
        """Method to delete a contact by ID."""
        logger.info(f"Deleting contact with ID: {contact_id}.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.delete(f"{self.BASE_URL}/contacts/{contact_id}", headers=headers)
        
        return response