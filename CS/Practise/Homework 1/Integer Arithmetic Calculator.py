# Integer Arithmetic Calculator

# Get user input of 2 integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Operations
addition = num1 + num2 
subtraction = num1 - num2
multiplication = num1 * num2

# Print output
print(str(num1), "+", str(num2), "=", addition)
print(str(num1), "-", str(num2), "=", subtraction)
print(str(num1), "*", str(num2), "=", multiplication)

# Data validation for num2 (cannot be 0)
if num2 != 0:
    division = format(num1 / num2, ".2f") # Format quotient to 2 decimal places 
    print(str(num1), "/", str(num2), "=", division)
    modulus = num1 % num2
    print(str(num1), "mod", str(num2), "=", modulus)
else:
    print(str(num1), "/", str(num2) + ": Division by zero is not allowed.")
    print(str(num1), "mod", str(num2) + ": Division by zero is not allowed.")



