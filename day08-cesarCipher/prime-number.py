"""Prime number checker"""
def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
print(is_prime(int(input("Enter a number: "))))