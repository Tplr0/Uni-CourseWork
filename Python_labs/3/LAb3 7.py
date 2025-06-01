Basic = int(input("Please input your basic: "))  # getting input of basic
TA = 200
DA = (Basic / 100) * 70
HRA = (Basic / 100) * 20
Grade_pay = Basic * 2  # Calculating TA DA HRA and grade pay

salary = Grade_pay + DA + TA + HRA  # calculating the salary

print("Your salary is: ", salary)  # printing the salary
