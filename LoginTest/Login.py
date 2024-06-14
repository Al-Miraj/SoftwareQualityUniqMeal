# from datetime import datetime
# from CHECK import InputHandler
# # from TRAINER import *
# # from SYSADMIN import *
# # from SUPERADMIN import *
# from LOG import *
# import USER
from ENCRYPT import encrypt
#from util.TESTSQLITE import init_database

import logging
import argon2
import sqlite3
import time
conn = sqlite3.connect('UniqueMealDB.db')
cursor = conn.cursor()

#None or list
def executeQuery(query: str, *args: any) -> list:
  query = query.strip()
  expected_amount_args = query.count("?")
  if (expected_amount_args != len(args)):
      conn != None
  
  for arg in args:
    if type(arg) == str:
      fomatted_arg = "\'" + arg.replace("\'", "\'\'") + "\'"
      query = query.replace("?", fomatted_arg, 1)
    else:
      query = query.replace("?", str(arg), 1)
    
  cursor.execute(query)
  
  if query[0:6].upper() == "SELECT":
    result = cursor.fetchall()
    for row in result:
      for field in row:
        if type(field) == str:
          field = field.replace("\'\'", "\'")
    return result
  
  else:
    # Commit the changes to the database
    conn.commit()




def Login(role):
    # print(" ___________________________________________________________________________________________________________")
    # print("|                                                                                                           |")
    # print("|     __    __    __    ________    __          __________    ___________    ______________    ________     |")
    # print("|    |  |  |  |  |  |  |   _____|  |  |        |   _______|  |   _____   |  |   __    __   |  |   _____|    |")
    # print("|    |  |  |  |  |  |  |  |_____   |  |        |  |          |  |     |  |  |  |  |  |  |  |  |  |_____     |")
    # print("|    |  |  |  |  |  |  |   _____|  |  |        |  |          |  |     |  |  |  |  |  |  |  |  |   _____|    |")
    # print("|    |  |__|  |__|  |  |  |_____   |  |_____   |  |_______   |  |_____|  |  |  |  |  |  |  |  |  |_____     |")
    # print("|    |______________|  |________|  |________|  |__________|  |___________|  |__|  |__|  |__|  |________|    |")
    # print("|                                                                                                           |")
    # print(" ___________________________________________________________________________________________________________")
    # print("\n")


    searchUserName = input("Enter your username: ")
    searchPassword = input("Enter your password: ")
    hashed_password = argon2.hash_password(searchPassword.encode())
    login_user = executeQuery("SELECT * FROM users WHERE Username = ? AND Role = ?", encrypt(searchUserName), encrypt(role))


    CheckUser(searchUserName, searchPassword)
    

def CheckUser(userName, passWord):
    if userName == "super_admin" and passWord == "Admin_123?":
        AdminPage()
    

    else:
        print("Sadd")


def AdminPage():
    print("Admin Page")

if __name__ == "__main__":
    Login()
