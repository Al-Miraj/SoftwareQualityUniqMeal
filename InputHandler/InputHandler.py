import re


class InputHandler:
    Cities = [
      "Amsterdam",
      "Rotterdam",
      "Den Haag",
      "Utrecht",
      "Eindhoven",
      "Groningen",
      "Tilburg",
      "Almere",
      "Breda",
      "Nijmege"
    ]


    @staticmethod
    def checkUsernameExists(username):
        """
        if it does not already exists in database (case insensitive)
            return true
        else
            return false
        """

    
    @staticmethod
    def checkUsernameFormat(username:str) -> bool:
        usernamelc = username.lower()
        correctFormat = True
        if (8 <= len(usernamelc) <= 10) == False:
            print("Username should be at least 8 and no more than 10 charachters long.")
            correctFormat = False
        elif re.search(r'[a-z_]', usernamelc[0]) == None:
            print("Username should start with any letter (a-z) or an underscore (_)")
            correctFormat = False
        elif re.search(r'[^a-z0-9_\'\.]', usernamelc[1:]):
            print("Username should not contain a character other than letters (a-z), numbers (0-9), underscores (_), apostrophes ('), and periods (.)")
            correctFormat = False
        return correctFormat
    
    @staticmethod
    def checkPasswordFormat(password:str)->bool:
        correctFormat = True
        if (12 <= len(password) <= 30) == False:
            print("Password should be at least 12 and no more than 30 charachters long.")
            correctFormat = False
        elif (re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@#$%&_\-+=`|\(){}[\]:;'<>,.?\/])[A-Za-z0-9~!@#$%&_\-+=`|\(){}[\]:;'<>,.?\/]{12,30}$", password) == None):
            print("Password should contain a combination of at least one lowercase letter (a-z), one uppercase letter (A-Z), one digit (0-9), and one special character ( ~!@#$%&_-+=`|\(){}[]:;'<>,.?/ ).")
            correctFormat = False
        return correctFormat

    @staticmethod
    def checkFirstName(firstName):
        correctFormat = True
        if (1<= len(firstName) <= 25) == False:
            print("First name must be at least 1 and no more than 25 charachters long.")
            correctFormat = False
        elif re.search(r'^[\sa-zA-Z\'-]+$', firstName) == None:
            print("First name must not contain a character other than letters a-z or A-Z and characters - or '")
            correctFormat = False
        return correctFormat

    @staticmethod
    def checkLastName(lastName):
        correctFormat = True
        if (1<= len(lastName) <= 25) == False:
            print("Last name must be at least 1 and no more than 25 charachters long.")
            correctFormat = False
        elif re.search(r'^[\sa-zA-Z\'-]+$', lastName) == None:
            print("Last name must not contain a character other than letters a-z or A-Z and characters - or '")
            correctFormat = False
        return correctFormat
    
    @staticmethod
    def checkEmailFormat(email:str):
        emaillw = email.lower()
        correctFormat = True
        if (5 <= len(emaillw) <= 320) == False:
            print("Email should be at least 5 and no more than 320 charachters long.")
            correctFormat = False
        elif re.search(r"^(?!\.)(?!.*\.\.)(?!.*--)(?!.*__)(?!.*_$)(?!.*-$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}$", emaillw) is None:
            print("Email does not have the correct format (example@email.com)")
            correctFormat = False
        return correctFormat


    #age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber
    @staticmethod
    def checkAgeFormat(age: str) -> bool:
        correctFormat = True
        if re.search(r'^\d{2,3}$', age) is None:
            print("Age must only contain digits 0-9.")
            correctFormat = False
        else:
            if not (18 <= int(age) <= 130):
                print("You must be at least 18 years old to be able to join.")
                correctFormat = False
        return correctFormat


    @staticmethod
    def checkGenderFormat(gender):
        correctFormat = True
        if not re.search(r'^(M|F)$', gender):
            print("Gender should be either M for Male or F for Female")
            correctFormat = False
        return correctFormat

    @staticmethod
    def checkWeightFormat(weight):
        correctFormat = True
        try:
            int(weight)
            float(weight)
        except ValueError:
            print("Weight must be a whole or decimal number i.e. 60 or 60.56")
            correctFormat = False
        return correctFormat

    @staticmethod
    def checkStreetFormat(street):
        correctFormat = True
        if(re.search(r"^(?=.*[A-Za-z])(?!.*[^A-Za-z0-9\-\. ])$", street) == False):
            print("Street name must only contain letters a-z or A-Z, numbers 0-9 and may contain characters - or .")
            correctFormat = False
        return correctFormat


    @staticmethod
    def checkHouseNumberFormat(houseNumber):
        correctFormat = True
        if (re.search(r'^\d{1,5}[A-Za-z]?$', houseNumber) == False):
            print("House number must contain at least 1 number and only contain digits and may contain letters a-z or A-Z")
            correctFormat = False
        return correctFormat


    @staticmethod        
    def checkZipCodeFormat(zipcode):
        correctFormat = True
        if re.search(r'^\d{4}[A-Za-z]{2}$', zipcode) == False:
            print("The zipcode must contain 4 digits and then 2 letters (DDDDXX) i.e. 1234ET")
            correctFormat = False
        return correctFormat


    @staticmethod
    def checkCityFormat(city):
        correctFormat = True
        if city not in InputHandler.Cities:
            print("Please choose one of the cities listed above.")
            correctFormat = False
        return correctFormat


    @staticmethod 
    def checkPhoneNumberFormsat(phoneNumber):
        correctFormat = True
        if(re.search(r'^[+]31[-]6[-]\d{8}$', phoneNumber)):
            print("Phone number must follow this format: (+31-6-DDDDDDDD)")
            correctFormat = False
        return correctFormat








        




    

    

    
