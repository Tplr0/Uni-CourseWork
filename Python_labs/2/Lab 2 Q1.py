import time

Unumber = int(input("Enter a number: "))
print(Unumber)
while Unumber >= 0:
    time.sleep(1)
    Unumber -= 1
    print(Unumber)
    if Unumber == 0:
        break