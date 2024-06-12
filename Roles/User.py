import datetime



# Define the abstract base User class
class User():
    def __init__(self, username, password, firstName, lastName):
        self.Username = username
        self.Password = password
        self.FirstName = firstName
        self.LastName = lastName
        self.RegistrationDate = datetime.datetime.now()
        User.__name__ = "Undefined User"
        self.Role = self.getRole()

    def getRole(self):
        return type(self).__name__

    def __str__(self):
        return f"First name: {self.FirstName}\nLast name: {self.LastName}\nRegistrationDate: {self.RegistrationDate}\nRole: {self.Role}"
