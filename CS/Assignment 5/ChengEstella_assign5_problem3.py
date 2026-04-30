# Name: Estella Cheng
# Date: October 6, 2025
# Class Section: 001
# Assignment 05_Problem #3: Multiplication Table

# Get a positive integer for lower number
while True:
    low = int(input("Lowest number: "))
    if low >= 0:
        break
    print("Lowest number must be 0 or greater")

# Get an integer larger than lower number for higher number
while True:
    high = int(input("Highest number: "))
    if high <= low:
        print("Highest number must be larger than lowest number!")
    else:
        break

# Generate multiplication table

# Find the largest number
max_value = high * high

# width of each column = lengths of character + 1 space 
width = len(str(max_value)) + 1 

# 1 - Print + sign and column headings
print("+" + " " * (width - 1), end = " ")
for i in range(low, high + 1):
    print(format(i, "<" + str(width)), end = "")
print() # Move to next line

# 2 - Print dashes that adjust automatically
total_width = (high - low + 2)* width
print("-" * total_width)

# 3 - Print rows 
for i in range(low, high + 1):
    print(str(i) + " " * (width - len(str(i))-1), end = "| ")
    for j in range(low, high + 1):
        product = i * j
        print(format(product, "<" + str(width)), end = "")
    print()  # move to next row


