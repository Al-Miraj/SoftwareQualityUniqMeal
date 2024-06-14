from . import ConsultantPage
from . import SystemPage
from . import SuperPage
from Roles.Consultant import Consultant
from Roles.SystemAdmin import SystemAdmin
from Roles.SuperAdmin import SuperAdmin
from Database.DBConfig import DBConfig
import sqlite3



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



















