import random
import math

in1 = int(input("Please input the smallest number of the range: "))
in2 = int(input("Please input the largest number of the range: "))
number = random.randint(in1, in2)
range_1 =(in1, in2, number)


count = 0
while count < math.log(in2 - in1 + 1, 2):
    count += 1
    print("Press n")
    guess = input("Guess a number: ")

    if number == guess:
        print("Congratulations you did it in", count, "try")

        break
    if number > guess:
        print("You guessed too small!")
    if number < guess:
        print("You Guessed too high!")

