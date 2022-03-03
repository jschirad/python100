# Dia 3 / 100 de Python

https://docs.python.org/3/tutorial/controlflow.html

# if / else conditional
print("Welocome to the rollercoaster!")
print("How old are you?")
age = input()
if int(age) >= 18:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you can't ride the rollercoaster!")

# Rollercoster 2.0
print("Welocome to the rollercoaster!")
bill = 0
print("How old are you?")
age = input()
if int(age) < 12:
    print("Child ticket is $5")
    bill = 5
elif int(age) >= 12 and int(age) < 18:
    print("Youth ticket is $10")
    bill = 10
elif int(age) >= 18 and int(age) < 65:
    print("Adult ticket is free")
else:
    print("Adult ticket is $15")
    bill = 15


print("Do you want a photo with your ticket?")
photo = input()
if photo == "yes":
    bill = bill + 5
    print("Your bill is $" + str(bill))
else:
    print("Your bill is $" + str(bill)) 
