class UserData:
    """Model for user data."""
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
