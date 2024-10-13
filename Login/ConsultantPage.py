from Roles.Consultant import Consultant
from InputHandler.InputHandler import InputHandler
from CryptUtils.argon import ph
from . import InputDef
from argon2 import exceptions as ex


def display_menuC(consultant):
    print(
    "Consultant\n" +
    "1: Update your password \n" + 
    "2: Add new member \n" +
    "3: Update member \n" +
    "4: Search member \n" +
    "5: Exit program"
    )

    user_input = input("Select an option: ")
    handle_optionC(user_input, consultant)

def handle_optionC(option, consultant):

    if option == '1':
        # InputDef.PasswordRenew(username)
        while True:
            newPW = input("Enter your new password: ")
            if InputHandler.checkPasswordFormat(newPW):
                try:
                    ph.verify(consultant.Password, consultant.Username + newPW)
                    print("You already use this password.")
                except (ex.VerifyMismatchError, ex.VerificationError):
                    if consultant.UpdatePassword(newPW):
                        print("Password has updated succesfully")
                    else:
                        print("Something went wrong.")
                    break
            else:
                print("Wrong password format. try again.")
        display_menuC(consultant)
    elif option == '2':
        InputDef.AddMember(username)
        display_menuC(username)
    elif option == '3':
        InputDef.UpdateMember(username)
        display_menuC(username)
    elif option == '4':
        InputDef.searchMember(username)
        display_menuC(username)
    elif option == '5':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")