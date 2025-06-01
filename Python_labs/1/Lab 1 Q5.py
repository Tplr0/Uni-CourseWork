#Three steps that a program typically performs:
# Gather input data:
# from keyboard / from files on disk drives
# Process the input data
# Display the results as output:
# send it to the screen / write to a file

#Calculate and print the average of three numbers: 20, 10, and 2.

List = [20,10,2] # enters a list of numbers

c = len(List) # get the number of numbers on the list to calculate the average
#print(c)

av = List[0] + List[1] + List[2] # adding all the list numbers together to calculate the average later

average = (av)/c # to calculate the average all the numbers are added together and divided by the number of numbers on the list

print("The average is: ", average) #printing the average

print(f"The average in 2 decimal points is:  {average:.2f}") #printing the average in 2 decimal points
