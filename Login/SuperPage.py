from . import InputDef
from Roles.SuperAdmin import SuperAdmin
from . import LOG

def display_menuA():
    print(
    "Super add\n" +
    "1: Check Users and their Roles \n" + 
    "2: Add new Consultant \n" +
    "3: Update Consultant \n" +
    "4: Delete Consultant \n" +
    "5: Reset password for Consultant \n" +
    "6: Add new SystemAdmin \n" +
    "7: Update SystemAdmin\n" +
    "8: Delete SystemAdmin \n" +
    "9: Reset password for SystemAdmin\n" +
    "10: Make a backup \n" +
    "11: Reset a backup\n" +
    "12: See Log files \n" +
    "13: Add Member \n" +
    "14: Update Member \n" +
    "15: Delete Member \n" +
    "16: Search Member\n" +
    "17: Exit program"
    )

    user_input = input("Select an option: ")
    handle_optionA(user_input)
    




def handle_optionA(option):
    if option == '1':
        InputDef.CheckList()
        display_menuA()
    elif option == '2':
        InputDef.AddConsultant()
        display_menuA()
    elif option == '3':
        InputDef.UpdateConsultant()
        display_menuA()
    elif option == '4':
        InputDef.Deleteconsultant()
        display_menuA()
    elif option == '5':
        InputDef.ResetconsultantPassword()
        display_menuA()
    elif option == '6':
        InputDef.AddSystemAdmin()
        display_menuA()
    elif option == '7':
        InputDef.UpdateSystemAdmin()
        display_menuA()
    elif option == '8':
        InputDef.DeleteSystemAdmin()
        display_menuA()
    elif option == '9':
        InputDef.ResetadminPassword()
        display_menuA()
    elif option == '10':
        pass
    elif option == '11':
        pass
    elif option == '12':
        LOG.getLog()
        display_menuA()
    elif option == '13':
        InputDef.AddMember()
        display_menuA()
    elif option == '14':
        InputDef.UpdateMember()
        display_menuA()
    elif option == '15':
        InputDef.Deletemember()
        display_menuA()
    elif option == '16':
        InputDef.searchMember()
        display_menuA()
    elif option == '17':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")