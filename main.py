# operator in python are "and" and "or" instead of && and ||
# also you can do checks like in line 9
# instead of != is possible to use "not"

age = int(input("How old are you? "))

if age >= 18 and age != 100:
    print("You are an adult!")
elif 18 > age > 0:
    print("You are a child!")
elif age == 100:
    print("You are a century man!")
else:
    print("You cannot have negative age!")

name = ""

while len(name) == 0:
    name = input("Enter your name: ").capitalize()

print("Hello " + name)

nickname = None  # None is the equivalent of "null"

while not nickname:
    nickname = input("Enter your nickname: ").capitalize()

print("Your nickname is: " + nickname)