import __main__
from datetime import datetime
# importing main to direct the user to the main menu while needed
# Importing the datetime to let the user key in their date of birth


def login():
    while True:
        print("\nAdmin Login")
        print("-----------------")
        inputun = input("Enter your username:")
        inputpwd = input("Enter your password:")
        with open('adminlogin.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            line_parts = line.strip().split()
            username = line_parts[0]
            password = line_parts[1]
            if username == inputun and password == inputpwd:
                # Access granted, perform admin actions
                admin_menu()  # directs the user to admin hall menu
                return
        # Access denied, inform the user
        print("Invalid login!")
        while True:
            # Let the user choose if they want to go back to the main menu
            choice = input("\nDo you want to go back to the main menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                __main__.mainmenu()
            elif choice.lower() in ["n", "no"]:
                login()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def admin_menu():
    while True:

        print("\nAdmin Menu")
        print("----------------")
        print("1) Hall Information management")
        print("2) Booking management")
        print("3) User management")
        print("4) Go back to main menu")
        print("5) Back to admin login")
        print("6) Exit program")
        # Let the user chose which function they want to use after login (Still in progress)

        choice = input("Enter your choice: ")
        if choice == '1':
            hall_info_management()
            # print("Coming Soon")
            pass
        elif choice == '2':
            booking_management()
            # print("Coming Soon")
            pass
        elif choice == '3':
            user_management()
            # print("Coming Soon")
            pass
        elif choice == '4':
            __main__.mainmenu()
            pass
        elif choice == '5':
            login()
        elif choice == '6':
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            admin_menu()


def hall_info_management():
    while True:

        print("\nHall information management")
        print("----------------")
        print("1) Enter Hall Information")
        print("2) View all the hall information")
        print("3) Search for hall information")
        print("4) Edit hall information")
        print("5) Delete hall information")
        print("6) Go back to main menu")
        print("7) Back to admin menu")
        print("8) Exit program")
        # Let the user chose which function they want to use after login (Still in progress)

        choice = input("Enter your choice: ")
        if choice == '1':
            enter_hall_info()

        elif choice == '2':
            view_hall_info()

            pass
        elif choice == '3':
            search_hall_info()

            pass
        elif choice == '4':
            edit_hall_info()
            # print("Coming Soon")
            pass
        elif choice == '5':
            delete_hall_info()

            pass
        elif choice == '6':
            __main__.mainmenu()
            pass
        elif choice == '7':
            admin_menu()
        elif choice == '8':
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            hall_info_management()


def user_management():
    # print("NO")
    while True:

        print("\nUser management")
        print("----------------")
        print("1) View all user information")
        print("2) Search user information using the first or last name")
        print("3) Edit user information")
        print("4) Delete user")
        print("5) Block user from login")
        print("6) Go back to main menu")
        print("7) Back to admin menu")
        print("8) Exit program")
        # Let the user chose which function they want to use after login (Still in progress)

        choice = input("Enter your choice: ")
        if choice == '1':
            view_user_info()
            # print("Coming Soon")
            pass
        elif choice == '2':
            search_user_info()
            # print("Coming Soon")
            pass
        elif choice == '3':
            edit_user_profile()
            # print("Coming Soon")
            pass
        elif choice == '4':
            delete_user()
            # print("Coming Soon")
            pass
        elif choice == '5':
            block_user()
            pass
        elif choice == '6':
            __main__.mainmenu()
            pass
        elif choice == '7':
            admin_menu()
        elif choice == '8':
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            user_management()


def booking_management():
    # print("NO")
    while True:
        print("\nBooking management")
        print("----------------")
        print("1) View all booking information")
        print("2) Search the booking information using the username or email")
        print("3) Edit booking information")
        print("4) Delete/Cancel the booking information")
        print("5) Go back to main menu")
        print("6) Back to admin menu")
        print("7) Exit program")
        # Let the user chose which function they want to use after login (Still in progress)

        choice = input("Enter your choice: ")
        if choice == '1':
            view_booking_info()
            pass
        elif choice == '2':
            search_booking_info()
            pass
        elif choice == '3':
            edit_booking_info()
            pass
        elif choice == '3':
            delete_booking_info()
            pass
        elif choice == '5':
            __main__.mainmenu()
            pass
        elif choice == '6':
            admin_menu()
        elif choice == '7':
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            booking_management()


def enter_hall_info():
    # print("NO")

    print("\nEnter Hall Information")
    print("------------------------")

    hall_id = input("Hall ID: ")
    hall_name = input("Hall Name: ")
    hall_description = input("Hall Description: ")
    while True:
        try:
            hall_pax = int(input("Hall maximum pax: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer")
    while True:
        try:
            hall_availability_date = input("Hall Availability Status (Date in (YYYY-MM-DD)): ")
            hall_availability_date = datetime.strptime(hall_availability_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use the year-month-day (YYYY-MM-DD) date format.")
    while True:
        try:
            hall_availability_time_first = input("Hall Availability Status Opening time "
                                                 "(Time in 24 hour HH:MM format): ")
            hall_availability_time_first = datetime.strptime(hall_availability_time_first, "%H:%M").time()
            break
        except ValueError:
            print("Invalid input format. Please use the 24 hour(HH:MM) format.")

    while True:
        try:
            hall_availability_time_last = input("Hall Availability Status Closing time (Time in 24 hour "
                                                "HH:MM format): ")
            hall_availability_time_last = datetime.strptime(hall_availability_time_last, "%H:%M").time()
            break
        except ValueError:
            print("Invalid input format. Please use the 24 hour(HH:MM) format.")
    while True:
        try:
            rate_price = int(input("Rate price per hour (RM): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer")

    with open('hallinfo.txt', 'a') as f:
        f.write(f"{hall_id};{hall_name};{hall_description};{hall_pax};{hall_availability_date};"
                f"{hall_availability_time_first};{hall_availability_time_last};{rate_price}\n")

    print("Hall information added successfully.")
    while True:
        # Let the user choose if they want to go back to the user menu
        choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
        if choice.lower() in ["y", "yes", "ye"]:
            admin_menu()
        elif choice.lower() in ["n", "no"]:
            enter_hall_info()
        else:
            print("Invalid choice. Please enter 'Yes' or 'No'.")
    # Can add a verification to see if admin wants to add more or go back to admin menu/ hall management


def view_hall_info():
    #  print("NO")
    # Can add a small Ui when outputting the hall information
    print("\nView All Hall Information")
    print("------------------------")
    with open('hallinfo.txt', 'r') as f:
        lines = [line.strip().split(";") for line in f.readlines()]
        # print(line.strip(":"))
        hallnum = 0
        while hallnum < len(lines):
            print("This is hall number:", hallnum + 1)
            print(f"Hall id: {lines[hallnum][0]}")
            print(f"Hall name: {lines[hallnum][1]}")
            print(f"Hall description: {lines[hallnum][2]}")
            print(f"Hall maximum pax: {lines[hallnum][3]}")
            print(f"Hall date: {lines[hallnum][4]}")
            print(f"Hall time(Open): {lines[hallnum][5]}")
            print(f"Hall time(close): {lines[hallnum][6]}")
            print(f"Hall rate price (Per Day): {lines[hallnum][7]}")

            view_choice = input("\nType 'done' to exit viewing hall info\n"
                                "Type 'next' to see the next hall info: ")

            if view_choice.lower() == 'done' or view_choice.lower() == '0':
                print("Exiting back to admin menu!")
                admin_menu()
                break
            elif view_choice.lower() == 'next':
                hallnum += 1
            else:
                print("Invalid choice. Please type 'done' or 'next'.")


def search_hall_info():
    #  print("NO")
    # Can add a small Ui when outputting the hall information
    while True:
        print("\nSearch Hall Information")
        print("------------------------")
        search_term = input("Enter search term: ")
        with open('hallinfo.txt', 'r') as f:
            lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                hall_info = line.strip().split(':')
                if search_term in line:
                    found = True
                    # print(line.strip(":"))
                    # f"{hall_id}:{hall_name}:{hall_description}:{hall_pax}:{hall_availability_date}:"
                    # f"{hall_availability_time}:{rate_price}\n"
                    while True:
                        print(f"Hall id: {hall_info[0]}")
                        print(f"Hall name: {hall_info[1]}")
                        print(f"Hall description: {hall_info[2]}")
                        print(f"Hall maximum pax: {hall_info[3]}")
                        print(f"Hall date: {hall_info[4]}")
                        print(f"Hall time(Open): {hall_info[5]}")
                        print(f"Hall time(Close): {hall_info[6]}")
                        print(f"Hall rate price (Per Day): {hall_info[7]}")
                        break
            if not found:
                print("No matching hall information found.")
        while True:
            # Let the user choose if they want to go back to the user menu
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                search_hall_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def edit_user_profile():
    # To let the admin update a user's profile (changing password or username for example)
    username = input("Please enter the user's username: ")
    with open("userlogin.txt", "r") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        user_info = line.strip().split(':')
        if user_info[0] == username:
            found = True
            break
    if not found:
        print("No such user found. Please check the user's username and try again.")
        return
    while True:
        print("\nWelcome to User Profile Edit Page.")
        print(f"1) Current username: {user_info[0]}")
        print(f"2) Current password: {user_info[1]}")
        print(f"3) Current first name: {user_info[2]}")
        print(f"4) Current last name: {user_info[3]}")
        print(f"5) Current date of birth: {user_info[4]}")
        print(f"6) Current contact number: {user_info[5]}")
        print(f"7) Current email address: {user_info[6]}")
        # print(f"8) ")

        update_choice = input("\nPlease enter the number of the detail you want to update. "
                              "Type 'done' or '0' to finish updating. ")
        if update_choice.lower() == 'done' or update_choice.lower() == '0':
            print("Exiting profile!")
            break
        elif update_choice == '1':
            new_username = input("Please enter the new username: ")
            user_info[0] = new_username
        elif update_choice == '2':
            new_password = input("Please enter the new password: ")
            user_info[1] = new_password
        elif update_choice == '3':
            new_first_name = input("Please enter the new first name: ")
            user_info[2] = new_first_name
        elif update_choice == '4':
            new_last_name = input("Please enter the new last name: ")
            user_info[3] = new_last_name
        elif update_choice == '5':
            while True:
                new_date_birth_input = input("Please input your date of birth (YYYY-MM-DD): ")
                try:
                    new_date_birth = datetime.strptime(new_date_birth_input, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format. Please use the year-month-day (YYYY-MM-DD) Number format.")
            user_info[4] = str(new_date_birth)
        elif update_choice == '6':
            new_contact_number = input("Please enter the new contact number: ")
            user_info[5] = new_contact_number
        elif update_choice == '7':
            new_email_address = input("Please enter the new email address: ")
            user_info[6] = new_email_address
        else:
            print("Invalid choice. Please enter the number of the detail you want to update.")

    # Updating the user_info in the lines list
    lines[i] = ":".join(user_info) + "\n"

    # Writing the updated user information back to the userlogin.txt file
    with open("userlogin.txt", "w") as f:
        f.writelines(lines)

    print("Profile updated successfully!")
    print("Redirecting you back to admin menu .....")
    admin_menu()


def delete_hall_info():
    while True:
        print("\nDelete Hall Information")
        print("------------------------")
        search_term = input("Enter search term: ")
        with open('hallinfo.txt', 'r') as f:
            lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                hall_info = line.strip().split(';')
                if search_term in line:
                    found = True
                    while True:
                        print("Do you want to delete this hall:")
                        print(f"Hall id: {hall_info[0]}")
                        print(f"Hall name: {hall_info[1]}")
                        print(f"Hall description: {hall_info[2]}")
                        print(f"Hall maximum pax: {hall_info[3]}")
                        print(f"Hall date: {hall_info[4]}")
                        print(f"Hall time(Open): {hall_info[5]}")
                        print(f"Hall time(Close): {hall_info[6]}")
                        print(f"Hall rate price (Per Day): {hall_info[7]}")

                        confirm_delete = input("Type 'yes' to confirm deletion, 'no' to cancel: ")
                        if confirm_delete.lower() in ["y", "yes", "ye"]:
                            # Delete the hall information
                            del lines[i]
                            # Write the modified lines back to the file
                            with open('hallinfo.txt', 'w') as file:
                                file.writelines(lines)
                            print("Hall information deleted successfully.")
                            break
                        elif confirm_delete.lower() in ["n", "no"]:
                            print("Deletion canceled.")
                            break
                        else:
                            print("Invalid choice. Please type 'yes' or 'no'.")
            if not found:
                print("No matching hall information found.")

        while True:
            choice = input("\nDo you want to go back to the admin menu? [Yes/ No]: ")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                delete_hall_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def edit_hall_info():
    while True:
        print("\nEdit Hall Information")
        print("------------------------")
        search_term = input("Enter search term(Hall Id or Hall name): ")
        with open('hallinfo.txt', 'r') as f:
            lines = f.readlines()

        found = False
        for i, line in enumerate(lines):
            hall_info = line.strip().split(';')
            if hall_info[1] or hall_info[0] == search_term:
                found = True
                break

        if not found:
            print("No such hall found. Please check the hall information and try again.")
            return

        while True:
            print("\nWelcome to the Edit Hall Information page.")
            print(f"Hall id: {hall_info[0]}")
            print(f"Hall name: {hall_info[1]}")
            print(f"Hall description: {hall_info[2]}")
            print(f"Hall maximum pax: {hall_info[3]}")
            print(f"Hall date: {hall_info[4]}")
            print(f"Hall time(Open): {hall_info[5]}")
            print(f"Hall time(Close): {hall_info[6]}")
            print(f"Hall rate price (Per Day): {hall_info[7]}")

            update_choice = input("\nPlease enter the number of the detail you want to update. "
                                  "Type 'done' or '0' to finish updating: ")

            if update_choice.lower() == 'done' or update_choice == '0':
                print("Exiting hall profile!")
                break
            elif update_choice == '1':
                new_hall_id = input("Please enter the new hall id: ")
                hall_info[0] = new_hall_id
            elif update_choice == '2':
                new_hall_name = input("Please enter the new hall name: ")
                hall_info[1] = new_hall_name
            elif update_choice == '3':
                new_hall_description = input("Please enter the new hall description: ")
                hall_info[2] = new_hall_description
            elif update_choice == '4':
                while True:
                    try:
                        new_max_pax = int(input("Please enter the new maximum pax: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                hall_info[3] = str(new_max_pax)
            elif update_choice == '5':
                while True:
                    new_hall_date_input = input("Please enter the new hall date (YYYY-MM-DD): ")
                    try:
                        new_hall_date = datetime.strptime(new_hall_date_input, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid date format. Please use the year-month-day (YYYY-MM-DD) format.")
                hall_info[4] = str(new_hall_date)
            elif update_choice == '6':
                new_open_time = input("Please enter the new open time (HH:MM): ")
                try:
                    new_open_time = datetime.strptime(new_open_time, "%H:%M").time()
                    hall_info[5] = str(new_open_time)
                except ValueError:
                    print("Invalid time format. Please use the HH:MM(24 hour) format.")
            elif update_choice == '7':
                new_close_time = input("Please enter the new close time (HH:MM): ")
                try:
                    new_close_time = datetime.strptime(new_close_time, "%H:%M").time()
                    hall_info[6] = str(new_close_time)
                except ValueError:
                    print("Invalid time format. Please use the HH:MM(24 hour) format.")
            elif update_choice == '8':
                while True:
                    try:
                        new_rate_price = int(input("Please enter the new rate price (Per Hour): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                hall_info[7] = str(new_rate_price)
            else:
                print("Invalid choice. Please enter the number of the detail you want to update.")

        # Updating the hall_info in the lines list
        lines[i] = ";".join(hall_info) + "\n"

        # Writing the updated hall information back to the hallinfo.txt file
        with open("hallinfo.txt", "w") as f:
            f.writelines(lines)
        while True:
            # Let the user choose if they want to go back to the user menu
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                edit_hall_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def view_user_info():
    while True:
        # can add a small ui in user info
        print("\nUser login information")
        print("---------------------------")
        with open("userlogin.txt", "r") as f:
            content = f.read()
            print(content)
        while True:
            # Let the user choose if they want to go back to the user menu
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                view_user_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def delete_user():
    while True:
        print("\nDelete user information")
        print("----------------------------")
        search_term = input("Enter search term: ")
        with open('userlogin.txt', 'r') as f:
            lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                user_info = line.strip().split(':')
                if search_term in line:
                    found = True
                    while True:
                        print("\nIs this the user's you are trying to delete?")
                        print(f"1) Current username: {user_info[0]}")
                        print(f"2) Current password: {user_info[1]}")
                        print(f"3) Current first name: {user_info[2]}")
                        print(f"4) Current last name: {user_info[3]}")
                        print(f"5) Current date of birth: {user_info[4]}")
                        print(f"6) Current contact number: {user_info[5]}")
                        print(f"7) Current email address: {user_info[6]}")

                        confirm_delete = input("Type 'yes' to confirm deletion, 'no' to cancel: ")
                        if confirm_delete.lower() in ["y", "yes", "ye"]:
                            # Delete the user information
                            del lines[i]
                            # Write the modified lines back to the file
                            with open('userlogin.txt', 'w') as file:
                                file.writelines(lines)
                            print("User information deleted successfully.")
                            break
                        elif confirm_delete.lower() in ["n", "no"]:
                            print("Deletion canceled.")
                            break
                        else:
                            print("Invalid choice. Please type 'yes' or 'no'.")
            if not found:
                print("No matching hall information found.")
                return
        while True:
            # Let the user choose if they want to go back to the user menu
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                delete_user()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def block_user():
    while True:
        print("\nBlock user information")
        print("----------------------------")

        username = input("Please enter the user's username: ")

        with open("userlogin.txt", "r") as f:
            lines = f.readlines()

        found = False
        for i, line in enumerate(lines):
            user_info = line.strip().split(':')
            if user_info[0] == username:
                found = True
                break

        if not found:
            print("No such user found. Please check the user's username and try again.")
            while True:
                choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
                if choice.lower() in ["y", "yes", "ye"]:
                    admin_menu()
                elif choice.lower() in ["n", "no"]:
                    block_user()
                else:
                    print("Invalid choice. Please enter 'Yes' or 'No'.")

        if user_info[7] == "no":
            action = "block"
        else:
            action = "unblock"

        print(f"\nIs this the user that you are trying to {action}.")
        # for j, info in enumerate(user_info, start=1):
        #     print(f"{j}) Current {info}")
        print(f"1) Current username: {user_info[0]}")
        print(f"2) Current password: {user_info[1]}")
        print(f"3) Current first name: {user_info[2]}")
        print(f"4) Current last name: {user_info[3]}")
        print(f"5) Current date of birth: {user_info[4]}")
        print(f"6) Current contact number: {user_info[5]}")
        print(f"7) Current email address: {user_info[6]}")

        confirm_block = input(f"Type 'yes' to {action} the user from login, 'no' to cancel: ")

        if confirm_block.lower() in ["y", "yes", "ye"]:
            if user_info[7] == "yes":
                user_info[7] = "no"
            elif user_info[7] == "no":
                user_info[7] = "yes"
            else:
                user_info[7] = "no"  # Toggle the confirmation status
            lines[i] = ":".join(user_info) + "\n"  # Update the specific line in the 'lines' list

            with open('userlogin.txt', 'w') as file:
                file.writelines(lines)

            print(f"User {action} status updated successfully.")
        elif confirm_block.lower() in ["n", "no"]:
            print(f"User {action} operation canceled.")
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

        while True:
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                block_user()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def search_user_info():
    while True:
        print("\nSearch user information")
        print("----------------------------")
        name = input("Please enter the user's first or last name: ")
        with open("userlogin.txt", "r") as f:
            lines = f.readlines()
        found = False
        for i, line in enumerate(lines):
            user_info = line.strip().split(':')
            if user_info[2] == name or user_info[3] == name:
                found = True
                break
        if not found:
            print("\nNo such user with this first or last name found. "
                  "\nPlease check the user's last or first name and try again.")
            while True:
                # Let the user choose if they want to go back to the admin menu
                choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
                if choice.lower() in ["y", "yes", "ye"]:
                    admin_menu()
                elif choice.lower() in ["n", "no"]:
                    search_user_info()
                else:
                    print("Invalid choice. Please enter 'Yes' or 'No'.")

        while True:
            print(f"\nThis is {user_info[0]}'s user information")
            print(f"Username: {user_info[0]}")
            print(f"Password: {user_info[1]}")
            print(f"First name: {user_info[2]}")
            print(f"Last name: {user_info[3]}")
            print(f"Date of birth: {user_info[4]}")
            print(f"Contact number: {user_info[5]}")
            print(f"Email address: {user_info[6]}")
            break
        while True:
            # Let the user choose if they want to go back to the user menu
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                search_user_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def view_booking_info():
    print(f"\nView all booking info")
    print("---------------------------------------------")
    search_term = str(print("Please input the username or the email: "))

    with open('bookinginfo.txt', 'r') as f:
        lines = f.readlines()
        found = False
        for i, line in enumerate(lines):
            booking_info = line.strip().split(';')
            if search_term in line[7] or line[8]:
                found = True
                print("\n{}'s booking information".format(search_term))
                print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                    "Event name", "Hall id", "Number of pax", "Date of renting",
                    "Time of renting", "Payment price", "Username", "Event description",
                    "Email", "Hours of renting"))
                print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                    *booking_info[:8]))

        if not found:
            print("No booking found with this user.")

    print("---------------------------------------------")  # Move this line outside the loop

    choice = input("\nDo you want to go back to the admin menu? [Yes/No]: ")
    if choice.lower() in ["y", "yes"]:
        admin_menu()
    elif choice.lower() in ["n", "no"]:
        view_booking_info()
    else:
        print("Invalid choice. Please enter 'Yes' or 'No'.")


def edit_booking_info():
    while True:
        print("\nEdit booking information")
        print("----------------------------")
        search_term = str(print("Please input the username or hall id: "))
        with open('bookinginfo.txt', 'r') as f:
            lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                booking_info = line.strip().split(';')
                if search_term in line:
                    found = True
                    while True:
                        print("\nCurrent booking information:")
                        print(f"1) Event name: {booking_info[0]}")
                        print(f"2) Hall ID: {booking_info[2]}")
                        print(f"3) Number of pax: {booking_info[3]}")
                        print(f"4) Date of renting: {booking_info[4]}")
                        print(f"5) Time of renting: {booking_info[5]}")
                        print(f"6) Payment price: {booking_info[6]}")
                        print(f"7) Username: {booking_info[7]}")
                        print(f"8) Event description: {booking_info[1]}")
                        print(f"8) Event description: {booking_info[1]}")
                        print(f"9) Hours of renting: {booking_info[9]}")

                        field_to_edit = input("Enter the number of the field to edit (1-8), or 'exit' to cancel: ")

                        if field_to_edit.lower() == 'exit':
                            print("Editing canceled.")
                            break

                        if not field_to_edit.isdigit() or int(field_to_edit) not in range(1, 9):
                            print("Invalid input. Please enter a number between 1 and 8.")
                            continue

                        new_value = input(f"Enter the new value for field {field_to_edit}: ")

                        # Update the selected field in the booking_info list
                        booking_info[int(field_to_edit) - 1] = new_value

                        print("\nUpdated booking information:")
                        print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                            "Event name", "Hall id", "Number of pax", "Date of renting",
                            "Time of renting", "Payment price", "Username", "Event description",
                            "Email", "Hours of renting"))
                        print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                            *booking_info))

                        save_changes = input("Do you want to save changes? (yes/no): ")
                        if save_changes.lower() in ["yes", "y"]:
                            # Update the line in the file with the modified booking_info
                            lines[i] = ';'.join([booking_info[0], booking_info[1], booking_info[2], booking_info[3],
                                                booking_info[4], booking_info[5], booking_info[6],
                                                 booking_info[7], booking_info[8], booking_info[9]]) + '\n'
                            with open('bookinginfo.txt', 'w') as file:
                                file.writelines(lines)
                            print("Changes saved successfully.")
                            break
                        elif save_changes.lower() in ["no", "n"]:
                            print("Changes not saved.")
                            break
                        else:
                            print("Invalid choice. Please enter 'yes' or 'no'.")
            if not found:
                print("No matching booking information found.")
                return

        # Let the user choose if they want to go back to the admin menu
        while True:
            choice = input("\nDo you want to go back to admin menu? (yes/no): ")
            if choice.lower() in ["yes", "y"]:
                admin_menu()
            elif choice.lower() in ["no", "n"]:
                edit_booking_info()
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")


def delete_booking_info():
    while True:
        print("\nDelete booking information")
        print("----------------------------")
        search_term = str(print("Please input the username or the hall id: "))
        with open('bookinginfo.txt', 'r') as f:
            lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                booking_info = line.strip().split(';')
                if search_term in line:
                    found = True
                    while True:
                        print("\nPress it is not the hall you are looking for")
                        print("It will cycle through all the booking you've made")
                        print("Is this the booking you are trying to delete?")
                        print(f"1) Event name: {booking_info[0]}")
                        print(f"2) Hall ID: {booking_info[2]}")
                        print(f"3) Number of pax: {booking_info[3]}")
                        print(f"4) Date of renting: {booking_info[4]}")
                        print(f"5) Time of renting: {booking_info[5]}")
                        print(f"6) Payment price: {booking_info[6]}")
                        print(f"7) Username: {booking_info[7]}")
                        print(f"8) Event description: {booking_info[1]}")
                        print(f"8) Event description: {booking_info[1]}")
                        print(f"9) Hours of renting: {booking_info[9]}")
                        confirm_delete = input("Type 'yes' to confirm deletion, 'no' to cancel: ")
                        if confirm_delete.lower() in ["y", "yes", "ye"]:
                            # Delete the booking information
                            del lines[i]
                            # Write the modified lines back to the file
                            with open('bookinginfo.txt', 'w') as file:
                                file.writelines(lines)
                            print("Booking information deleted successfully.")
                            break
                        elif confirm_delete.lower() in ["n", "no"]:
                            print("Deletion canceled.")
                            break
                        else:
                            print("Invalid choice. Please type 'yes' or 'no'.")
            if not found:
                print("No matching booking information found.")
                return

        # Let the user choose if they want to go back to the admin menu
        while True:
            choice = input("\nDo you want to go back to admin menu? [Yes/ No]: ")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                delete_booking_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def search_booking_info():
    while True:
        print("\nSearch Booking Information")
        print("------------------------")
        search_term = str(print("Please input the username or the email: "))
        with open('bookinginfo.txt', 'r') as f:
            lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                booking_info = line.strip().split(':')
                if search_term in line:
                    found = True
                    print("\nMatching booking information:")
                    print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                        "Event name", "Hall id", "Number of pax", "Date of renting",
                        "Time of renting", "Payment price", "Username", "Event description",
                        "Email", "Hours of renting"))
                    print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                        *booking_info))
                    break
            if not found:
                print("No matching booking information found.")

        while True:
            # Let the user choose if they want to go back to the user menu
            choice = input("\nDo you want to go back to user menu? [Yes/ No]:")
            if choice.lower() in ["y", "yes", "ye"]:
                admin_menu()
            elif choice.lower() in ["n", "no"]:
                search_booking_info()
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


# if __name__ == "__main__":
#     admin_menu()
