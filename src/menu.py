class Menu():

    @staticmethod
    def display_main_user_menu():
        print("""         
              MAIN MENU
              
              1. Account menu
              2. Book menu
              3. Borrowed book menu
              4. Logs menu
              88. Log out
              99. Exit App
              """)

    @staticmethod
    def display_user_acc_menu():
        print("""
              USER ACCOUNT MENU:
              
              1. Change username
              2. Change password
              3. Change email
              4. Change phone number
              5. Change recovery question
              6. Go back to previous menu
              77. Go back to User Main Menu
              88. Log Out
              99. Exit App
              
              """)

    @staticmethod
    def display_admin_main_menu():
        print("""
              ADMIN MAIN MENU:
              
              1. Account Menu
              2. Author Menu
              3. Book Copy Menu
              4. Borrowed Book Menu
              5. Log Menu
              88. Log Out
              99. Exit App
              
              """)

    @staticmethod
    def display_admin_author_menu():
        print("""
              ADMIN AUTHOR MENU:
              
              1. Add Author
              2. Modify Author
              3. Delete Author
              4. Search by Author
              77. Go back to Admin Main Menu
              88. Log Out
              99. Exit App
              
              """)

    @staticmethod
    def display_admin_log_menu():
        print("""
              ADMIN LOG MENU:
              
              1. Report Bugs
              2. Generate Bug Report
              77. Go back to Admin Main Menu
              88. Log Out
              99. Exit App
              
              """)

    @staticmethod
    def display_admin_acc_menu():
        print("""
              ADMIN ACCOUNT MENU:
              
              1. Change Username
              2. Change Password
              3. Change email
              4. Change phone number
              5. Change special question
              77. Go back to Admin Main Menu
              88. Log Out
              99. Exit App
              
              """)

    @staticmethod
    def display_admin_book_copy_menu():
        print("""
              ADMIN BOOK COPY MENU:
              
              1. Add Book Copy
              2. Delete Book Copy
              3. Change Book availability
              4. Change Book location
              77. Go back to Admin Main Menu
              88. Log Out
              99. Exit App
              
              """)
