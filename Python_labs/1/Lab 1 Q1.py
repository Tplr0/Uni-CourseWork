#Three steps that a program typically performs:
# Gather input data:
# from keyboard / from files on disk drives
# Process the input data
# Display the results as output:
# send it to the screen / write to a file

#Calculate area of rectangle

#print() # print to ask for the user to input length
length = int(input("Please input the length of the rectangle: ")) # user input the length of the rectangle

#print() # print to ask for the user to input width
width = int(input("Please input the width of the rectangle: ")) # user inputs the width of the rectangle

area = length*width # the area of the rectangle is calculated by multiplying the length and width inputted by the user

print("The area of this rectangle is:", area) # area is outputted
