# Triangle Validator

# Get user input of side lengths a, b, c of a triangle
a = float(input("What is side length 1? "))
b = float(input("What is side length 2? "))
c = float(input("What is side length 3? "))

# Check if it is a valid triangle
if a + b > c or a + c > b or b + c > a:
    # Calculate the perimeter
    perimeter = a + b + c
    print("The perimeter of the triangle is", format(perimeter, ".1f"))
           
    # Determine type of triangle
    if a == b == c:
        print("This is an equilateral triangle.")
    elif a != b != c:
        print("This is a scalene triangle.")
    else:
        print("This is an isosceles triangle.")
else:
    print("This is not a valid triangle.")
    
