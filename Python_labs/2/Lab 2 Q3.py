number_list = []

for i in range(1, 4):
    print("Enter number ", i, )
    list = int(input())
    number_list.append(list)
print("The numbers you entered are,", number_list)
number_list.sort()

print("The largest number from the list is,", number_list[2])