class ContactData:
    """Model for contact data"""
    def __init__(self, first_name, last_name, birthdate, email, phone, street1, street2, city, state_province, postal_code, country):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def to_dict(self):
        """Converts the contact data object to a dictionary for serialization."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "email": self.email,
            "phone": self.phone,
            "street1": self.street1,
            "street2": self.street2,
            "city": self.city,
            "state_province": self.state_province,
            "postal_code": self.postal_code,
            "country": self.country
        }
