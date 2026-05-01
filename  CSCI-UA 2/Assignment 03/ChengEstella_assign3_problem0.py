# Name: Estella Cheng
# Date: September 22, 2025
# Class Section: 001
# Assignment 03_Problem #0：Two Rectangles (Warm-Up)

# Get rectangle dimensions from user
width1 = int(input("Enter the width for Rectangle #1: "))
length1 = int(input("Enter the length for Rectangle #1: "))
width2 = int(input("Enter the width for Rectangle #2: "))
length2 = int(input ("Enter the length for Rectangle #2: "))

# Calculate areas
area1 = width1 * length1
area2 = width2 * length2

# Print areas
print("Rectangle #1 has an area of", area1)
print("Rectangle #2 has an area of", area2)

# Compare rectangle sizes 
if area1 > area2:
   print("Rectangle #1 is larger than Rectangle #2!")
elif area1 == area2:
   print("Rectangle #1 and Rectangle #2 are the same size!")
else:
    print("Rectangle #2 is larger than Rectangle #1!")

# Determine if either rectangle is a square 
if width1 == length1:
   print("Rectangle #1 is a square!")
if width2 == length2:
   print("Rectangle #2 is a square!")


   
