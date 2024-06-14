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

    return SystemAdmin.AddNewConsultant(username, password, firstName, lastName)
    #newConsultant = SystemAdmin.AddNewConsultant(username, password, firstName, lastName)
    ##DBConfig.usersDAO.InsertUsers([newConsultant])

    conn.close()












