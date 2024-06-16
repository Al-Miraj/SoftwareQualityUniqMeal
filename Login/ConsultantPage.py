from Roles.Consultant import Consultant
from . import InputDef

def display_menuC():
    print(
    "Consultant\n" +
    "1: Update your password \n" + 
    "2: Add new member \n" +
    "3: Update member \n" +
    "4: Search member \n" +
    "5: Exit program"
    )

    user_input = input("Select an option: ")
    handle_optionC(user_input)

def handle_optionC(option):
    if option == '1':
        InputDef.PasswordRenew()
        display_menuC()
    elif option == '2':
        InputDef.AddMember()
        display_menuC()
    elif option == '3':
        InputDef.UpdateMember()
        display_menuC()
    elif option == '4':
        InputDef.searchMember()
        display_menuC()
    elif option == '5':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")