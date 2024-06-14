from .User import User
from .Member import Member
from Database.DBConfig import DBConfig

class Consultant(User):

    def UpdatePassword(self, newPassword):
        oldPassword = self.Password
        username = self.Username
        self.Password = newPassword
        DBConfig.usersDAO.UpdateUserPassword(username, oldPassword, newPassword)
    
    def AddNewMember(self, firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber):
        newMember = Member(firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber)
        DBConfig.membersDAO.InsertMembers([newMember])
    
    def UpdateMemberInfo(self, toUpdate, membershipID, oldInfo, newInfo):
        if toUpdate == "MembershipID":
            DBConfig.membersDAO.UpdateMemberMembershipID(oldInfo, newInfo)
        elif toUpdate == "FirstName":
            DBConfig.membersDAO.UpdateMemberFirstName(membershipID, oldInfo, newInfo)
        elif toUpdate == "LastName":
            DBConfig.membersDAO.UpdateMemberLastName(membershipID, oldInfo, newInfo)
        elif toUpdate == "Age":
            DBConfig.membersDAO.UpdateMemberAge(membershipID, oldInfo, newInfo)
        elif toUpdate == "Gender":
            DBConfig.membersDAO.UpdateMemberGender(membershipID, oldInfo, newInfo)
        elif toUpdate == "Weight":
            DBConfig.membersDAO.UpdateMemberWeight(membershipID, oldInfo, newInfo)
        elif toUpdate == "Street":
            DBConfig.membersDAO.UpdateMemberStreet(membershipID, oldInfo, newInfo)
        elif toUpdate == "HouseNumber":
            DBConfig.membersDAO.UpdateMemberHouseNumber(membershipID, oldInfo, newInfo)
        elif toUpdate == "ZipCode":
            DBConfig.membersDAO.UpdateMemberZipCode(membershipID, oldInfo, newInfo)
        elif toUpdate == "City":
            DBConfig.membersDAO.UpdateMemberCity(membershipID, oldInfo, newInfo)
        elif toUpdate == "Email":
            DBConfig.membersDAO.UpdateMemberEmail(membershipID, oldInfo, newInfo)
        elif toUpdate == "PhoneNumber":
            DBConfig.membersDAO.UpdateMemberPhoneNumber(membershipID, oldInfo, newInfo)
        
        #todo figure out what can and cannot be updated or modified

    def SearchMemberInfo(self, searchTerm) -> any:
        return DBConfig.membersDAO.SelectMemberByMatch(searchTerm)





