def main():
    input_name = input("Please enter your name: ")
    input_money = int(input("Please enter how much you make in a year: "))
    return input_name, input_money

def second(name, money):
    if money >= 50000:
        print("Congratulations, {}! You made more than RM50,000 this year.".format(name))
    else:
        print("Unfortunately, {} did not make more than RM50,000 this year. Better luck next year!".format(name))

name, money = main()
second(name, money)

