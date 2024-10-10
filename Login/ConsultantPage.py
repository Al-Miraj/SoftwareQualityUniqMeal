from Roles.Consultant import Consultant
from . import InputDef

def display_menuC(username):
    print(
    "Consultant\n" +
    "1: Update your password \n" + 
    "2: Add new member \n" +
    "3: Update member \n" +
    "4: Search member \n" +
    "5: Exit program"
    )

    user_input = input("Select an option: ")
    handle_optionC(user_input, username)

def handle_optionC(option, username):
    if option == '1':
        InputDef.PasswordRenew(username)
        display_menuC(username)
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