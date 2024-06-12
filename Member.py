import random
import datetime

class Member: 
    firstName = None
    lastName = None
    age = None
    gender = None
    weight = None
    street = None
    houseNumber = None
    zipCode = None
    city = None
    email = None
    phoneNumber = None
    membershipID = None

    
    def __init__(self, firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.weight = weight
        self.street = street
        self.houseNumber = houseNumber
        self.zipCode = zipCode
        self.city = city
        self.email = email
        self.phoneNumber = phoneNumber
        self.membershipID = _generateMembershipID()
    
    def _generateMembershipID():
        today = datetime.datetime.now()
        currentYear = str(today.year)

        yearDigits = currentYear[2:]
        randseq = ""
        for i in range(7):
            randseq += f"{random.randint(0, 9)}"

        sum = 0
        for char in yearDigits + randseq:
            sum += int(char)
        checksum = sum % 10

        return yearDigits + randseq + str(checksum)

