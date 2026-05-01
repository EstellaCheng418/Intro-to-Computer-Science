# Name: Estella Cheng
# Date: October 6, 2025
# Class Section: 001
# Assignment 05_Problem #1: Step by Step

# Get a positive upper limit 
while True:
    upper_limit = int(input("Pick a number to go up to: "))
    if upper_limit <= 0:
        print("Invalid, try again.")
    else:
        break

# Print the pattern, starting at number 1 to upper limit
for i in range(1, upper_limit + 1): # Outer loop control rows
    for num in range(1, i + 1): # Inner loop prints numbers for each row
        print(num, end = " ") # Move to the next line after finishing one row
    print()
