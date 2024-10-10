from Roles.SystemAdmin import SystemAdmin
from . import InputDef
from . import LOG

def display_menuB(username):
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
    handle_optionB(user_input, username)

def handle_optionB(option, username):
    if option == '1':
        InputDef.PasswordRenew(username)
        display_menuB(username)
    elif option == '2':
        InputDef.CheckList(username)
        display_menuB(username)
    elif option == '3':
        InputDef.AddConsultant(username)
        display_menuB(username)
    elif option == '4':
        InputDef.UpdateConsultant(username)
        display_menuB(username)
    elif option == '5':
        InputDef.DeleteConsultant(username)
        display_menuB(username)
    elif option == '6':
        InputDef.ResetConsultantPassword(username)
        display_menuB(username)
    elif option == '7':
        pass
    elif option == '8':
        pass
    elif option == '9':
        LOG.view_superadmin_logs()
        display_menuB(username)
    elif option == '10':
        InputDef.AddMember(username)
        display_menuB(username)
    elif option == '11':
        InputDef.UpdateMember(username)
        display_menuB(username)
    elif option == '12':
        InputDef.DeleteMember(username)
        display_menuB(username)
    elif option == '13':
        InputDef.SearchMember(username)
        display_menuB(username)
    elif option == '14':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")