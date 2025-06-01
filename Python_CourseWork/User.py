import __main__
from datetime import datetime
# importing main to direct the user to the main menu while needed
# Importing the datetime to let the user key in their date of birth


def user_menu():
    while True:
        print("\nUser Menu")
        print("---------------")
        print("1) Login with account")
        print("2) Sign up as new user")
        print("3) Exit to main menu")
        print("4) Exit program")

        # Could add one more option to let the user update their profile#
        # Letting the user chose to log in with their account, signing up as a new user,
        # exiting to the main menu or exiting the program
        choice = input("Enter your choice: ")
        if choice == "1":
            input_username_login, input_password_login, user_email = user_login()
            verify_login(input_username_login, input_password_login, user_email)
            # Directing the user to the log in loop
        elif choice == "2":
            usersignup()
            # Directing the new user to the signup loop
        elif choice == "3":
            __main__.mainmenu()
            # Directing the user to the main menu
            pass
        elif choice == "4":
            print("System exited")
            exit()
            # Exiting the system
        else:
            print("Invalid Choice!")
            # Looping back to user menu to let the user choose the options again when they mistype
            user_menu()


def user_blocked():
    while True:
        print("\nUser is blocked from login.\nPlease contact admin to unblock the account.")
        print("Redirecting to user menu .....")
        user_menu()
        pass


def user_login():
    while True:
        print("\nUser Login")
        print("-----------------")
        input_username_login = input("Enter your username:")
        input_password_login = input("Enter your password:")
        with open('userlogin.txt', 'r') as f:
            lines = f.readlines()

        for line in lines:
            line_parts = line.strip().split(':')
            email_us = line_parts[6]
        user_email = email_us
        return input_username_login, input_password_login, user_email
    # Separate the user login and verify login into different functions so that username input can be returned and used
    # later


