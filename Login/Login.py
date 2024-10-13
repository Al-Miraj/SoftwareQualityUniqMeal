from InputHandler.InputHandler import InputHandler
from Database.DBConfig import DBConfig
from CryptUtils.CryptoManager import decrypt
from CryptUtils.argon import ph
from argon2 import exceptions as ex
from Roles.Consultant import Consultant
from Roles.SystemAdmin import SystemAdmin
from Roles.SuperAdmin import SuperAdmin

from . import ConsultantPage
from . import SystemPage
from . import SuperPage

MAX_ATTEMPTS = 3

def DisplayWelcomePage():
    print("Welcome to the Unique Meal Member Management System!")
    print("Press 1. Log in.")
    print("Press 2. Forgot password.")
    print("Press 3. Exit\n")

def DisplayPageDivider():
    print("\n\n###############################################\n")

def validate_username_password(username: str, password: str) -> bool:
    if not InputHandler.checkUsernameFormat(username):
        print("Invalid username format.")
        return False
    if not InputHandler.checkPasswordFormat(password):
        print("Invalid password format.")
        return False
    return True

def CreateUserObj(fetchedUser):
    username  = decrypt(fetchedUser[0])
    password  = decrypt(fetchedUser[1])
    firtsname = decrypt(fetchedUser[2])
    lastname  = decrypt(fetchedUser[3])
    regDate   = decrypt(fetchedUser[4])
    role      = decrypt(fetchedUser[5])
    if role == "SuperAdmin":
        return SuperAdmin(username, password, firtsname, lastname, regDate)
    elif role == "SystemAdmin":
        return SystemAdmin(username, password, firtsname, lastname, regDate)
    elif role == "Consultant":
        return Consultant(username, password, firtsname, lastname, regDate)
    else:
        return None

def handle_login_attempt(usernameInput: str, passwordInput: str):
    fetchedUser = DBConfig.usersDAO.SelectUser(usernameInput)
    if not fetchedUser:
        print("User not found.")
        return False

    password  = decrypt(fetchedUser[1])
    try:
        ph.verify(password, usernameInput + passwordInput)
        userObj = CreateUserObj(fetchedUser)
        if userObj == None:
                print("Something went Wrong. Could not determine user role.")
                return None
        print("Logged in.")
        return userObj
    except (ex.VerifyMismatchError, ex.VerificationError):
        print("Wrong username or password combination.")
        return None


def RunLoginPage():
    print("-- Log in --\n")
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Username: ")
        password = input("Password: ")

        if validate_username_password(username, password):
            userObj = handle_login_attempt(username, password)
            if userObj == None:
                return False
            else:
                return userObj

        attempts += 1

    print("Too many wrong tries. Incident logged.")
    return False



def main():
    DisplayWelcomePage()

    while (True):
        menuChoice = input("-> ")
        if menuChoice == "1":
            DisplayPageDivider()
            userObj = RunLoginPage()
            if userObj == False:
                break
            if userObj.Role == "SuperAdmin":
                print("now logging in as Super Admin")
                SuperPage.display_menuA(userObj.Username)
            elif userObj.Role == "SystemAdmin":
                print("now logging in as System Admin")
                SystemPage.display_menuB(userObj.Username)
            else:
                print("now logging in as Consultant")
                ConsultantPage.display_menuC(userObj)
            break
        elif menuChoice == "2":
            print("--Not Implemented--\n")
        elif menuChoice == "3":
            return

    




    # WORK ON FORGOT PASSWORD FEATURE