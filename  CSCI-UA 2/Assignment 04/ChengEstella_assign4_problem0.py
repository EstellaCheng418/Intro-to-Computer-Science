# Name: Estella Cheng
# Date: September 30, 2025
# Class Section: 001
# Assignment 04_Problem #0: Seeing Stars

# Part 1
# Get a positive integer for number1
while True:
    num1 = int(input("Number 1: "))
    if num1 <= 0: 
        print("Invalid, try again!")
    else:
        break 
        
# Get an integer larger than number1 for number2 (number1 is positive, number2 should also be positive)
while True:
    num2 = int(input("Number 2: "))
    if num2 <= num1: 
        print("Invalid, try again!")
    else:
        break 

# Part 2 - print number of stars starting at number1 and up to number2
stars = num1
while stars <= num2:
    print(stars, '*' * stars)
    stars += 1

# Part 3 - print number of stars starting at number2 - 1 and up to number1
stars = num2 - 1
while stars >= num1:
    print(stars, '*' * stars)
    stars -= 1
    
    
        
