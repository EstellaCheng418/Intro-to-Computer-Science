# Name: Estella Cheng
# Date: December 4, 2025
# Class Section: 001
# Assignment 11_Part #0: Rectangles

class Rectangle:
    def __init__(self, width, length, x, y):
        self.width = width
        self.length = length
        self.x = x
        self.y = y

    def get_area (self):
        return self.width * self.length

    def get_perimeter (self):
        return 2 * (self.width + self.length)

# Create two rectangles
r1 = Rectangle(10,15,5,3)
r2 = Rectangle(3,5,15,7)

# Print out info of both rectangles
# Print coordinates using x position and y position
# Use class methods to calculate and print area and perimeter

# Output Rectangle #1
print("Rectangle #1")
print("* Coordinates: (" + str(r1.x) + ", " + str(r1.y) + ")")
print("* Area:", r1.get_area())
print("* Perimeter:", r1.get_perimeter())

print()

# Output Rectangle #2
print("Rectangle #2")
print("* Coordinates: (" + str(r2.x) + ", " + str(r2.y) + ")")
print("* Area:", r2.get_area())
print("* Perimeter:", r2.get_perimeter())




