import os
import sys
import json
import sqlite3

from Roles.Member import Member



#C:\Users\khadi\OneDrive\Documenten\Jaar2_Semester2\Software Quality\SoftwareQualityUniqMeal\UniqueMealDB.db

def get_db_conn(filename):
    db_conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), filename))
    return db_conn


def read_json_file(filename) -> list:  # buiten class?

    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as file:

        contents = json.load(file)
    return contents


def insertMembersIntoMember(members, conn, cursor):
    for member in members:
        memberObj = Member(
            member["FirstName"],
            member["LastName"],
            member["Age"],
            member["Gender"],
            member["Weight"],
            member["Street"],
            member["HouseNumber"],
            member["ZipCode"],
            member["City"],
            member["Email"],
            member["PhoneNumber"]
        )
        memberObj.RegistrationDate = member["RegistrationDate"]
        memberObj.MembershipID = member["MembershipID"]
        
        insertMemberQ = """INSERT OR IGNORE INTO members (MembershipID, FirstName, LastName, Age, Gender, Weight, Street, HouseNumber, ZipCode, City, Email, PhoneNumber, RegistrationDate)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        insertMemberValues = [*memberObj.__dict__.values()]
        cursor.execute(insertMemberQ, insertMemberValues)
        conn.commit()





def main():
    """
    hehehe
    """
    members = read_json_file("members.json")
    conn = get_db_conn("UniqueMealDB.db")
    cursor = conn.cursor()
    deleteMembers(conn, cursor)
    insertMembersIntoMember(members, conn, cursor)

    #write_to_db(data, conn, cursor)
    return None


def deleteMembers(conn, cursor):

    cursor.execute("DELETE FROM members")
    conn.commit()



'''

CREATE TABLE IF NOT EXISTS members (

    MembershipID TEXT PRIMARY KEY,

    FirstName TEXT NOT NULL,

    LastName TEXT NOT NULL,

    Age INTEGER,

    Gender TEXT,

    Weight REAL,

    Street TEXT,

    HouseNumber TEXT,

    ZipCode TEXT,

    City TEXT,

    Email TEXT,

    PhoneNumber TEXT,

    RegistrationDate TEXT
);

'''