
# Define variables
a = 1 # Initial attempt
b = 1 # Initial correct attempt

num_list = []

def function_print():
    print('The numbers are:', num_list[0], num_list[1], num_list[2])
    mean = sum(num_list) / 3
    print('The mean is', mean)
    num_list.sort()
    print('The sum of the largest two numbers is', num_list[1] + num_list[2])

while True:
    value = input(f'Attempt {a}: Enter a non-negative integer: ')
    a += 1 # Increment attempt counter
    if value.isdigit(): # Check if it's a string of digits
        num = int(value) # Convert the string to an integer
        if num >= 0:
            num_list.append(num)
            if len(num_list) == 3:
                function_print()
                break
    else: # Error Check
        b = a # Reset correct attempt counter