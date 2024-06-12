from .SystemAdmin import SystemAdmin


class SuperAdmin(SystemAdmin):
    def UpdatePassword(self, password=""):
        return "SuperAdmin is not allowed to change its own password."
    
    def AddNewSystemAdmin(self, username, password, firstName, lastName):
        newSystemAdmin = SystemAdmin(username, password, firstName, lastName)
        #todo save new system admin to database
    
    def UpdateSystemAdminInfo(self, SystemAdmin):
        #todo figure out what can and cannot be updated or modified
        pass

    def DeleteSystemAdmin(self, systemAdmin):
        #todo use query to delete systemAmdin from database
        pass

    def ResetSystemAdminPassword(self, systemAdmin):
        consultant.password = "temporarySy123" #todo should adhere to pw rules
        #todo update database