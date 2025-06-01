StuNum = int(input("Please input the number of student marks that will be entered: "))
counter = 0
Smarks = []
Snames = []

for i in range(StuNum):
    Snames.append(str(input("Please input a students names: "))) # appending the students names to the list

    while True:
        try:
            Smarks.append(int(input("Please input a students mark: "))) # appending the students marks to the list
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while not 0 <= Smarks[i] <= 100:
        Snames.pop(i)
        Smarks.pop(i)
    else:
        counter += 1
average = sum(Smarks) / len(Smarks)


print("Valid marks entered: ", counter)
print("The average mark is: ", average)