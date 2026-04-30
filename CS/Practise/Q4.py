# user input 4 numbers

x1 = float(input("x1: "))
while x1 < 0:
    x1 = input("Invalid coordinates")
    x1 = float(input("x1: "))
    
y1 = float(input("y1: "))
while y1 < 0:
    y1 = input("Invalid coordinates")
    y1 = float(input("y1: "))
    
x2 = float(input("x2: "))
while x2 < 0:
    x2 = input("Invalid coordinates")
    x2 = float(input("x1: "))
    
y2 = float(input("y2: "))
while y2 < 0:
    y2 = input("Invalid coordinates")
    y2 = float(input("y1: "))

# Output
print("Your result:\t")
print("(x1, y1) = (" + str(x1) + ",", str(y1) + ")\t")
print("(x2, y2) = (" + str(x2) + ",", str(y2) + ")\t")

# Calculate distance
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("d =", str(d))

