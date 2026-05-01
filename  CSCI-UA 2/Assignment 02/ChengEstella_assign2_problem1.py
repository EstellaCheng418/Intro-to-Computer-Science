# Name: Estella Cheng
# Date: September 19, 2025
# Class Section: 001
# Assignment 02_Problem #1: Special Numbers

# Ask the user to input 2 numbers 
num1 = int(input("Enter a number between 1 and 999: "))
num2 = int(input("Enter another number between 1 and 999: "))

print("Computing special number...")

# 1. Find product of ones
ones1 = num1 % 10
ones2 = num2 % 10
product_ones = ones1 * ones2
print("1. Product of ones:", ones1, "*", ones2, "=", product_ones)

# 2. Find absolute difference of tens
tens1 = (num1 // 10) % 10
tens2 = (num2 // 10) % 10
abs_diff_tens = abs(tens1 - tens2)     
print("2. Absolute difference of tens: |" + str(tens1)+ "-" + str(tens2) + "| =", abs_diff_tens)
    
# 3. Find sum of hundreds
hundreds1 = num1 // 100
hundreds2 = num2 // 100
sum_hundreds = hundreds1 + hundreds2
print("3. Sum of hundreds:", hundreds1, "+", hundreds2, "=", sum_hundreds)

# 4. Join the numbers to form the special number
special_number = str(product_ones)+ str(abs_diff_tens) + str(sum_hundreds)
print("4. Join the numbers: " + special_number) 
print("Your special number is " + special_number + "!")


