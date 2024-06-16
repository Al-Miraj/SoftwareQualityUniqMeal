from Roles.SystemAdmin import SystemAdmin
from . import InputDef
from . import LOG

def display_menuB():
    print(
    "Admin\n" +
    "1: Update your password \n" + 
    "2: List of Users and their Roles \n" +
    "3: Add new Consultant \n" +
    "4: Update Consultant \n" +
    "5: Delete a Consultant \n" +
    "6: Reset a Consultant's password \n" +
    "7: Making Backup \n" +
    "8: Restore Backup \n" +
    "9: See Log file \n" +
    "10: Add new member \n" +
    "11: Update a member\n" +
    "12: Delete a member \n" +
    "13: Search member \n" +
    "14: Exit program"
    )

    user_input = input("Select an option: ")
    handle_optionB(user_input)

def handle_optionB(option):
    if option == '1':
        InputDef.PasswordRenew()
        display_menuB()
    elif option == '2':
        InputDef.CheckList()
        display_menuB()
    elif option == '3':
        InputDef.AddConsultant()
        display_menuB()
    elif option == '4':
        InputDef.UpdateConsultant()
        display_menuB()
    elif option == '5':
        InputDef.DeleteConsultant()
        display_menuB()
    elif option == '6':
        InputDef.ResetConsultantPassword()
        display_menuB()
    elif option == '7':
        pass
    elif option == '8':
        pass
    elif option == '9':
        LOG.getLog()
    elif option == '10':
        InputDef.AddMember()
        display_menuB()
    elif option == '11':
        InputDef.UpdateMember()
        display_menuB()
    elif option == '12':
        InputDef.DeleteMember()
        display_menuB()
    elif option == '13':
        InputDef.SearchMember()
        display_menuB()
    elif option == '14':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")