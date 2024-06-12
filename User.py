import datetime

username = ""

class User:
    Username = None
    Password = None

# Er zijn drie soorten users: Super admin, system admin en consultant
class SuperAdmin(User):
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Super admin is de enige die nieuwe system admin kan aanmaken
    def createNewSystemAdmin(self, username, password):
        systemAdmin = SystemAdmin(username, password)

class SystemAdmin(User):
    def __init(self, username, password):
        self.username = username
        self.password = password

    def createNewConsultant(self, username, password):
        consultant = Consultant(username, password)
    
class Consultant(User):
    def __init(self, username, password):
        self.username = username
        self.password = password



  