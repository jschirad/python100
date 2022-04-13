import os
import art
#HINT: You can call clear() to clear the output in the console.
clear = lambda: os.system('clear')
# Empty dictionary
dictionary = {}

# Add new value to dictionary
def add_new_value(name, bid):
    dictionary[name] = bid
    return dictionary

# Ask user for name and bid
def main():
    clear()
    print(art.logo)
    switch = True
    while switch != False:
        name = input("What is your name? ")
        bid = input("What is your bid? $")
        # Add new value to dictionary
        add_new_value(name, bid)
        # Ask user if they want to continue
        another = input("There is another bid? (y/n) ")
        if another == "n":
            switch = False
        else:
            clear()

# Calculate highest bid
def high_score():
    clear()
    max_value = 0
    # Loop through dictionary
    for key, value in dictionary.items():
        if int(value) > int(max_value):
            max_value = value
            max_key = key
    print("The highest bid is from", max_key, "with a bid of $", max_value)
    print(art.logo)

# Call main function
main()
# Call high_score function
high_score()





