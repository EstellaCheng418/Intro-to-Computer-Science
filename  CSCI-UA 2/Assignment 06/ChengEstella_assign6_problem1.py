# Name: Estella Cheng
# Date: October 13, 2025
# Class Section: 001
# Assignment 06_Problem #1: Part 1a: Number Analyzer

import math

# function: is_even
# input: a positive integer
# processing: determines if the supplied number is even
# output: Boolean
def is_even(n: int)-> bool:
    return n > 0 and n % 2 == 0

# function: is_odd
# input: a positive integer
# processing: determines if the supplied number is odd
# output: Boolean
def is_odd(n: int) -> bool:
    return n > 0 and n % 2 != 0

# function: is_prime
# input: a positive integer
# processing: determines if the supplied number is prime (only has 2 factors, 1 and itself)
# output: Boolean
def is_prime(n: int)-> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # test odd divisors up to sqrt(n)
    limit = int(n ** 0.5)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

# function: sum_factors
# input: an integer (whose factors we want to sum)
# processing:
# 1. If n <= 1, return 0 (1 and 0 have no proper factors).
# 2. Start total at 1 (1 is always a factor of any number > 1).
# 3. Go through possible factors from 2 up to the square root of n.
# 4. If a number divides n evenly, add it and its pair (n // d) to the total.
# 5. Avoid double-counting when n is a perfect square
# output: return sum of factors of n (exclude n itself)
def sum_factors(n: int)-> int:
    if n <= 1:
        return 0
    total = 1 # 1 is always a factor for n 
    limit = int(n ** 0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            total += d
            other = n // d
            if other != d: 
                total += other
    return total

# function: is_perfect
# input: a positive integer
# processing: determines if the supplied number is perfect.(number = sum of factors)
# output: Boolean
def is_perfect(n: int)-> bool:
    return n > 0 and sum_factors(n)== n 

# function: is_abundant
# input: a positive integer
# processing: determines if the supplied number is abundant.(number less than sum of factors)
# output: Boolean
def is_abundant(n: int)-> bool:
    return n > 0 and sum_factors(n) > n


# Get a positive starting number
while True:
    start = int(input("Enter starting number: "))
    if start > 0:
        break 
    print("Invalid, try again")

# Get an ending number greater than starting number
while True:
    end = int(input("Enter ending number: "))
    if end > start:
        break
    print("Invalid, try again")

for n in range(start, end + 1):
    # Check if n is even or off
    if is_even(n):
        even_odd = "even"
    else:
        even_odd = "odd"

    # Decide classification
    category = ""
    if is_prime(n):
        category = "prime"
    elif is_perfect(n):
        category = "perfect"
    elif is_abundant(n):
        category = "abundant"

    # Print the result
    if category != "":
        print(str(n) + " is..." + even_odd + " " + category)
    else:
        print(str(n) + " is..." + even_odd)


        
        
        



