import admin
import User
# import admin and user to direct the user to admin or user login


def mainmenu():
    while True:
        print("\nMain Menu:")
        print("-------------------")
        print("1) Login as admin")
        print("2) Login as user")
        print("3) Sign up as new user")
        print("4) Exit Program")
        choice = input("Enter your choice: ")
        # User is directed to admin login if they input 1 or user login if they input 2

        if choice == '1':
            admin.login()
            pass
        elif choice == '2':
            User.user_menu()
            pass
        elif choice == '3':
            User.usersignup()
            pass
        elif choice == '4':
            print("System exited")
            exit()  
            # User is exited from the system
        else:
            print("Invalid Choice!")
            mainmenu()


#  starting the program
mainmenu()
