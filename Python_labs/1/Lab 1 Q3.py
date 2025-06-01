#Three steps that a program typically performs:
# Gather input data:
# from keyboard / from files on disk drives
# Process the input data
# Display the results as output:
# send it to the screen / write to a file\

#. Receive an integer from the user, add 5 to it, double it, subtract 7 from it, and display the final number on the screen

int1 = int(input("Please input an integer: ")) # lets the user inputs an integer to be calulated

int2 = ((int1 + 5)*2) - 7 # the integer is added by 5, then doubled and substracted by 7


print("The final number is: ", int2) # print the final number of the integer

