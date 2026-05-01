# Name: Estella Cheng
# Date: October 13, 2025
# Class Section: 001
# Assignment 06_Problem #0: Challenge 2

# Function: valid_date
# Input: two integers (month and day)
# Processing:
# 1. Check that month is in range 1-12
# 2. If Feb -> days in range 1-28
# 3. If Apr/Jun/Sep/Nov -> days in range 1-30
# 4. Else -> days in range 1-31
# Output: True for valid date, otherwise False 

def valid_date(month, day):
    if month < 1 or month > 12:
        return False

    if month == 2:
        return day >= 1 and day <= 28

    if month == 4 or month == 6 or month == 9 or month == 11:
        return day >= 1 and day <= 30

    return day >= 1 and day <= 31


print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False


    
                                               
