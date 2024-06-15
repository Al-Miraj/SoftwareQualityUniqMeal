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

def handle_optionC(option):
    if option == '1':
        InputDef.PasswordRenew()
    elif option == '2':
        InputDef.AddMember()
    elif option == '3':
        InputDef.UpdateMember()
    elif option == '4':
        InputDef.searchMember()
    elif option == '5':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")