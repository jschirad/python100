# Your program should: print each number from 1 to 100.
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
#

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
