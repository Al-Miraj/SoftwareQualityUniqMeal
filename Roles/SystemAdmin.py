from .Member import Member
from .Consultant import Consultant
from Database.DBConfig import DBConfig


class SystemAdmin(Consultant):
    def CheckAllUsers(self) -> list | None:
        return DBConfig.usersDAO.SelectAllUsers()

    def AddNewConsultant(self, username, password, firstName, lastName) -> None:
        newConsultant = Consultant(username, password, firstName, lastName)
        DBConfig.usersDAO.InsertUsers([newConsultant])
    
    def UpdateConsultantInfo(self, toUpdate, username, oldInfo, newInfo):
        if toUpdate == "Username":
            DBConfig.usersDAO.UpdateUserUserName(oldInfo, newInfo)
        elif toUpdate == "FirstName":
            DBConfig.usersDAO.UpdateUserFirstName(username, oldInfo, newInfo)
        elif toUpdate == "LastName":
            DBConfig.usersDAO.UpdateUserLastName(username, oldInfo, newInfo)
        #update Role allowed???
        elif toUpdate == "Role":
            DBConfig.usersDAO.UpdateUserRole(username, oldInfo, newInfo)

    def DeleteConsultant(self, username, password):
        DBConfig.usersDAO.DeleteUser(username, password)

    def ResetConsultantPassword(self, username):
        consToResetPW = DBConfig.usersDAO.SelectUser(username)
        DBConfig.usersDAO.UpdateUserPassword(username, consToResetPW[1], "temporaryC123") #todo should adhere to pw rules
    
    def MakeSystemBackup(self):
        #wtf does this mean
        pass

    def RestoreSystemBackup(self):
        #wtf does this mean part 2
        pass

    def SeeLogFiles(self):
        #wtf does this mean part 3??????
        pass

    def DeleteMember(self, membershipID, firstName, lastName):
        DBConfig.membersDAO.DeleteMember(membershipID, firstName, lastName)