# # First Challenge
# # Even or Odd number
print("Type a number:")
number = input()
if int(number) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# # Secodn Challenge
# # BMI Calculator

height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

height_int = float(height)
weight_int = int(weight)

bmi = weight_int / (height_int ** 2)

bmi_result = int(bmi)
if bmi_result < 18.5:
    print("Your BMI is " + str(bmi_result) + " and you are underweight")
elif bmi_result >= 18.5 and bmi_result <= 24.9:
    print("Your BMI is " + str(bmi_result) + " and you are normal weight")
elif bmi_result >= 25 and bmi_result <= 29.9:
    print("Your BMI is " + str(bmi_result) + " and you are overweight")
else:
    print("Your BMI is " + str(bmi_result) + " and you are obese")

# # Third Challenge
# # Check if a year is a leap year
print("What year would you like to check?")
year = input()
if int(year) % 4 == 0 and int(year) % 100 == 0 or int(year) % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

# Fourth Challenge
# Pizza Delivery
print("Welcome to the Pizza Delivery Service!")
print("Our pizzas are Small Pizza $15, Medium Pizza $20, and Large Pizza $25")
bill = 0
size = input("What size pizza do you want? (small, medium, large) ")
if size == "small":
    bill = bill + 15
    print("Do you want pepperoni? Y or N")
    pepperoni = input()
    if pepperoni == "Y":
        bill = bill + 2
    else:
        print("No pepperoni")
elif size == "medium":
    bill = bill + 20
    print("Do you want pepperoni? Y or N")
    pepperoni = input()
    if pepperoni == "Y":
        bill = bill + 3
    else:
        print("No pepperoni")
elif size == "large":
    bill = bill + 25
    print("Do you want pepperoni? Y or N")
    pepperoni = input()
    if pepperoni == "Y":
        bill = bill + 3
    else:
        print("No pepperoni")
print("Do you want extra cheese? Y or N")
extra_cheese = input()
if extra_cheese == "Y":
    bill = bill + 1
else:
    print("No extra cheese")
print("Your bill is $" + str(bill))


# 5 Challenge

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_string = combined_string.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")
l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")

true = t + r + u + e
love = l + o + v + e

love_result = str(true) + str(love)
love_score = int(love_result)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")