def verify_login(input_username_login, input_password_login, user_email):
    with open('userlogin.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        line_parts = line.strip().split(':')
        username = line_parts[0]
        password = line_parts[1]
        is_blocked = line_parts[7]

        if username == input_username_login and password == input_password_login:
            # Access granted, perform admin actions
            # implement is blocked feature
            if is_blocked.lower() == "yes":
                user_blocked()
            else:
                user_main_menu(input_username_login, user_email)  # directs the user to user hall menu

    # Access denied, inform the user
    print("Invalid login!")

    while True:
        # Let the user choose if they want to go back to the user menu
        choice = input("\nDo you want to go back to user menu? [Yes/ No]:")
        if choice.lower() in ["y", "yes", "ye"]:
            user_menu()
        elif choice.lower() in ["n", "no"]:
            input_username_login, input_password_login, email = user_login()
            verify_login(input_username_login, input_password_login, user_email)
        else:
            print("Invalid choice. Please enter 'Yes' or 'No'.")


def usersignup():
    while True:
        # Let the user key in the details required for a profile including the username, password, first and last name,
        # date of birth, contact number and email address
        input_username = input("\nPlease enter the desired username: ")
        with open("userlogin.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            user_info = line.split()
            if user_info[0] == input_username:
                print("Username already taken. Please chose a different username.")
                usersignup()
        input_password = input("Please enter the password you want: ")
        input_first_name = input("Please enter your first name: ")
        input_last_name = input("Please enter your last name: ")
        # a while loop and a try ... except loop used to let the user enter the year-month-day format that will be
        # saved into the text file

        while True:
            date_birth_input = input("Please input your date of birth (YYYY-MM-DD): ")
            try:
                date_birth = datetime.strptime(date_birth_input, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use the year-month-day (YYYY-MM-DD) Number format.")
        contact_number = input("Please enter your contact number: ")

        # Letting the user inputting their email address and checking if the email address has @ in it
        email_address = input("Please enter your email address: ")
        while '@' not in email_address:
            print("\nPlease enter a valid email address.")
            email_address = input("Please enter your email address: ")
        is_blocked = "no"

        # Opening the userlogin.txt file (if it exists and create the file if it doesn't exist) as f
        # and writing all the signup information into the text file to save it
        # The text file should close right after all the information is saved
        with open("userlogin.txt", "a") as f:
            f.write(
                f"{input_username}:{input_password}:{input_first_name}:{input_last_name}:"
                f"{date_birth}:{contact_number}:{email_address}:{is_blocked}\n")

        print("Thank you for signing up!")
        print("Redirecting you to user login ..... ")
        input_username_login, input_password_login, user_email = user_login()
        verify_login(input_username_login, input_password_login, user_email)
        # redirecting the user to the login page after they sign up


def user_main_menu(input_username_login, user_email):
    while True:
        print("\nUser Hall Menu")
        print("----------------")
        print("1) Book a venue")
        print("2) View booking information")
        print("3) Delete/ Cancel a booking")
        print("4) Edit booking information")
        print("5) Search for booking information")
        print("6) Update user profile information")
        print("7) Go back to main menu")
        print("8) Back to user menu")
        print("9) Exit program\n")
        # Let the user chose which function they want to use after login (Still in progress)

        choice = input("Enter your choice: ")
        if choice == '1':
            hall_booking(input_username_login, user_email)
            pass
        elif choice == '2':
            view_booking_info(input_username_login, user_email)
            pass
        elif choice == '3':
            delete_booking_info(input_username_login, user_email)
            pass
        elif choice == '4':
            edit_booking_info(input_username_login, user_email)
            pass
        elif choice == '5':
            search_booking_info(input_username_login, user_email)
            pass
        elif choice == '6':
            update_profile(input_username_login)
            # print("Coming Soon")
            pass
        elif choice == '7':
            __main__.mainmenu()
            pass
        elif choice == '8':
            user_menu()
        elif choice == '9':
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            print("Please choose again!")
            user_main_menu(input_username_login, user_email)
            # if the user typed in an invalid option it loops back to the user hall menu to let the user retype


def update_profile(input_username_login):
    # To let the user update their profile (changing password or username for example)
    with open("userlogin.txt", "r") as f:
        lines = f.readlines()

    found = False
    for i, line in enumerate(lines):
        user_info = line.strip().split(':')
        if user_info[0] == input_username_login:
            found = True
            break

    if not found:
        print("No such user found. Please check your username and try again.")
        return

    while True:
        print("\nWelcome to the Update Profile Page.")
        print(f"1) Current username: {user_info[0]}")
        print(f"2) Current password: {user_info[1]}")
        print(f"3) Current first name: {user_info[2]}")
        print(f"4) Current last name: {user_info[3]}")
        print(f"5) Current date of birth: {user_info[4]}")
        print(f"6) Current contact number: {user_info[5]}")
        print(f"7) Current email address: {user_info[6]}")

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
    print("Redirecting you back to user menu .....")
    user_menu()


def hall_booking(input_username_login, user_email):
    while True:
        print("\nWelcome to hall booking page")
        print("---------------------------------")
        event_name = input("Please input the event's name: ")
        event_description = input("Please input the event's description: ")

        try:
            with open('hallinfo.txt', 'r') as f:
                hall_ids = [line.strip().split(';')[0] for line in f]
                if hall_ids:
                    print("\nThese are all the available Hall IDs:")
                    for hall_id in hall_ids:
                        print(hall_id)
                        if "Audi" in hall_id:
                            print("RM300 per hour")
                        elif "Banquet" in hall_id:
                            print("RM100 per hour")
                        elif "Meeting" in hall_id:
                            print("RM50 per hour")
                        else:
                            print("Hall price is not updated, please contact an admin to proceed")
                else:
                    print("No existing hall IDs.")

            while True:
                hall_id = input("Please input the hall ID: ")
                if hall_id in hall_ids:
                    break
                else:
                    print("Invalid hall ID. Please enter a valid hall ID.")

        except FileNotFoundError:
            print("Error: hallinfo.txt not found.")
            return

        number_of_pax = input("Please input the number of pax that will attend: ")

        while True:
            date_of_renting = input("Please input the date of renting (YYYY-MM-DD): ")
            try:
                date_renting = datetime.strptime(date_of_renting, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use the year-month-day (YYYY-MM-DD) format.")

        while True:
            try:
                time_of_renting = input("Please input the time of renting (Time in 24-hour HH:MM format): ")
                time_renting = datetime.strptime(time_of_renting, "%H:%M").time()
                break
            except ValueError:
                print("Invalid input format. Please use the 24-hour (HH:MM) format.")

        while True:
            try:
                hour_of_renting = int(input("Please input how many hours you are renting the hall for: "))
                break
            except ValueError:
                print("Invalid input! Please input an integer value of how many hours the hall will be booked.")

        if "Audi" in hall_id:
            price = int(300)
        elif "Banquet" in hall_id:
            price = int(100)
        elif "Meeting" in hall_id:
            price = int(50)

        payment_price = hour_of_renting * price

        with open("bookinginfo.txt", "a") as f:
            f.write(f"{event_name};{event_description};{hall_id};{number_of_pax};{date_renting};{time_renting}"
                    f";{payment_price};{input_username_login};{user_email}:{hour_of_renting}\n")

        print("Hall booked successfully!")

        # After booking, ask the user if they want to go back to the user menu
        choice = input("\nDo you want to go back to the user menu? [Yes/No]: ").lower()
        if choice in ["yes", "y"]:
            user_main_menu(input_username_login, user_email)
            break
        elif choice in ["no", "n"]:
            continue
        else:
            print("Invalid choice. Please enter 'Yes' or 'No'.")


def view_booking_info(input_username_login, user_email):
    print(f"\nView {input_username_login}'s booking info")
    print("---------------------------------------------")
    search_term = input_username_login
    with open('bookinginfo.txt', 'r') as f:
        lines = f.readlines()
        found = False
        for i, line in enumerate(lines):
            booking_info = line.strip().split(';')
            if search_term in line:
                found = True
                print("\n{}'s booking information".format(input_username_login))
                print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                    "Event name", "Hall id", "Number of pax", "Date of renting",
                    "Time of renting", "Payment price", "Username", "Event description",
                    "Email", "Hours of renting"))
                print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format(
                    *booking_info[:8]))

        if not found:
            print("No booking found with this user.")

    print("---------------------------------------------")  # Move this line outside the loop

    choice = input("\nDo you want to go back to the user menu? [Yes/No]: ")
    if choice.lower() in ["y", "yes"]:
        user_main_menu(input_username_login, user_email)
    elif choice.lower() in ["n", "no"]:
        view_booking_info(input_username_login, user_email)
    else:
        print("Invalid choice. Please enter 'Yes' or 'No'.")


def delete_booking_info(input_username_login, user_email):
    while True:
        print("\nDelete booking information")
        print("----------------------------")
        search_term = input_username_login
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
                user_main_menu(input_username_login, user_email)
            elif choice.lower() in ["n", "no"]:
                delete_booking_info(input_username_login, user_email)
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")


def edit_booking_info(input_username_login, user_email):
    while True:
        print("\nEdit booking information")
        print("----------------------------")
        search_term = input_username_login
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
                        print(f"9) Email Address: {booking_info[8]}")
                        print(f"10)Hours of renting: {booking_info[9]}")

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
                            lines[i] = ';'.join([booking_info[0], booking_info[1], booking_info[2],
                                                 booking_info[3], booking_info[4], booking_info[5],
                                                 booking_info[6], booking_info[7],
                                                booking_info[8], booking_info[9]]) + '\n'
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
                user_main_menu(input_username_login, user_email)
            elif choice.lower() in ["no", "n"]:
                edit_booking_info(input_username_login, user_email)
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")


def search_booking_info(input_username_login, user_email):
    while True:
        print("\nSearch Booking Information")
        print("------------------------")
        search_term = input("Please input the username or the hall id your are searching for: ")
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
                user_main_menu(input_username_login, user_email)
            elif choice.lower() in ["n", "no"]:
                search_booking_info(input_username_login, user_email)
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")

