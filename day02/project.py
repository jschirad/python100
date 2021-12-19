# Tip Calculator
print("Welcome to the Tip Calculator")
bill = input("What is the bill? ")
tip_percent = input("What is the tip percentage? ")
people = input("How manu people are splitting the bill? ")
total = float(bill) + (float(bill) * float(tip_percent) / 100)
total_per_person = total / int(people)
print("The total is ${:.2f}".format(total) + " and each person owes ${:.2f}".format(total_per_person))