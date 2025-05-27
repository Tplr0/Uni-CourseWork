tuple1 = (2, 4, 5)  #
print(sum(tuple1))

turtle =(1, "Hello")
turtle2 = (5, )
turtle3 = ("single", )
turtle += turtle2
turtle += turtle3
print(turtle)

tup1 = ("single", "hello", "no", "why")
str1 = ''
for item in tup1:
    str1 = str1 + item
print(str1)

l = ["why", "huh", 6, "lmao",]
print(l)
print(type(l))
t = tuple(l)
print(t)
print(type(t))

# Create a tuple containing a sequence of items
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# Check if the character "r" is present in the 'tuplex' tuple and print the result
print("r" in tuplex)
# Check if the number 5 is present in the 'tuplex' tuple and print the result
print(5 in tuplex)

tuple3 = (23, 45, 65, 78, 98, 9, 45, 56, 43)
print(tuple3[-1::-1])