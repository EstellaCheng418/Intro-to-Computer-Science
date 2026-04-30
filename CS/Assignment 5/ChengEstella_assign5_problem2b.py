# Name: Estella Cheng
# Date: October 6, 2025
# Class Section: 001
# Assignment 05_Problem #2b: Find all Prime Numbers between 1 and 1000

for num in range(1, 1001):
    if num == 1:
        print("1 is technically not a prime number.")
    else:
        is_prime = True # Assume prime number 

        # Test divisors from 2 to num - 1
        for i in range (2, num):
            if num % i == 0:
                is_prime = False # Not prime number
                break
        if is_prime:
            print(num, "is a prime number!")

