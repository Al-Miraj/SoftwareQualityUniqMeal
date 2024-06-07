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
