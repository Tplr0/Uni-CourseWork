num1 = int(input("Please input number 1: "))  # getting input for user for 2 numbers
num2 = int(input("Please input number 2: "))
operation = input(
    "please enter an arithmetic operation(+, -, *, /, %):")  # getting the arithmetic operation from the user

sum1 = num1 + num2  # doing arithmetic operation to the two inputs (+, -, *, /, %).
sub1 = num1 - num2
mult1 = num1 * num2
div1 = num1 / num2
mod1 = num1 % num2
if operation == "+":
    print("The sum of the numbers you entered is:", sum1)  # printing the sum
elif operation == "-":
    print("The subtraction of the numbers you entered is:", sub1)  # printing the subtraction
elif operation == "*":
    print("The multiplication of the numbers you entered is:", mult1)  # printing the multiplication
elif operation == "/":
    print("The division of the numbers you entered is:", div1)  # printing the division
elif operation == "%":
    print("The modulus of the numbers you entered is:", mod1)  # printing the modulus
