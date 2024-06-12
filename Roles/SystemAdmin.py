from .Consultant import Consultant


class SystemAdmin(Consultant):
    def CheckAllUsers(self):
        #todo fetch all users from database and print their profile
        pass

    def AddNewConsultant(self, username, password, firstName, lastName):
        newConsultant = Consultant(username, password, firstName, lastName)
        #todo save new consultant to database
    
    def UpdateConsultantInfo(self, consultant):
        #todo figure out what can and cannot be updated or modified
        pass

    def DeleteConsultant(self, consultant):
        #todo use query to delete consultant from database
        pass

    def ResetConsultantPassword(self, consultant):
        consultant.password = "temporaryC123" #todo should adhere to pw rules
        #todo update database
    
    def MakeSystemBackup(self):
        #wtf does this mean
        pass

    def RestoreSystemBackup(self):
        #wtf does this mean part 2
        pass

    def SeeLogFiles(self):
        #wtf does this mean part 3??????
        pass

    def DeleteMember(self, member):
        #todo use query to delete member from database
        pass