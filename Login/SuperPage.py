from . import InputDef
from Roles.SuperAdmin import SuperAdmin

def display_menuA():
    print(
    "Consultant\n" +
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

def handle_optionA(option):
    if option == '1':
        InputDef.CheckList()
    elif option == '2':
        InputDef.AddConsultant()
    elif option == '3':
        InputDef.UpdateConsultant()
    elif option == '4':
        pass
    elif option == '5':
        pass
    elif option == '6':
        pass
    elif option == '7':
        pass
    elif option == '8':
        pass
    elif option == '9':
        pass
    elif option == '10':
        pass
    elif option == '11':
        pass
    elif option == '12':
        pass
    elif option == '13':
        pass
    elif option == '14':
        pass
    elif option == '15':
        pass
    elif option == '16':
        pass
    elif option == '17':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")