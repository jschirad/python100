# First Challenge

# Take two digit numbers and add them together
two_digit = input("Enter a two digit number: ")
if len(two_digit) == 2:
    print(int(two_digit[0]) + int(two_digit[1]))
else:
    print("ERROR : enter a two digit number")

# Second Challenge

# BMI Calculator
height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

height_int = float(height)
weight_int = int(weight)

bmi = weight_int / (height_int ** 2)

bmi_result = int(bmi)
print("Your BMI is " + str(bmi_result))

# Third Challenge

age = input("Enter your age: ")
age_int = int(age)
years_left = 90 - age_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print("You have lived for " + str(days_left) + " days")
print("You have lived for " + str(weeks_left) + " weeks")
print("You have lived for " + str(months_left) + " months")

# Tip Calculator
print("Welcome to the Tip Calculator")
bill = input("What is the bill? ")
tip_percent = input("What is the tip percentage? ")
people = input("How manu people are splitting the bill? ")
total = float(bill) + (float(bill) * float(tip_percent) / 100)
total_per_person = total / int(people)
print("The total is ${:.2f}".format(total) + " and each person owes ${:.2f}".format(total_per_person))