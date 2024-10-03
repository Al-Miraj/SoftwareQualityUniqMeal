import re

'''
whitelisting, identify good data and filter the rest
    - list what is harmless and regect what does not meet this
blacklisting, identify bad data and filter the rest
    - list what is harmfull and reject everything that meets this

whitelisting is preferred because it blocks both bad and unknown data

/////////////

user input is what comes from input fields of type text and password or from textareas
it might be invalid because of typing errors.

if user input is invalid, you should politely tell the user that something isnt right
and encourage them to change the input.

do NOT try to massage invalid input as an attacker may still find a way
to bypass this. it is better to just reject it completely and log the
activity.
/////////////////

suggestion for good input validation:
    - function that return a boolean
    - check the range
    - check the length
    - check for null-byte presence
    - validate input before anything else
    - perform authorization tests along with input validation
    - pattern matching with RegEx

'''
















class InputHandler:
    error = None
    message = ''
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

    
    # @staticmethod
    # def checkUsernameFormat(username:str) -> bool:
    #     usernamelc = username.lower() #does this count as massaging input
    #     correctFormat = True
    #     if (8 <= len(usernamelc) <= 10) == False:
    #         print("Username should be at least 8 and no more than 10 charachters long.")
    #         correctFormat = False
    #     elif re.search(r'[a-z_]', usernamelc[0]) == None:
    #         print("Username should start with any letter (a-z) or an underscore (_)")
    #         correctFormat = False
    #     elif re.search(r'[^a-z0-9_\'\.]', usernamelc[1:]): XXXXXXXXXXX
    #         print("Username should not contain a character other than letters (a-z), numbers (0-9), underscores (_), apostrophes ('), and periods (.)")
    #         correctFormat = False
    #     return correctFormat
    
    @staticmethod
    def checkUsernameFormat(username:str) -> bool:
        usernamelc = username.lower()
        if (8 <= len(usernamelc) <= 10):
            if re.search(r'[a-z_]', usernamelc[0]):
                if re.search(r'^[a-z0-9_\'\.]+$', usernamelc[1:]): 
                    return True
        return false

    
    # @staticmethod
    # def checkPasswordFormat(password:str)->bool:
    #     correctFormat = True
    #     if (12 <= len(password) <= 30) == False:
    #         print("Password should be at least 12 and no more than 30 charachters long.")
    #         correctFormat = False
    #     elif (re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@#$%&_\-+=`|\(){}[\]:;'<>,.?\/])[A-Za-z0-9~!@#$%&_\-+=`|\(){}[\]:;'<>,.?\/]{12,30}$", password) == None):
    #         print("Password should contain a combination of at least one lowercase letter (a-z), one uppercase letter (A-Z), one digit (0-9), and one special character ( ~!@#$%&_-+=`|\(){}[]:;'<>,.?/ ).")
    #         correctFormat = False
    #     return correctFormat


    @staticmethod
    def checkPasswordFormat(password:str)->bool:
        if (12 <= len(password) <= 30):
            if (re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@#$%&_\-+=`|\(){}[\]:;'<>,.?\/])[A-Za-z0-9~!@#$%&_\-+=`|\(){}[\]:;'<>,.?\/]{12,30}$", password)):
                return True
        return False



    # @staticmethod
    # def checkFirstName(firstName):
    #     correctFormat = True
    #     if (1<= len(firstName) <= 25) == False:
    #         print("First name must be at least 1 and no more than 25 charachters long.")
    #         correctFormat = False
    #     elif re.search(r'^[\sa-zA-Z\'-]+$', firstName) == None:
    #         print("First name must not contain a character other than letters a-z or A-Z and characters - or '")
    #         correctFormat = False
    #     return correctFormat


    @staticmethod
    def checkFirstName(firstName:str)->bool:
        if (1<= len(firstName) <= 25):
            if re.search(r'^[\sa-zA-Z\'-]+$', firstName):
                return True
        return False


    # @staticmethod
    # def checkLastName(lastName):
    #     correctFormat = True
    #     if (1<= len(lastName) <= 25) == False:
    #         print("Last name must be at least 1 and no more than 25 charachters long.")
    #         correctFormat = False
    #     elif re.search(r'^[\sa-zA-Z\'-]+$', lastName) == None:
    #         print("Last name must not contain a character other than letters a-z or A-Z and characters - or '")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkLastName(lastName:str)->bool:
        if (1<= len(lastName) <= 25):
            if re.search(r'^[\sa-zA-Z\'-]+$', lastName):
                return True
        return False

    
    # @staticmethod
    # def checkEmailFormat(email:str):
    #     emaillw = email.lower()
    #     correctFormat = True
    #     if (5 <= len(emaillw) <= 320) == False:
    #         print("Email should be at least 5 and no more than 320 charachters long.")
    #         correctFormat = False
    #     elif re.search(r"^(?!\.)(?!.*\.\.)(?!.*--)(?!.*__)(?!.*_$)(?!.*-$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}$", emaillw) is None:
    #         print("Email does not have the correct format (example@email.com)")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkEmailFormat(email:str)->bool:
        emaillw = email.lower()
        if (5 <= len(emaillw) <= 320):
            if re.search(r"^(?!\.)(?!.*\.\.)(?!.*--)(?!.*__)(?!.*_$)(?!.*-$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}$", emaillw):
                return True
        return False


    # #age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber
    # @staticmethod
    # def checkAgeFormat(age: str) -> bool:
    #     correctFormat = True
    #     if re.search(r'^\d{2,3}$', age) is None:
    #         print("Age must only contain digits 0-9.")
    #         correctFormat = False
    #     else:
    #         if not (18 <= int(age) <= 130):
    #             print("You must be at least 18 years old to be able to join.")
    #             correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkAgeFormat(age: str) -> bool:
        if re.search(r'^\d{2,3}$', age):
            if (18 <= int(age) <= 130):
                return True
        return False


    # @staticmethod
    # def checkGenderFormat(gender):
    #     correctFormat = True
    #     if not re.search(r'^(M|F)$', gender): XXXXXXXXXXX???
    #         print("Gender should be either M for Male or F for Female")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkGenderFormat(gender:str)->bool:
        return re.search(r'^(M|F)$', gender)


    # @staticmethod XXXXXXXXXXX
    # def checkWeightFormat(weight):
    #     correctFormat = True
    #     try:
    #         int(weight)
    #         float(weight)
    #     except ValueError:
    #         print("Weight must be a whole or decimal number i.e. 60 or 60.56")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkWeightFormat(weight:str)->bool:
        if re.search(r'^[0-9]+([\.||\,][0-9]{1,2})?$', weight):
            if (0 < float(weight) <= 500):
                return True
        return False



    # @staticmethod
    # def checkStreetFormat(street:str)->bool:
    #     correctFormat = True
    #     if(re.search(r"^(?=.*[A-Za-z])(?!.*[^A-Za-z0-9\-\. ])$", street) == False):
    #         print("Street name must only contain letters a-z or A-Z, numbers 0-9 and may contain characters - or .")
    #         correctFormat = False
    #     return correctFormat
    
    @staticmethod
    def checkStreetFormat(street:str)->bool:
        return re.search(r"^(?=.*[A-Za-z])(?!.*[^A-Za-z0-9\-\. ])$", street)



    # @staticmethod
    # def checkHouseNumberFormat(houseNumber:str)->bool:
    #     correctFormat = True
    #     if (re.search(r'^\d{1,5}[A-Za-z]?$', houseNumber) == False):
    #         print("House number must contain at least 1 number and only contain digits and may contain letters a-z or A-Z")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkHouseNumberFormat(houseNumber:str)->bool:
        return re.search(r'^\d{1,5}[A-Za-z]?$', houseNumber)


    # @staticmethod        
    # def checkZipCodeFormat(zipcode:str)->bool:
    #     correctFormat = True
    #     if re.search(r'^\d{4}[A-Za-z]{2}$', zipcode) == False:
    #         print("The zipcode must contain 4 digits and then 2 letters (DDDDXX) i.e. 1234ET")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod        
    def checkZipCodeFormat(zipcode:str)->bool:
        return re.search(r'^\d{4}[A-Za-z]{2}$', zipcode)


    # @staticmethod
    # def checkCityFormat(city:str)->bool:
    #     correctFormat = True
    #     if city not in InputHandler.Cities:
    #         print("Please choose one of the cities listed above.")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod
    def checkCityFormat(city:str)->bool:
        return city in InputHandler.Cities


    # @staticmethod 
    # def checkPhoneNumberFormsat(phoneNumber:str)->bool:
    #     correctFormat = True
    #     if(re.search(r'^[+]31[-]6[-]\d{8}$', phoneNumber)):
    #         print("Phone number must follow this format: (+31-6-DDDDDDDD)")
    #         correctFormat = False
    #     return correctFormat

    @staticmethod 
    def checkPhoneNumberFormsat(phoneNumber:str)->bool:
        return re.search(r'^[+]31[-]6[-]\d{8}$', phoneNumber)






    

    

    
