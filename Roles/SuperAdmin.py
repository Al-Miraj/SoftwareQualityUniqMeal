from .SystemAdmin import SystemAdmin
from Database.DBConfig import DBConfig

class SuperAdmin(SystemAdmin):
    def UpdatePassword(self, password="") -> str:
        print("SuperAdmin is not allowed to change its own password.")
    
    def AddNewSystemAdmin(self, username, password, firstName, lastName):
        newSystemAdmin = SystemAdmin(username, password, firstName, lastName)
        DBConfig.usersDAO.InsertUsers([newSystemAdmin])
    
    def UpdateSystemAdminInfo(self, toUpdate, username, oldInfo, newInfo):
        if toUpdate == "Username":
            DBConfig.usersDAO.UpdateUserUserName(oldInfo, newInfo)
        elif toUpdate == "FirstName":
            DBConfig.usersDAO.UpdateUserFirstName(username, oldInfo, newInfo)
        elif toUpdate == "LastName":
            DBConfig.usersDAO.UpdateUserLastName(username, oldInfo, newInfo)
        #update Role allowed???
        elif toUpdate == "Role":
            DBConfig.usersDAO.UpdateUserRole(username, oldInfo, newInfo)

    def DeleteSystemAdmin(self, username, password):
        DBConfig.usersDAO.DeleteUser(username, password)

    def ResetSystemAdminPassword(self, username):
        systAdminToResetPW = DBConfig.usersDAO.SelectUser(username)
        DBConfig.usersDAO.UpdateUserPassword(username, systAdminToResetPW[1], "temporarySYS123") #todo should adhere to pw rules