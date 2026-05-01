# Name: Estella Cheng
# Date: October 6, 2025
# Class Section: 001
# Assignment 05_Problem #2a: Prime Number Finder 

# Get a positive number and validate it 
num = int(input("Enter a positive number to test: "))
while num <= 0:
    num = int(input("Invalid input. Please enter a positive number: "))
print()

# Special case: 1 is not prime number
if num == 1:
    print("1 is not a prime number.")
else:
    is_prime = True # Assume 1 = prime, 0 = not prime

    # Determine if the number is a prime number
    for i in range(2, num): # Test divisors from 2 up to num - 1
        if num % i == 0:
            print(i, "is a divisor of", num, "...stopping")
            is_prime = False 
            break
        else:
            print(i, "is NOT a divisor of", num, "...continuing")
print()
    
# Output 
if not is_prime:
    print(num, "is not prime number.")
else:
    print(num, "is a prime number!")
