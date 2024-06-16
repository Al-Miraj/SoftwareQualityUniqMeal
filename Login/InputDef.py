from . import ConsultantPage
from . import SystemPage
from . import SuperPage
from Roles.Consultant import Consultant
from Roles.SystemAdmin import SystemAdmin
from Roles.SuperAdmin import SuperAdmin
from Database.DBConfig import DBConfig
from InputHandler.InputHandler import InputHandler
import sqlite3
from argon2 import PasswordHasher
from Roles.User import User
from Roles.Member import Member
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet
from CryptUtils.CryptoManager import encrypt, decrypt
import logging

ph = PasswordHasher()

def CheckList():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()

    query = "SELECT Username, Role FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    for user, role in result:
        print(f"Username: {user}, Role: {role}\n")
        input("Press enter to go back.. ")
        break

    logging.info("User printed checklist")

    

def AddConsultant():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    print("Enter the following details to add a new consultant:")
        
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    firstName = input("First Name: ").strip()
    lastName = input("Last Name: ").strip()

    if not username or not password or not firstName or not lastName:
        print("All fields are required. Please try again.")
        return
    
    if not InputHandler.checkUsernameFormat(username) or \
        not InputHandler.checkPasswordFormat(password) or \
        not InputHandler.checkFirstName(firstName) or \
        not InputHandler.checkLastName(lastName):
            return
    
    encrypted_username = encrypt(username)
    hashed_password = ph.hash(password)
    encrypted_firstName = encrypt(firstName)
    encrypted_lastName = encrypt(lastName)

    # Use placeholder values for SystemAdmin initialization
    system_admin = SystemAdmin('placeholder_user', 'placeholder_pass', 'placeholder_first', 'placeholder_last')
    system_admin.AddNewConsultant(encrypted_username, hashed_password, encrypted_firstName, encrypted_lastName)

    print("Consultant added successfully.")

    

def handle_optionM(option):
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    if option == '1':
        updatemem = input("Type the first name of the Consultant you want to update: ")
        n_name = input("Update first name: ")
        check_name = InputHandler.checkFirstName(n_name)
        if InputHandler.error:
            print(InputHandler.message)
        else:
            encrypted_firstName = encrypt(n_name)
            query = '''UPDATE users SET FirstName = ? WHERE FirstName = ?'''
            cursor.execute(query, (encrypted_firstName, updatemem))
            print("Successfully updated to:", n_name)
            logging.info("Successfully updated to:", n_name)
            conn.commit()
    elif option == '2':
        updatemem = input("Type the last name of the Consultant you want to update: ")
        n_lname = input("Update last name: ")
        check_lname = InputHandler.checkLastName(n_lname)
        if InputHandler.error:
            print(InputHandler.message)
        else:
            encrypted_lastName = encrypt(n_lname)
            query = '''UPDATE users SET LastName = ? WHERE LastName = ?'''
            cursor.execute(query, (encrypted_lastName, updatemem))
            print("Successfully updated to:", n_lname)
            logging.info("Successfully updated to:", n_lname)
            conn.commit()
    elif option == '3':
        updatemem = input("Type the username of the Consultant you want to update: ")
        n_username = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            encrypted_userName = encrypt(n_lname)
            query = '''UPDATE users SET Username = ? WHERE Username = ?'''
            cursor.execute(query, (encrypted_userName, updatemem))
            print("Successfully updated to:", n_username)
            logging.info("Successfully updated to:", n_username)
            conn.commit()

