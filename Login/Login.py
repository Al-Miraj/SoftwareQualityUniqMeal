import logging
import os
import sqlite3
from .ConsultantPage import ConsultantPage

from argon2 import PasswordHasher

# # Initialize the password hasher
ph = PasswordHasher()

# Initialize SQLite database connection
conn = sqlite3.connect('Database\\UniqueMealDB.db')
cursor = conn.cursor()



def executeQuery(query, *args):
    print("HI")

    cursor.execute(query, args)
    
    if query.strip().upper().startswith('SELECT'):
        return cursor.fetchone()
    else:
        conn.commit()

def login(role):
    searchUsername = input("Enter username: ")
    searchPassword = input("Enter password: ")

    try:
        # Retrieve user from database
        login_user = executeQuery("SELECT * FROM users WHERE Username = ? AND Role = ?", searchUsername, role)

        if login_user:
            # Retrieve stored hashed password
            stored_hash = login_user[0][1]  # Adjust based on your database schema
            # Verify password attempt
            try:
                print(ph.verify(stored_hash, searchPassword))
                logging.info(f"Successful login attempt for {searchUsername}.")
                print("Login successful.")
                print("* " * 20)
                print("* " * 20)
                return True
            except exceptions.VerifyMismatchError:
                logging.info(f"Failed login attempt for {searchUsername}.")
                print("Login incorrect.")
                print("Invalid username/password combination. Please try again.")
                return False
        else:
            logging.info(f"User {searchUsername} does not exist.")
            print("Invalid username/password combination. Please try again.")
            return False

    except Exception as e:
        logging.error(f"Error during login: {str(e)}")
        print(f"Error during login: {str(e)}")
        return False

def display_menu():
    print("Welcome to the ... ")
    print("Press 1. Log in as Super Administrator")
    print("Press 2. Log in as System Administrator")
    print("Press 3. Log in as Consultant")
    print("Press 4. Exit")

def handle_option(option):
    if option == '1':
        print("You selected Log in as Super Administrator.")
        if login("SuperAdmin"):
            # Call function for Super Admin
            mainSuper()
    elif option == '2':
        print("You selected Log in as System Administrator.")
        if login("SystemAdmin"):
            # Call function for System Admin
            mainAdmin()
    elif option == '3':
        print("You selected Log in as Consultant.")
        if login("Consultant"):
            # Call function for Consultant
            mainConsultant()
    elif option == '4':
        print("* " * 20)
        print("Exiting...")
        print("* " * 20)
        return False
    else:
        print("Invalid option. Please try again.")

def mainSuper():
    print("Welcome, Super Administrator!")
    #Roles\\SuperAdmin()
    # Call function for Super Admin

def mainAdmin():
    print("Welcome, System Administrator!")
    #Roles\\SystemAdmin()
    # Call function for System Admin

def mainConsultant():
    print("Welcome, Consultant!")
    #Roles\\Consultant()
    display_menuA()
    user_input = input("Select an option: ")
    handle_optionA(user_input)

def Loginmain():

    # Initialize logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("Application started.")

    # Loop for displaying menu and handling user input
    while True:
        display_menu()
        option = input("Select an option: ")
        logging.info(f"User selected option {option}.")
        if not handle_option(option):
            break

    # Close database connection
    conn.close()
    logging.info("Application exited.")


