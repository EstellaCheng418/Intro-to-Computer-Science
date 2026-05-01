# Name: Estella Cheng
# Date: September 20, 2025
# Class Section: 001
# Assignment 02_Problem #2: Your New Yard


print("How much fencing will you need for your new yard?")

# Ask the user for inputs  
x1 = float(input("First x: "))
x2 = float(input("Second x: "))
y1 = float(input("First y: "))
y2 = float(input("Second y: "))

# Compute the length and width of rectangle
length = abs(x1 - x2)
width = abs(y1 - y2)

# Print the length and width as floats 
print("Length:", length)
print("Width:", width)
      
# Calculate the perimeter
perimeter = 2 * length + 2 * width

# Print the perimeter as integer
print("Your yard's perimeter is", int(perimeter))
