# # First Challenge
# # Even or Odd number
# print("Type a number:")
# number = input()
# if int(number) % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# # Secodn Challenge
# # BMI Calculator

# height = input("Enter your height in meters: ")
# weight = input("Enter your weight in kilograms: ")

# height_int = float(height)
# weight_int = int(weight)

# bmi = weight_int / (height_int ** 2)

# bmi_result = int(bmi)
# if bmi_result < 18.5:
#     print("Your BMI is " + str(bmi_result) + " and you are underweight")
# elif bmi_result >= 18.5 and bmi_result <= 24.9:
#     print("Your BMI is " + str(bmi_result) + " and you are normal weight")
# elif bmi_result >= 25 and bmi_result <= 29.9:
#     print("Your BMI is " + str(bmi_result) + " and you are overweight")
# else:
#     print("Your BMI is " + str(bmi_result) + " and you are obese")

# # Third Challenge
# # Check if a year is a leap year
# print("What year would you like to check?")
# year = input()
# if int(year) % 4 == 0 and int(year) % 100 == 0 or int(year) % 400 == 0:
#     print("It is a leap year")
# else:
#     print("It is not a leap year")

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

