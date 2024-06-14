from Roles.SystemAdmin import SystemAdmin

def display_menuB():
    print(
    "Consultant\n" +
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

def handle_optionB(option):
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
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
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")