def Deleteconsultant():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    # Prompt user for the username of the consultant to delete
    username = input("Enter the username of the consultant you want to delete: ")
    
    try:
        # Execute the delete operation based on username
        cursor.execute('''DELETE FROM users WHERE UserName = ?''', (username))
        
        # Check if any row was affected
        if cursor.rowcount == 1:
            print(f"Successfully deleted consultant {username}")
            logging.info(f"Successfully deleted consultant {username}")
        else:
            print(f"Consultant {username} not found or unable to delete.")
            logging.info(f"Consultant {username} not found or unable to delete.")
            
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any errors that occur during the deletion process
        print(f"Error deleting consultant: {str(e)}")
        logging.info(f"Error deleting consultant: {str(e)}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()



def ResetconsultantPassword():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    ph = PasswordHasher()

    try:
        username = input("Enter the username of the consultant whose password you want to reset: ")

        # Check if the user exists
        consToResetPW = DBConfig.usersDAO.SelectUser(username)
        if not consToResetPW:
            print(f"Consultant {username} not found.")
            return
        
        n_password = input("New password: ")

        # Check password format using InputHandler
        if not InputHandler.checkPasswordFormat(n_password):
            print(InputHandler.message)
            return

        # Hash the new password
        hashed_password = ph.hash(n_password)

        # Update the user's password in the database
        DBConfig.usersDAO.UpdateUserPassword(username, consToResetPW[1], hashed_password)
        print(f"Successfully updated password for: {username}")
        logging.info(f"Successfully updated password for: {username}")
        
        
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error resetting password: {str(e)}")
        logging.info(f"Error resetting password: {str(e)}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def AddSystemAdmin():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    print("Enter the following details to add a new admin:")
        
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    firstName = input("First Name: ").strip()
    lastName = input("Last Name: ").strip()

    if not username or not password or not firstName or not lastName:
        print("All fields are required. Please try again.")
        return
    
    if not InputHandler.checkUsernameFormat(username) or \
        not InputHandler.checkPasswordFormat(password) or \
        not InputHandler.checkFirstName(firstName) or \
        not InputHandler.checkLastName(lastName):
            return
    
    encrypted_username = encrypt(username)
    hashed_password = ph.hash(password)
    encrypted_firstName = encrypt(firstName)
    encrypted_lastName = encrypt(lastName)

    # Use placeholder values for SystemAdmin initialization
    super_admin = SuperAdmin('placeholder_user', 'placeholder_pass', 'placeholder_first', 'placeholder_last')
    super_admin.AddNewSystemAdmin(encrypted_username, hashed_password, encrypted_firstName, encrypted_lastName)

    print("Admin added successfully.")
    logging.info("Admin added successfully.")

    conn.close()



def UpdateSystemAdmin():
    updateMenu1()
    option = input("Select an option: ")
    handle_optionA(option)

def updateMenu1():
    print(
    "Update Menu\n" +
    "1: Update first name \n" +
    "2: Update lastName name \n" + 
    "3: Update username" 
)
    

def handle_optionA(option):
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    if option == '1':
        updatemem = input("Type the first name of the Admin you want to update: ")
        n_name = input("Update first name: ")
        check_name = InputHandler.checkFirstName(n_name)
        if InputHandler.error:
            print(InputHandler.message)
        else:
            encrypted_username = encrypt(n_name)
            query = '''UPDATE users SET FirstName = ? WHERE FirstName = ?'''
            cursor.execute(query, (encrypted_username, updatemem))
            print("Successfully updated to:", n_name)
            logging.info("Admin first name updated successfully.")
            conn.commit()
    elif option == '2':
        updatemem = input("Type the last name of the Admin you want to update: ")
        n_lname = input("Update last name: ")
        check_lname = InputHandler.checkLastName(n_lname)
        if InputHandler.error:
            print(InputHandler.message)
        else:
            encrypted_lastName = encrypt(n_lname)
            query = '''UPDATE users SET LastName = ? WHERE LastName = ?'''
            cursor.execute(query, (encrypted_lastName, updatemem))
            print("Successfully updated to:", n_lname)
            logging.info("Admin last name updated successfully.")
            conn.commit()
    elif option == '3':
        updatemem = input("Type the username of the Admin you want to update: ")
        n_username = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            encrypted_username = encrypt(n_username)
            query = '''UPDATE users SET Username = ? WHERE Username = ?'''
            cursor.execute(query, (encrypted_username, updatemem))
            print("Successfully updated to:", n_username)
            logging.info("Admin username updated successfully.")
            conn.commit()




def DeleteSystemAdmin():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    # Prompt user for the username of the consultant to delete
    username = input("Enter the username of the admin you want to delete: ")
    
    try:
        # Execute the delete operation based on username
        cursor.execute('''DELETE FROM users WHERE UserName = ?''', (username,))
        
        # Check if any row was affected
        if cursor.rowcount == 1:
            print(f"Successfully deleted Systemadmin {username}")
            logging.info(f"Systemadmin {username} deleted successfully.")
        else:
            print(f"SystemAdmin {username} not found or unable to delete.")
            logging.info(f"SystemAdmin {username} not found or unable to delete.")
            
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any errors that occur during the deletion process
        print(f"Error deleting admin: {str(e)}")
        logging.info(f"Error deleting admin: {str(e)}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()




def ResetadminPassword():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    ph = PasswordHasher()

    try:
        username = input("Enter the username of the consultant whose password you want to reset: ")

        # Check if the user exists
        systAdminToResetPW = DBConfig.usersDAO.SelectUser(username)
        if not systAdminToResetPW:
            print(f"admin {username} not found.")
            return
        
        n_password = input("New password: ")

        # Check password format using InputHandler
        if not InputHandler.checkPasswordFormat(n_password):
            print(InputHandler.message)
            return

        # Hash the new password
        hashed_password = ph.hash(n_password)

        # Update the user's password in the database
        DBConfig.usersDAO.UpdateUserPassword(username, systAdminToResetPW[1], hashed_password)
        print(f"Successfully updated password for: {username}")
        logging.info(f"Password updated for: {username}")
        
        
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error resetting password: {str(e)}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def AddMember():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    print("Enter the following details to add a new Member")
        
    firstName = input("First Name: ").strip()
    lastName = input("Last Name: ").strip()
    age = int(input("Age: ").strip())
    gender = input("Gender:").strip()
    weight = int(input("weight:"))
    street = input("Street: ").strip()
    houseNumber = int(input("House Number: ").strip())
    zipCode = input("Zip Code: ").strip()
    city = input("City: ").strip()
    email = input("Email: ").strip()
    phoneNumber = input("Phone Number: ").strip()



    if not firstName or not lastName or not age or not gender or not weight or not street or not houseNumber or not zipCode or not city or not email or not phoneNumber:
        print("All fields are required. Please try again.")
        return
    
    

    newMember = Member(firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber)
    DBConfig.membersDAO.InsertMembers([newMember])

    print("Member added successfully.")
    logging.info("Member added successfully.")

    conn.close()


def UpdateMember():
    updateMenu2()
    option = input("Select an option: ")
    handle_option2(option)

def updateMenu2():
    print(
    "Update Menu\n" +
    "1: Update first name \n" +
    "2: Update Last name \n" + 
    "3: Update age \n" + 
    "4: Update Gender \n" + 
    "5: Update Weight \n" + 
    "6: Update Street \n" + 
    "7: Update House Number \n" + 
    "8: Update Zip Code \n" + 
    "9: Update City \n" + 
    "10: Update Email adress \n" + 
    "11: Update Phone number"

)

def handle_option2(option):
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    if option == '1':
        updatemem = input("Type the first name of the Admin you want to update: ")
        n_name = input("Update first name: ")
        check_name = InputHandler.checkFirstName(n_name)
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET FirstName = ? WHERE FirstName = ?'''
            cursor.execute(query, (n_name, updatemem))
            print("Successfully updated to:", n_name)
            conn.commit()
    elif option == '2':
        updatemem = input("Type the last name of the Admin you want to update: ")
        n_lname = input("Update last name: ")
        check_lname = InputHandler.checkLastName(n_lname)
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET LastName = ? WHERE LastName = ?'''
            cursor.execute(query, (n_lname, updatemem))
            print("Successfully updated to:", n_lname)
            conn.commit()
    elif option == '3':
        updatemem = input("Type the age of the member you want to update: ")
        age1 = input("Update age: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET Age = ? WHERE Age = ?'''
            cursor.execute(query, (age1, updatemem))
            print("Successfully updated to:", age1)
            conn.commit()

    elif option == '4':
        updatemem = input("Type the gender you want to update: ")
        gender1 = input("Update gender: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET Gender = ? WHERE Gender = ?'''
            cursor.execute(query, (gender1, updatemem))
            print("Successfully updated to:", gender1)
            conn.commit()

    elif option == '5':
        updatemem = input("Type the weight you want to update: ")
        weight1 = input("Update weight: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET Weight = ? WHERE Weight = ?'''
            cursor.execute(query, (weight1, updatemem))
            print("Successfully updated to:", weight1)
            conn.commit()

    elif option == '6':
        updatemem = input("Type the Street you want to update: ")
        street1 = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET Street = ? WHERE Street = ?'''
            cursor.execute(query, (street1, updatemem))
            print("Successfully updated to:", street1)
            conn.commit()

    elif option == '7':
        updatemem = input("Type the house number you want to update: ")
        house1 = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET HouseNumber = ? WHERE HouseNumber = ?'''
            cursor.execute(query, (house1, updatemem))
            print("Successfully updated to:", house1)
            conn.commit()

    elif option == '8':
        updatemem = input("Type the Zipcode you want to update: ")
        zipcode1 = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET ZipCode = ? WHERE ZipCode = ?'''
            cursor.execute(query, (zipcode1, updatemem))
            print("Successfully updated to:", zipcode1)
            conn.commit()

    
    elif option == '9':
        updatemem = input("Type the city you want to update: ")
        city1 = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET City = ? WHERE City = ?'''
            cursor.execute(query, (City, updatemem))
            print("Successfully updated to:", City)
            conn.commit()


    elif option == '10':
        updatemem = input("Type the Email you want to update: ")
        email1 = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET EmailAdress = ? WHERE EmailAdress = ?'''
            cursor.execute(query, (email1, updatemem))
            print("Successfully updated to:", email1)
            conn.commit()

    elif option == '11':
        updatemem = input("Type the phone you want to update: ")
        phone1 = input("Update username: ")
        if InputHandler.error:
            print(InputHandler.message)
        else:
            query = '''UPDATE users SET PhoneNumber = ? WHERE PhoneNumber = ?'''
            cursor.execute(query, (phone1, updatemem))
            print("Successfully updated to:", phone1)
            conn.commit()




    




def Deletemember():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    # Prompt user for the username of the consultant to delete
    First_name = input("Enter the first name of the member you want to delete: ")
    Last_name = input("Enter the Last name of the member you want to delete:  ")

    
    try:
        # Execute the delete operation based on username
        cursor.execute('''DELETE FROM members WHERE FirstName = ? AND LastName = ? ''', (First_name, Last_name ))
        
        # Check if any row was affected
        if cursor.rowcount == 1:
            print(f"Successfully deleted Member {First_name} + {Last_name}")
        else:
            print(f"Member {First_name} not found or unable to delete.")
            
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any errors that occur during the deletion process
        print(f"Error deleting : {str(e)}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()






def searchMember(search_key='all'):
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()

    print("Searching for member....")
    search_input = input("Type (partial) member information: ").lower()

    if search_key == 'all':
        search_key_list = ['memberID', 'firstName', 'lastName', 'age', 'gender', 'weight', 'street', 'houseNumber', 'zipCode', 'city', 'email', 'phoneNumber']
    else:
        search_key_list = [search_key]

    cursor.execute(''' SELECT * FROM members ''')
    records = cursor.fetchall()
    total_found = 0
    for row in records:
        search = False
        for key in search_key_list:
            if key == 'memberID':
                field_value = str(row[0]).lower()
            elif key == 'firstName':
                field_value = str(row[1]).lower()
            elif key == 'lastName':
                field_value = str(row[2]).lower()
            elif key == 'age':
                field_value = str(row[3]).lower()
            elif key == 'gender':
                field_value = str(row[4]).lower()
            elif key == 'weight':
                field_value = str(row[5]).lower()
            elif key == 'street':
                field_value = str(row[5]).lower()
            elif key == 'houseNumber':
                field_value = str(row[6]).lower()
            elif key == 'zipCode':
                field_value = str(row[7]).lower()
            elif key == 'city':
                field_value = str(row[8]).lower()
            elif key == 'email':
                field_value = str(row[9]).lower()
            elif key == 'phoneNumber':
                field_value = str(row[10]).lower()

            if search_input in field_value:
                search = True
                break

        if search:
            print(f"Found match: {search_input} in {key} - {field_value}")
            print(row)
            total_found += 1

    print(f"Total members found: {total_found}")

    cursor.close()
    conn.close()




def PasswordRenew():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    ph = PasswordHasher()

    try:
        username = input("Enter the username to reset: ")

        # Check if the user exists
        consToResetPW = DBConfig.usersDAO.SelectUser(username)
        if not consToResetPW:
            print(f"Consultant {username} not found.")
            return

        # Debug: Print the stored password hash
        stored_password = consToResetPW[1]  # assuming the password is stored in the 2nd column
        print(f"Stored password hash: {stored_password}")


        # If the old password is correct, ask for the new password
        n_password = input("New password: ")

        # Check password format using InputHandler
        if not InputHandler.checkPasswordFormat(n_password):
            print(InputHandler.message)
            return

        # Hash the new password
        hashed_password = ph.hash(n_password)

        # Update the user's password in the database
        DBConfig.usersDAO.UpdateUserPassword(username, consToResetPW[1], hashed_password)
        print(f"Successfully updated password for: {username}")

        # Commit the transaction
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()