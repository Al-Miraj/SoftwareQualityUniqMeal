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
from Login import Login
from Login import InputDef

import sqlite3
import os
import sys


def read_json_file(filename) -> list:  # buiten class?

    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as file:

        contents = json.load(file)
    return contents


if __name__ == "__main__":
    Login.Loginmain()
    #InputDef.ResetconsultantPassword()