#Three steps that a program typically performs:
# Gather input data:
# from keyboard / from files on disk drives
# Process the input data
# Display the results as output:
# send it to the screen / write to a file


#Calculate employee income tax based on the following formula:
#Tax = 0.25 * (monthly income * 11 – number of kids * 450)
#Your program will display the name of the employee and amount of tax on the screen.

name = str(input("Please input your name: ")) # This function lets the user inputs their name

monthly_income = float(input("Please input your monthly income: ")) # this function ask the user to input the users month;y income

no_of_kids = int(input("Please input the number of kids you have: ")) # this function ask the users how many kids they have

Tax = 0.25 * (monthly_income * 11 - no_of_kids * 450) # this function calculates the amout of tha=x needed to be paid by the user



# these function gathers all the previous inputs of the user and prints the user name and the calculated tax
print("Your name is:", name)
print(f"And your amount of tax needed to be paid is: {Tax:.2f}") # the f function rounds the tax to 2 decimal points and show the decimal points



#print("And your amount of tax needed to be paid is: ", round(Tax, 2))