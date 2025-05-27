mlist = []  # creating a list#

for i in range(1, 6):
    list1 = int(input("Please input a students mark: "))  # letting user input the students marks
    mlist.append(list1)  # placing the user input into the list

sum1 = sum(mlist)

average = sum1 / 5  # summing the marks and dividing by 5 to calculate the average marks
print("Total marks: ", sum1, "%")
print("The average marks of the students is: ", average, "%")  # printing the average
