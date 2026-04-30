# Name: Estella Cheng
# Date: October 13, 2025
# Class Section: 001
# Assignment 06_Problem #0: Challenge 1

# Function: maximum
# Input: two numbers
# Processing: compares number and determines which is larger
# Output: larger number
def maximum(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

# Function: minimum
# Input: two numbers
# Processing: compares number and determines which is smaller
# Output: smaller number
def minimum(num1, num2):
    if num1 <= num2:
        return num1
    else:
        return num2

'''
a = 5
b = 10
c = 15
d = 20
ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20
ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5
ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)
'''



