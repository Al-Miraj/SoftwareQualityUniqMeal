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



def CheckList():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()

    query = "SELECT Username, Role FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    for user, role in result:
        print(f"Username: {user}, Role: {role}")

    conn.close()

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

    # Use placeholder values for SystemAdmin initialization
    system_admin = SystemAdmin('placeholder_user', 'placeholder_pass', 'placeholder_first', 'placeholder_last')
    system_admin.AddNewConsultant(username, password, firstName, lastName)

    print("Consultant added successfully.")

    conn.close()

def UpdateConsultant():
    updateMenu()
    option = input("Select an option: ")
    handle_optionM(option)

def updateMenu():
    print(
    "Update Menu\n" +
    "1: Update first name \n" +
    "2: Update first name \n" + 
    "3: Update username" 
)
    

# def handle_optionM(option):
#     #fix update in database
#     #add check function
#     if option == '1':
#         updatemem = input("Type the first name of the Consultant you want to update: ")
#         n_name = input("Update first name: ")
#         check_name = InputHandler.checkFirstName(n_name)
#         if InputHandler.error:
#             print(InputHandler.message)
#         else:
#             query = '''UPDATE users set FirstName = ? WHERE First_name = ?'''
#             cursor.execute(query, n_name, updatemem)
#             print("Succesfully updated to:", n_name)
#             conn.commit()
#     elif option == '2':
#         updatemem = input("Type the last name of the Consultant you want to update: ")
#         n_lname = input("Update last name: ")
#         check_lname = InputHandler.checkLastName(n_lname)
#         if InputHandler.error:
#             print(InputHandler.message)
#         else:
#             query = '''UPDATE users SET LastName = ? WHERE LastName = ?'''
#             cursor.execute(query, n_lname, updatemem)
#             print("Succesfully updated to:", n_lname)
#             conn.commit()
#     elif option == '3':
#         updtatemem = input("Type the username of the Consultant you want to update")
#         n_username = input("Update username: ")
#         #input handeler
#         query = '''UPDATE users SET Username = ? WHERE Username = ?'''
#         cursor.execute(query, n_lname, updatemem)
#         print("Succesfully updated to:", n_username)
#         conn.commit()

def Deleteconsultant():
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()
    
    # Prompt user for the username of the consultant to delete
    username = input("Enter the username of the consultant you want to delete: ")
    
    try:
        # Execute the delete operation based on username
        cursor.execute('''DELETE FROM users WHERE UserName = ?''', (username,))
        
        # Check if any row was affected
        if cursor.rowcount == 1:
            print(f"Successfully deleted consultant {username}")
        else:
            print(f"Consultant {username} not found or unable to delete.")
            
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any errors that occur during the deletion process
        print(f"Error deleting consultant: {str(e)}")
    
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
        
        
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error resetting password: {str(e)}")
    
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

    # Use placeholder values for SystemAdmin initialization
    super_admin = SuperAdmin('placeholder_user', 'placeholder_pass', 'placeholder_first', 'placeholder_last')
    super_admin.AddNewSystemAdmin(username, password, firstName, lastName)

    print("Admin added successfully.")

    conn.close()
