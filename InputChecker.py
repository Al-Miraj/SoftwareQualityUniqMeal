import re
from User import User

class InputChecker:

    def checkPhoneNumber(phoneNumber):
        regex_phone_number_pattern = r'^[+]31[-]6[-]\d{8}$'
        if(re.search(regex_phone_number_pattern,phoneNumber)):
            print("yay")
        else:
            print("nay")

    # def checkZipcode(zipCode):
    #     # zipcode_check_pattern = r'^d{8}'