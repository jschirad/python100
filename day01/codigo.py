# My first codeline in python
print("Hello World!")
print("Hello"+" "+"Facu")
# Input () will get user input in console
print("What is your name?")
myName = input()
print("It is good to meet you, "+myName)
#----------------------------------------------------#

# First Challenge
print("Hello!")
print("First Challenge")
myName = input("What is your name? ")
print("It is good to meet you, "+myName)
print("The length of your name is: "+str(len(myName)))
#----------------------------------------------------#

# Second Challenge
print("Second Challenge")
a = input("Enter a number: a =")
b = input("Enter another number: b =")
# swap values
a, b = b, a
print("a is now: "+a)
print("b is now: "+b)
#----------------------------------------------------#

#Final task
print("Welcome to the Band Name Generator")
print("Where do you live?")
city = input()
print("What is your pet name?")
petname = input()
print("Your Band Name is: The " + city + " " + petname + " Band")