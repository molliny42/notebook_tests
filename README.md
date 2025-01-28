**README.md (English version)**:

# Automated Tests for Contact List API

This project contains automated tests for the Contact List API. The tests use pytest to check various operations in the application.

- Application: [Thinking Tester Contact List](https://thinking-tester-contact-list.herokuapp.com/)
- API Documentation: [Postman API](https://documenter.getpostman.com/view/4012288/TzK2bEa8)  

---

## Tests for Users API

### Positive:
- **Check the full user lifecycle**  
  Steps:
  1. Login with a test user
  2. Create a new user
  3. Logout the current user
  4. Login with the new user
  5. Get the profile of the new user
  6. Delete the new user
  7. Check that the deleted user cannot log in

### Negative:
1. **Login with wrong data**
2. **Add an existing user**

---

## Tests for Contacts API

### Positive:
1. **Add a contact**
2. **Get all contacts**
3. **Get a contact by ID**
4. **Delete a contact**
5. **Update a contact**

### Negative:
1. **Add a contact without a first name**
2. **Add a contact without a last name**
3. **Get a non-existing contact**
4. **Delete a non-existing contact**

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/molliny42/notebook_tests.git
   ```

2. Go to the project directory:
   ```bash
   cd notebook_tests
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the environment:
   - For Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

1. Run the tests:
   ```bash
   pytest tests/
   ```

2. To generate a report in HTML using Allure:

   - Run the tests with the Allure parameter:
     ```bash
     pytest --alluredir=allure-results
     ```

   - After the tests finish, to view the HTML report:
     ```bash
     allure serve allure-results
     ```

   More information about Allure: [official Allure website](https://allure.qatools.ru/).

---

## Logging

Test logs are located in the `logs/` folder.