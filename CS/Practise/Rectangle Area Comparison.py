#Rectangle Area Comparison

# Get user input of width and length of 2 rectangles
width1 = int(input("What is the width for rectangle 1? "))
length1 = int(input("What is the length for rectangle 1? "))
width2 = int(input("What is the width for rectangle 2? "))
length2 = int(input("What is the length for rectangle 2? "))

# Calculate area of each rectangle
area1 = width1 * length1
area2 = width2 * length2

# Compare size of 2 rectangles
if area1 > area2:
    print("Rectangle 1 is larger than rectangle 2.")

elif area1 < area2:
    print("Rectangle 2 is larger than rectangle 1.")
else:
    print("Two rectangles are the same size!")

# Check if there is a square
if width1 == length1:
    print("Rectangle 1 is a square!")
if width2 == length2:
    print("Rectangle 2 is a square!")
