from Roles.Consultant import Consultant


Consultant

def display_menuA():
    print(
    "Consultant\n" +
    "1: Update your password \n" + 
    "2: Add new member \n" +
    "3: Update member \n" +
    "4: Search member by first last and member id\n" +
    "5: Exit program"
    )

def handle_optionA(option):
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        pass
    elif option == '5':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please choose a valid option.")