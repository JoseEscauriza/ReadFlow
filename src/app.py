import sys
from .menu import Menu

while True:
    Menu.display_main_user_menu()
    choice = input("Please select an option: (1/6) ")

    match choice:
        case '1':
            Menu.display_user_acc_menu()

        case '2':
            pass

        case '3':
            pass

        case '4':
            pass

        case '5':
            pass

        case '6':
            print("Goodbye")
            sys.exit()
