from .DataAccesObjects.MembersDAO import MembersDAO
from .DataAccesObjects.UsersDAO import UsersDAO
from .DBConnectionManager import DCM
from JsonFileHandler.JsonFileHandler import JsonFileHandler
from CryptUtils.CryptoManager import encrypt, decrypt
from Roles.Member import Member
from Roles.User import User
from CryptUtils.argon import ph
#works like a static class
class DBConfig:
    DBName = "UniqueMealDB"
    DBFile = "UniqueMealDB.db"
    DBPath = "Database\\UniqueMealDB.db" #"SoftwareQualityUniqMeal\\Database\\UniqueMealDB.db"
    membersJsonPath = "Database\\Data\\members.json"
    usersJsonPath = "Database\\Data\\users.json"
    dcm = DCM(DBFile)
    dcm.connect()
    usersDAO = UsersDAO(dcm.conn)
    membersDAO = MembersDAO(dcm.conn)


    def hi():
        return True


    def ResetMembers():
        DBConfig.EmptyMembers()
        DBConfig.FillMembers()
    
    def ResetUsers():
        DBConfig.EmptyUsers()
        DBConfig.FillUsers()

    def EmptyMembers():
        cursor = DBConfig.dcm.conn.cursor()
        cursor.execute("DELETE FROM members")
        DBConfig.dcm.conn.commit()
        cursor.close()
    
    def EmptyUsers():
        cursor = DBConfig.dcm.conn.cursor()
        cursor.execute("DELETE FROM users")
        DBConfig.dcm.conn.commit()
        cursor.close()
    
    def FillMembers():
        members = JsonFileHandler.ReadJsonFile(DBConfig.membersJsonPath)
        cursor = DBConfig.dcm.conn
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
            insertMemberValues = [encrypt(memberObj.MembershipID),
                                  encrypt(memberObj.FirstName),
                                  encrypt(memberObj.LastName),
                                  encrypt(str(memberObj.Age)),
                                  encrypt(memberObj.Gender),
                                  encrypt(str(memberObj.Weight)),
                                  encrypt(memberObj.Street),
                                  encrypt(memberObj.HouseNumber),
                                  encrypt(memberObj.ZipCode),
                                  encrypt(memberObj.City),
                                  encrypt(memberObj.Email),
                                  encrypt(memberObj.PhoneNumber),
                                  encrypt(memberObj.RegistrationDate)]
            cursor.execute(insertMemberQ, insertMemberValues)
        DBConfig.dcm.conn.commit()
    
    def FillUsers():
        users = JsonFileHandler.ReadJsonFile(DBConfig.usersJsonPath)
        cursor = DBConfig.dcm.conn
        for user in users:
            userObj = User(
                user["Username"],
                user["Password"],
                user["FirstName"],
                user["LastName"],
                user["RegistrationDate"]
            )
            userObj.Role = user["Role"]
            
            insertUsersQ = """INSERT OR IGNORE INTO users (Username, Password, FirstName, LastName, RegistrationDate, Role)
                            VALUES (?, ?, ?, ?, ?, ?)"""
            insertUsersValues = [encrypt(userObj.Username), 
                                 encrypt(ph.hash(userObj.Username + userObj.Password)), 
                                 encrypt(userObj.FirstName), 
                                 encrypt(userObj.LastName), 
                                 encrypt(userObj.RegistrationDate), 
                                 encrypt(userObj.Role)]
            cursor.execute(insertUsersQ, insertUsersValues)
        DBConfig.dcm.conn.commit()


    def createTable():
        query = """
CREATE TABLE IF NOT EXISTS members (
    MembershipID TEXT REQUIRED KEY,
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
);"""