# from InputChecker import InputChecker
from Roles.User import User
from Roles.Member import Member
from Roles.Consultant import Consultant
from Roles.SystemAdmin import SystemAdmin
from Roles.SuperAdmin import SuperAdmin
from Database.DBConfig import DBConfig
from Database.DataAccesObjects.UsersDAO import UsersDAO
from Database.DataAccesObjects.MembersDAO import MembersDAO

import sqlite3
import os
import sys


def read_json_file(filename) -> list:  # buiten class?

    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as file:

        contents = json.load(file)
    return contents


if __name__ == "__main__":
    conn = DBConfig.dcm.conn
    cursor = conn.cursor()

    DBConfig.ResetMembers()
    DBConfig.ResetUsers()

    superAdminData = DBConfig.usersDAO.SelectUser("user1")
    superAdmin = SuperAdmin(superAdminData[0], superAdminData[1], superAdminData[2], superAdminData[3], superAdminData[4])
    print(superAdmin)
    print("=============\n")

    systemAdminData = DBConfig.usersDAO.SelectUser("user2")
    systemAdmin = SystemAdmin(systemAdminData[0], systemAdminData[1], systemAdminData[2], systemAdminData[3], systemAdminData[4])
    print(systemAdmin)
    print("=============\n")

    consultantData = DBConfig.usersDAO.SelectUser("user3")
    consultant = Consultant(consultantData[0], consultantData[1], consultantData[2], consultantData[3], consultantData[4])
    print(consultant)
    print("=============\n")

    print("=============\nT E S T   C O N S U L T A N T\n=============\n")

    print("TEST CONSULTANT PASSWORD UPDATE")
    print(f"{consultant.FirstName} password: {consultant.Password}")
    oldPassword = consultant.Password
    consultant.UpdatePassword("NewPW123")
    print(f"{consultant.FirstName} password: {consultant.Password}")
    print("=============\n")
    
    DBConfig.ResetUsers() #resets changes in db

    print("TEST CONSULTANT ADD NEW MEMBER")
    consultant.AddNewMember("New", "Member", 50, "Female", "70", "NewStreet", "400A", "1998KA", "NewCity", "NewEmail@mail.com", "123456789")
    newMember = DBConfig.membersDAO.SelectMember("New", "Member")
    print(newMember)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST CONSULTANT UPDATE MEMBER INFO MEMBERSHIPID")
    consultant.UpdateMemberInfo("MembershipID", "2410158313", "2410158313", "123ID")
    updateIDmember = DBConfig.membersDAO.SelectMemberByMatch("123ID")
    print(updateIDmember)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST CONSULTANT UPDATE MEMBER INFO AGE")
    consultant.UpdateMemberInfo("Age", "2410158313", "56", "18")
    updateAgemember = DBConfig.membersDAO.SelectMemberByMatch("2410158313")
    print(updateAgemember)
    print("=============\n")


    print("TEST CONSULTANT SEARCH MEMBER INFO")
    searchTerm = "8YZ"
    foundMember = consultant.SearchMemberInfo(searchTerm)
    print(foundMember)
    print("=============\n")


    print("=============\nT E S T   S Y S T E M A D M I N\n=============\n")


    print("TEST SYSTEMADMIN PASSWORD UPDATE")
    print(f"{systemAdmin.FirstName} password: {systemAdmin.Password}")
    sysoldPassword = systemAdmin.Password
    systemAdmin.UpdatePassword("NewPW123")
    print(f"{systemAdmin.FirstName} password: {systemAdmin.Password}")
    print("=============\n")
    
    DBConfig.ResetUsers() #resets changes in db

    print("TEST SYSTEMADMIN ADD NEW MEMBER")
    systemAdmin.AddNewMember("New1", "Member1", 30, "Femawwle", "70", "NewStreet1", "400A", "1998KA", "NewCity", "NewEmail@mail.com", "123456789")
    sysnewMember = DBConfig.membersDAO.SelectMember("New1", "Member1")
    print(sysnewMember)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SYSTEMADMIN SEARCH MEMBER INFO")
    syssearchTerm = "8YZ"
    sysfoundMember = systemAdmin.SearchMemberInfo(searchTerm)
    print(sysfoundMember)
    print("=============\n")

    print("TEST SYSTEMADMIN CHECK ALL USERS")
    sysallusers = systemAdmin.CheckAllUsers()
    for user in sysallusers:
        print(user)
        print()
    
    print("TEST SYSTEMADMIN ADD NEW CONSULTANT")
    systemAdmin.AddNewConsultant("hehe", "haha", "FN", "LN")
    newCons = DBConfig.usersDAO.SelectUser("hehe")
    print(newCons)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SYSTEMADMIN UPDATE CONSULTANT INFO")
    systemAdmin.UpdateConsultantInfo("FirstName", "user13", "Matthew", "NEWWW")
    updateFNcons = DBConfig.usersDAO.SelectUser("user13")
    print(updateFNcons)
    print("=============\n")


    print("TEST SYSTEMADMIN DELETE CONSULTANT")
    systemAdmin.DeleteConsultant("hehe", "haha")
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SYSTEMADMIN RESET CONSULTANT PASSWORD")
    systemAdmin.ResetConsultantPassword("user8")
    resetPWcons = DBConfig.usersDAO.SelectUser("user8")
    print(resetPWcons)
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SYSTEMADMIN DELETE MEMBER")
    systemAdmin.DeleteMember("2410005351", "First0", "Last0")

    DBConfig.ResetMembers()

    print("=============\nT E S T   S U P E R A D M I N\n=============\n")

    print("TEST SUPERADMIN PASSWORD UPDATE")
    print(f"{superAdmin.FirstName} password: {superAdmin.Password}")
    saoldPassword = superAdmin.Password
    superAdmin.UpdatePassword("NewPW123")
    print(f"{superAdmin.FirstName} password: {superAdmin.Password}")
    print("=============\n")
    
    DBConfig.ResetUsers() #resets changes in db

    print("TEST SUPERADMIN ADD NEW MEMBER")
    superAdmin.AddNewMember("New", "Member", 50, "Female", "70", "NewStreet", "400A", "1998KA", "NewCity", "NewEmail@mail.com", "123456789")
    supnewMember = DBConfig.membersDAO.SelectMember("New", "Member")
    print(supnewMember)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SUPERADMIN UPDATE MEMBER INFO MEMBERSHIPID")
    superAdmin.UpdateMemberInfo("MembershipID", "2410158313", "2410158313", "123ID")
    supupdateIDmember = DBConfig.membersDAO.SelectMemberByMatch("123ID")
    print(supupdateIDmember)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SUPERADMIN UPDATE MEMBER INFO AGE")
    superAdmin.UpdateMemberInfo("Age", "2410158313", "56", "18")
    supupdateAgemember = DBConfig.membersDAO.SelectMemberByMatch("2410158313")
    print(supupdateAgemember)
    print("=============\n")


    print("TEST SUPERADMIN SEARCH MEMBER INFO")
    searchTerm = "8YZ"
    foundMember = superAdmin.SearchMemberInfo(searchTerm)
    print(foundMember)
    print("=============\n")
    

    print("TEST SUPERADMIN ADD NEW MEMBER")
    superAdmin.AddNewMember("New1", "Member1", 30, "Femawwle", "70", "NewStreet1", "400A", "1998KA", "NewCity", "NewEmail@mail.com", "123456789")
    supnewMember = DBConfig.membersDAO.SelectMember("New1", "Member1")
    print(supnewMember)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SUPERADMIN SEARCH MEMBER INFO")
    supsearchTerm = "8YZ"
    supfoundMember = superAdmin.SearchMemberInfo(searchTerm)
    print(supfoundMember)
    print("=============\n")

    print("TEST SUPERADMIN CHECK ALL USERS")
    supallusers = superAdmin.CheckAllUsers()
    for user in supallusers:
        print(user)
        print()
    
    print("TEST SUPERADMIN ADD NEW CONSULTANT")
    superAdmin.AddNewConsultant("hehe", "haha", "FN", "LN")
    supnewCons = DBConfig.usersDAO.SelectUser("hehe")
    print(supnewCons)
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SUPERADMIN UPDATE CONSULTANT INFO")
    superAdmin.UpdateConsultantInfo("FirstName", "user13", "Matthew", "NEWWW")
    supupdateFNcons = DBConfig.usersDAO.SelectUser("user13")
    print(supupdateFNcons)
    print("=============\n")


    print("TEST SUPERADMIN DELETE CONSULTANT")
    superAdmin.DeleteConsultant("hehe", "haha")
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SUPERADMIN RESET CONSULTANT PASSWORD")
    superAdmin.ResetConsultantPassword("user8")
    supresetPWcons = DBConfig.usersDAO.SelectUser("user8")
    print(supresetPWcons)
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SYSTEMADMIN DELETE MEMBER")
    systemAdmin.DeleteMember("2410005351", "First0", "Last0")
    print("=============\n")

    DBConfig.ResetMembers()

    print("TEST SUPERADMIN ADD NEW SYSTEMADMIN")
    superAdmin.AddNewSystemAdmin("hehe", "haha", "FN", "LN")
    supnewSYS = DBConfig.usersDAO.SelectUser("hehe")
    print(supnewSYS)
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SUPERADMIN UPDATE SYSTEMADMIN INFO FIRSTNAME")
    superAdmin.UpdateSystemAdminInfo("FirstName", "user13", "Matthew", "NEWWW")
    supupdateFNsyst = DBConfig.usersDAO.SelectUser("user13")
    print(supupdateFNsyst)
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SUPERADMIN DELETE SYSTEMADMIN")
    superAdmin.DeleteSystemAdmin("user1", "password1")
    print("=============\n")

    DBConfig.ResetUsers()

    print("TEST SUPERADMIN RESET SYSTEMADMIN PASSWORD")
    superAdmin.ResetSystemAdminPassword("user1")
    print("=============\n")

    DBConfig.ResetUsers()
    DBConfig.ResetMembers()




























    # #consultant.AddNewMember("asd", "asdfg", 13, "Female", 40.0, "straatie", "90", "1234aAB", "Roosendaal", "Emailllll", "123456789")
    # # membersOfMatch = consultant.SearchMemberInfo("41403")
    # # for m in membersOfMatch:
    # #     print(m)
    # #     print()
    # # memberToSelect = Member("First0", "Last0", 26, "Make", 66.2671257993742, "Street0", "57", "9206AB", "City0", "7652365764", "2024-06-12 08:30:11.781313")
    
    # #member = DBConfig.membersDAO.SelectMember(memberToSelect)
    # #enter your code here :)



