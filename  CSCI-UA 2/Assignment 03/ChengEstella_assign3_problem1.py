# Name: Estella Cheng
# Date: September 22, 2025
# Class Section: 001
# Assignment 03_Problem #1：What Kind of Triangle?

print("Triangle Tester\n\n")

# Ask the user to enter 3 side lengths
# Let a, b, c be the 3 sides of the triangle
a = float(input("What is the length of side 1? "))
b = float(input("What is the length of side 2? "))
c = float(input("What is the length of side 3? "))

# Format the sides to 2 decimal places 
a = float(format(a, ".2f"))
b = float(format(b, ".2f"))
c = float(format(c, ".2f"))

# Check if the triangle is valid
if (a + b > c) and (b + c > a) and (a + c > b):
    print("This is a valid triangle!")

    # Calculate the perimeter of triangle (to nearest tenth)
    perimeter = a + b + c
    print("The perimeter of the triangle is", format(perimeter, ".1f"))

    # Determine the type of triangle
    if a == b == c:
       print("This is an equilateral triangle")
    elif a != b != c: 
       print("This is a scalene triangle")
    else:
       print("This is an isosceles triangle")

    # Check if it's a right triangle
    # z will represent the new hypotenuse 
    if a >= b and a >= c:
        x, y, z = b, c, a
    elif b >= a and b >= c:
        x, y, z = a, c, b
    else:
        x, y, z = a, b, c
        
    # Compare squares, rounded to 0 decimals
    if round(x**2) + round(y**2) == round(z**2):
        print("This is also a right triangle")

else:
    print("This is not a valid triangle.") 










        
              
              
              

      
