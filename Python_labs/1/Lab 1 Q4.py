#Three steps that a program typically performs:
# Gather input data:
# from keyboard / from files on disk drives
# Process the input data
# Display the results as output:
# send it to the screen / write to a file

#Calculate area and circumference of circle.
import math
pi = 3.141592653589793238462643383279502884197 # adds the value pi into the code because not importing math from system

radius = int(input("Please input the radius of the circle: ")) #lets the user inputs the radius

area = math.pi * (radius * radius) #calculate the area of the circle

circumference = (2 * math.pi) * radius # calculates the circumference of the circle

print(f"The area of the circle is : {area:.2f}") # prints the area of the circle and rounds the answer to 2 decimal points

print(f"The circumference of the circle is: {circumference:.2f}" ) #prints the circumference and rounds the answer to 2 decimal points





