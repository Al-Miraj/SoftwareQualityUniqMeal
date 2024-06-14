# from InputChecker import InputChecker
from Roles.User import User
from Roles.Member import Member
from Roles.Consultant import Consultant
from Roles.SystemAdmin import SystemAdmin
from Roles.SuperAdmin import SuperAdmin
from Database import DBConfig, DBConnectionManager
from Database.DataAccesObjects.UsersDAO import UsersDAO

import sqlite3
import os
import sys


def read_json_file(filename) -> list:  # buiten class?

    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as file:

        contents = json.load(file)
    return contents


if __name__ == "__main__":
    dbFile = DBConfig.DBConfig.DBFile
    DCMobj = DBConnectionManager.DCM(dbFile)
    DCMobj.connect()
    conn = DCMobj.conn
    cursor = conn.cursor()
    #enter your code here :)

    userDAO = UsersD


