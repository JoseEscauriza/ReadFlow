class Menu:
    @staticmethod
    def display_main_user_menu():
        print(
            """
              
              MAIN MENU
              
              1. Account menu
              2. Book menu
              3. Borrowed book menu
              4. Logs menu
              5. Log out
              6. Exit
              """
        )

    @staticmethod
    def display_user_acc_menu():
        print(
            """
              Please pick an option:
              1. Change username
              2. Change password
              3. Change email
              4. Change phone number
              5. Change recovery question
              6. Go back to previous menu
              7. Go to main menu
              """
        )

    @staticmethod
    def user_book_menu():
        print(
            """
            
            BOOK MENU
            
            1. Book library display
            2. Book(s) search by ISBN/author/title/genre
            3. Check book location
            4. Borrow book
            5. Return book
            6. Go back to previous Menu
            77. Go to Main Menu
            
            """
        )

    @staticmethod
    def user_borrowed_book_menu():
        print(
            """
            BORROWED BOOKS MENU
            
            1. What books is the User borrowing?
            2. Display due dates
            3. Go back to previous Menu
            77. Go back to Main Menu
            
            """
        )
