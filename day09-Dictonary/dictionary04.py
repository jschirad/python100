import os
import art
#HINT: You can call clear() to clear the output in the console.
clear = lambda: os.system('clear')
dictionary = {}
def add_new_value(name, bid):
    dictionary[name] = bid
    return dictionary


def main():
    clear()
    print(art.logo)
    switch = True
    while switch != False:
        name = input("What is your name? ")
        bid = input("What is your bid? $")
        add_new_value(name, bid)
        another = input("There is another bid? (y/n) ")
        if another == "n":
            switch = False
        else:
            clear()
def high_score():
    clear()
    max_value = 0
    for key, value in dictionary.items():
        if int(value) > int(max_value):
            max_value = value
            max_key = key
    print("The highest bid is from", max_key, "with a bid of $", max_value)
    print(art.logo)

main()
high_score()





