class Menu():

    @staticmethod
    def display_main_user_menu():
        print("""
              
              MAIN MENU
              
              1. Account menu
              2. Book menu
              3. Borrowed book menu
              4. Logs menu
              5. Log out
              6. Exit
              """)

    @staticmethod
    def display_user_acc_menu():
        print("""
              Please pick an option:
              1. Change username
              2. Change password
              3. Change email
              4. Change phone number
              5. Change recovery question
              6. Go back to previous menu
              7. Go to main menu
              """)
