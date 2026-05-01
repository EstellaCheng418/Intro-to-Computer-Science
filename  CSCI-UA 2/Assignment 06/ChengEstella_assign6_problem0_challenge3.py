# Name: Estella Cheng
# Date: October 13, 2025
# Class Section: 001
# Assignment 06_Problem #0: Challenge 3

# Function: simple_sort_version
# Input: three integers(a,b,c)
# Processing:
# 1. Get the smallest and largest number using min and max
# 2. Calculate the middle value by subtracting smallest and largest number from the total 
# Output: arrange a,b,c in ascending order

def simple_sort_version(a,b,c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    middle = (a + b + c) - smallest - largest
    return smallest, middle, largest

'''
a,b,c = simple_sort_version(10,20,30)
print(a,b,c) # 10 20 30
a,b,c = simple_sort_version(10,30,20)
print(a,b,c) # 10 20 30
a,b,c = simple_sort_version(30,20,10)
print(a,b,c) # 10 20 30
a,b,c = simple_sort_version(30,10,20)
print(a,b,c) # 10 20 30
'''
