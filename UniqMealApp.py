# from InputChecker import InputChecker
from Roles.User import User
from Roles.Member import Member
from Roles.Consultant import Consultant
from Roles.SystemAdmin import SystemAdmin
from Roles.SuperAdmin import SuperAdmin
from Database.DBConfig import DBConfig
from Database.DataAccesObjects.UsersDAO import UsersDAO
from Database.DataAccesObjects.MembersDAO import MembersDAO
from InputHandler.InputHandler import InputHandler
#from Login import Login
from Login import InputDef

import sqlite3
import os
import sys


def read_json_file(filename) -> list:  # buiten class?

    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as file:

        contents = json.load(file)
    return contents


if __name__ == "__main__":
    print("\n================USERNAME================")
    print(InputHandler.checkUsernameFormat("6"))
    print()
    print(InputHandler.checkUsernameFormat("Tqwer%yuio"))
    print()
    print(InputHandler.checkUsernameFormat(".sdfghytuj"))
    print()
    print(InputHandler.checkUsernameFormat("_asdfghjkoiu"))
    print()
    print(InputHandler.checkUsernameFormat("_asdfghjk"))
    print("============================\n")

    # Password tests
    print("\n================PASSWORD================")
    print(InputHandler.checkPasswordFormat("aS6!"))
    print()
    print(InputHandler.checkPasswordFormat("aaaaaaaaaaaa"))
    print()
    print(InputHandler.checkPasswordFormat("aS6!ghytghyt^"))
    print()
    print(InputHandler.checkPasswordFormat("aS6!ghytghytghytghytghytghytghyt"))
    print()
    print(InputHandler.checkPasswordFormat("aS6!ghytghyt"))
    print("============================\n")

    # First Name tests
    print("\n================FIRSTNAME================")
    print(InputHandler.checkFirstName(""))
    print()
    print(InputHandler.checkFirstName("aaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print()
    print(InputHandler.checkFirstName("Khadija$"))
    print()
    print(InputHandler.checkFirstName("Khadija-"))
    print("============================\n")

    # Last Name tests
    print("\n================LASTNAME================")
    print(InputHandler.checkLastName(""))
    print()
    print(InputHandler.checkLastName("aaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print()
    print(InputHandler.checkLastName("Khadija$"))
    print()
    print(InputHandler.checkLastName("Kh-adi ja'"))
    print("============================\n")

    # Email tests
    print("\n================EMAIL================")
    print(InputHandler.checkEmailFormat(""))
    print()
    print(InputHandler.checkEmailFormat("a@b"))
    print()
    print(InputHandler.checkEmailFormat("a@b.com"))
    print()
    print(InputHandler.checkEmailFormat("name@domain.subdomain.com"))
    print()
    print(InputHandler.checkEmailFormat("name@domain..com"))
    print()
    print(InputHandler.checkEmailFormat("name@domain-.com"))
    print()
    print(InputHandler.checkEmailFormat("name@-domain.com"))
    print()
    print(InputHandler.checkEmailFormat(".name@domain.com"))
    print()
    print(InputHandler.checkEmailFormat("name@domain.com."))
    print()
    print(InputHandler.checkEmailFormat("name@domain"))
    print("============================\n")

    # Age tests
    print("\n================AGE================")
    print(InputHandler.checkAgeFormat("17"))
    print()
    print(InputHandler.checkAgeFormat("18"))
    print()
    print(InputHandler.checkAgeFormat("130"))
    print()
    print(InputHandler.checkAgeFormat("131"))
    print()
    print(InputHandler.checkAgeFormat("abc"))
    print()
    print(InputHandler.checkAgeFormat("21.5"))
    print("============================\n")

    # Gender tests
    print("\n================GENDER================")
    print(InputHandler.checkGenderFormat("M"))
    print()
    print(InputHandler.checkGenderFormat("F"))
    print()
    print(InputHandler.checkGenderFormat("m"))
    print()
    print(InputHandler.checkGenderFormat("X"))
    print()
    print(InputHandler.checkGenderFormat("Male"))
    print("============================\n")

    # Weight tests
    print("\n================WEIGHT================")
    print(InputHandler.checkWeightFormat("60"))
    print()
    print(InputHandler.checkWeightFormat("60.5"))
    print()
    print(InputHandler.checkWeightFormat("abc"))
    print()
    print(InputHandler.checkWeightFormat("60kg"))
    print()
    print(InputHandler.checkWeightFormat("60.56"))
    print("============================\n")

    # Street tests
    print("\n================STREET================")
    print(InputHandler.checkStreetFormat(""))
    print()
    print(InputHandler.checkStreetFormat("Main Street"))
    print()
    print(InputHandler.checkStreetFormat("123 Main St"))
    print()
    print(InputHandler.checkStreetFormat("Main-Street."))
    print()
    print(InputHandler.checkStreetFormat("Main Street!"))
    print("============================\n")

    # House Number tests
    print("\n================HOUSENUM================")
    print(InputHandler.checkHouseNumberFormat(""))
    print()
    print(InputHandler.checkHouseNumberFormat("123"))
    print()
    print(InputHandler.checkHouseNumberFormat("123a"))
    print()
    print(InputHandler.checkHouseNumberFormat("12345"))
    print()
    print(InputHandler.checkHouseNumberFormat("123456"))
    print()
    print(InputHandler.checkHouseNumberFormat("123@"))
    print("============================\n")

    # Zip Code tests
    print("\n================ZIPCODE================")
    print(InputHandler.checkZipCodeFormat("1234AB"))
    print()
    print(InputHandler.checkZipCodeFormat("1234ABCD"))
    print()
    print(InputHandler.checkZipCodeFormat("12345A"))
    print()
    print(InputHandler.checkZipCodeFormat("1234A"))
    print()
    print(InputHandler.checkZipCodeFormat("123AB"))
    print()
    print(InputHandler.checkZipCodeFormat("12AB"))
    print("============================\n")

    # City tests
    print("\n================CITY================")
    print(InputHandler.checkCityFormat("Amsterdam"))
    print()
    print(InputHandler.checkCityFormat("Rotterdam"))
    print()
    print(InputHandler.checkCityFormat("New York"))
    print()
    print(InputHandler.checkCityFormat("Utrecht"))
    print("============================\n")

    # Phone Number tests
    print("\n================PHONE================")
    print(InputHandler.checkPhoneNumberFormsat("+31-6-12345678"))
    print()
    print(InputHandler.checkPhoneNumberFormsat("31-6-12345678"))
    print()
    print(InputHandler.checkPhoneNumberFormsat("+31612345678"))
    print()
    print(InputHandler.checkPhoneNumberFormsat("+31-6-1234567"))
    print()
    print(InputHandler.checkPhoneNumberFormsat("+31-6-123456789"))
    print()

    print("done")