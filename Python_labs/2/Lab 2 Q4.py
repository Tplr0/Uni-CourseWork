year1 = int(input("Please enter a year: "))
year = year1 - 1900
#print(year)
while year > 0:
    year = year - 4

    if year == 0:
        print("This is a leap year!")
        break
    elif year < 0:
        print("This is not a leap year!")
        break