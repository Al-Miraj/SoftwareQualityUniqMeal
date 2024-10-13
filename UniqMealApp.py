from Database.DBConfig import DBConfig
from CryptUtils.CryptoManager import encrypt, decrypt
from CryptUtils.argon import ph
from Roles.SuperAdmin import SuperAdmin
from Roles.Member import Member, datetime
from Login import Login
from Backup import Backup



def CreateMemberObj(fetchedMember):
    id_ = decrypt(fetchedMember[0])
    FirstName  = decrypt(fetchedMember[1])
    LastName  = decrypt(fetchedMember[2])
    Age = decrypt(fetchedMember[3])
    Gender  = decrypt(fetchedMember[4])
    Weight   = decrypt(fetchedMember[5])
    Street      = decrypt(fetchedMember[6])
    HouseNumber = decrypt(fetchedMember[7])
    zipcode = decrypt(fetchedMember[7])
    city = decrypt(fetchedMember[7])
    email = decrypt(fetchedMember[7])
    phoneNumber = decrypt(fetchedMember[7])
    registrationDate = decrypt(fetchedMember[7])
    obj = Member(FirstName, LastName, Age, Gender, Weight, Street, HouseNumber, zipcode, city, email, phoneNumber, registrationDate)
    obj.MembershipID = id_
    return obj



if __name__ == "__main__":
    print("--start--\n\n")
    
    Login.RunLoginPage()
