import logging
import os
import sqlite3
from Database.DBConfig import DBConfig
from . import ConsultantPage
from . import SystemPage
from . import SuperPage

ph = DBConfig.ph

# Initialize SQLite database connection
conn = DBConfig.dcm.conn
cursor = conn.cursor()



def executeQuery(query, *args):
    cursor.execute(query, args)
    
    if query.strip().upper().startswith('SELECT'):
        return cursor.fetchone()
    else:
        conn.commit()

def login(role):
    searchUsername = input("Enter username: ")
    searchPassword = input("Enter password: ")
    print()

    try:
        # Retrieve user from database
        login_user = executeQuery("SELECT * FROM users WHERE Username = ? AND Role = ?", searchUsername, role)
        

        if login_user:
            # Retrieve stored hashed password
            stored_hash = login_user[1]  # Adjust based on your database schema

            # Verify password attempt
            try:
                print(ph.verify(stored_hash, searchUsername+searchPassword))
                logging.info(f"Successful login attempt for {searchUsername}.")
                print("Login successful.")
                print("* " * 20)
                print("* " * 20)
                return True, searchPassword, searchUsername
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
    choice = int(print("Press 4. Exit"))
    handle_option(choice)

def handle_option(option):
    if option == '1':
        print("You selected Log in as Super Administrator.\n")
        if login("SuperAdmin"):
            print("Welcome, Super Administrator!")
            SuperPage.display_menuA()
            user_input = input("Select an option: ")
            SuperPage.handle_optionA(user_input)


    elif option == '2':
        print("You selected Log in as System Administrator.")
        if login("SystemAdmin"):
            print("Welcome, System Administrator!")
            print()
            SystemPage.display_menuB()
            user_input = input("Select an option: ")
            SystemPage.handle_optionB(user_input)

    
    elif option == '3':
        print("You selected Log in as Consultant.")
        if login("Consultant"):
            print("Welcome, Consultant!")
            ConsultantPage.display_menuC()
            user_input = input("Select an option: ")
            ConsultantPage.handle_optionC(user_input)
    
    elif option == '4':
        print("* " * 20)
        print("Exiting...")
        print("* " * 20)
        return False
    
    else:
        print("Invalid option. Please try again.")
    

def Loginmain():

    # Initialize logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("Application started.")

    # Loop for displaying menu and handling user input
    while True:
        display_menu()
        option = input("Select an option: ")
        logging.info(f"User selected option {option}.\n")
        if not handle_option(option):
            break

    # Close database connection
    DBConfig.dcm.disconnect()
    logging.info("Application exited.")


