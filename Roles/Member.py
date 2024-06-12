import random
import datetime

class Member:     
    def __init__(self, firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber):
        #WARNING: dont change the order of the attributes as they need to be the same order as the database columns
        self.MembershipID = self._generateMembershipID()
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age
        self.Gender = gender
        self.Weight = weight
        self.Street = street
        self.HouseNumber = houseNumber
        self.ZipCode = zipCode
        self.City = city
        self.Email = email
        self.PhoneNumber = phoneNumber
        self.RegistrationDate = datetime.datetime.now()
    
    def _generateMembershipID(self):
        today = datetime.datetime.now()

        currentYear = str(today.year)
        yearDigits = currentYear[2:]

        randseq = ""
        for i in range(7):
            randseq += f"{random.randint(0, 9)}"

        sum = 0
        for char in yearDigits + randseq:
            sum += int(char)
        checksum = str(sum % 10)

        return yearDigits + randseq + checksum
    
    def __str__(self):
        return f"ID: {self.MembershipID}\nFirst name: {self.FirstName}\nLast name: {self.LastName}"

