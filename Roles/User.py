import datetime



class User():
    def __init__(self, username, password, firstName, lastName, registrationDate=None):
        self.Username = username
        self.Password = password
        self.FirstName = firstName
        self.LastName = lastName
        self.RegistrationDate = datetime.datetime.now() if registrationDate == None else registrationDate
        User.__name__ = "Undefined User"
        self.Role = self.getRole()

    def getRole(self):
        return type(self).__name__

    def __str__(self):
        return f"First name: {self.FirstName}\nLast name: {self.LastName}\nRegistrationDate: {self.RegistrationDate}\nRole: {self.Role}"

