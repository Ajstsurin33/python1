
#: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise.


def is_prime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


number1 = 29
number2 = 15

print(f"{number1} is prime: {is_prime(number1)}")
print(f"{number2} is prime: {is_prime(number2)}")
