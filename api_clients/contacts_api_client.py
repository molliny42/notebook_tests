import requests
from logger_config import setup_logger

logger = setup_logger(__name__, "contacts_api_client.log")

class ContactsApiClient:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

    def __init__(self, token=None):
        self.token = token
        logger.info("ContactsApiClient initialized.")

    def add_contact(self, first_name, last_name, birthdate, email, phone, street1, street2, city, state_province, postal_code, country):
        """Method to add a new contact."""
        logger.info(f"Adding contact: {first_name} {last_name}, Email: {email}")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.post(
            f"{self.BASE_URL}/contacts",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "birthdate": birthdate,
                "email": email,
                "phone": phone,
                "street1": street1,
                "street2": street2,
                "city": city,
                "stateProvince": state_province,
                "postalCode": postal_code,
                "country": country
            },
            headers=headers
        )
        
        #  try:
        #     response.raise_for_status()
        # except requests.exceptions.HTTPError as e:
        #     logger.error(f"HTTP error occurred while adding contact: {e}")
        #     raise
        
        # logger.info(f"Contact {first_name} {last_name} added successfully.")
        return response

    def get_contacts(self):
        """Method to get all contacts."""
        logger.info("Getting all contacts.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.BASE_URL}/contacts", headers=headers)
        
        # try:
        #     response.raise_for_status()
        # except requests.exceptions.HTTPError as e:
        #     logger.error(f"HTTP error occurred while getting contacts: {e}")
        #     raise
        
        # logger.info(f"Retrieved {len(response.json())} contacts.")
        return response

    def get_contact_by_id(self, contact_id):
        """Method to get a contact by ID."""
        logger.info(f"Getting contact with ID: {contact_id}.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.BASE_URL}/contacts/{contact_id}", headers=headers)
        
        # try:
        #     response.raise_for_status()
        # except requests.exceptions.HTTPError as e:
        #     logger.error(f"HTTP error occurred while getting contact {contact_id}: {e}")
        #     raise
        
        # logger.info(f"Contact {contact_id} retrieved successfully.")
        return response

    def update_contact(self, contact_id, first_name=None, last_name=None, birthdate=None, email=None, phone=None, street1=None, street2=None, city=None, state_province=None, postal_code=None, country=None):
        """Method to update an existing contact."""
        logger.info(f"Updating contact with ID: {contact_id}.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        contact_data = {
            "firstName": first_name,
            "lastName": last_name,
            "birthdate": birthdate,
            "email": email,
            "phone": phone,
            "street1": street1,
            "street2": street2,
            "city": city,
            "stateProvince": state_province,
            "postalCode": postal_code,
            "country": country
        }
        
        contact_data = {key: value for key, value in contact_data.items() if value is not None}
        
        response = requests.put(
            f"{self.BASE_URL}/contacts/{contact_id}",
            json=contact_data,
            headers=headers
        )
        
        # try:
        #     response.raise_for_status()
        # except requests.exceptions.HTTPError as e:
        #     logger.error(f"HTTP error occurred while updating contact {contact_id}: {e}")
        #     raise
        
        # logger.info(f"Contact {contact_id} updated successfully.")
        return response

    def delete_contact(self, contact_id):
        """Method to delete a contact by ID."""
        logger.info(f"Deleting contact with ID: {contact_id}.")
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.delete(f"{self.BASE_URL}/contacts/{contact_id}", headers=headers)
        
        # try:
        #     response.raise_for_status()
        # except requests.exceptions.HTTPError as e:
        #     logger.error(f"HTTP error occurred while deleting contact {contact_id}: {e}")
        #     raise
        
        # logger.info(f"Contact {contact_id} deleted successfully.")
        return response