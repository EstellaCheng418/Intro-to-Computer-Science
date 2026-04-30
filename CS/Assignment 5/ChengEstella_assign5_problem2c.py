# Name: Estella Cheng
# Date: October 6, 2025
# Class Section: 001
# Assignment 05_Problem #2c: Custom Number Range

# Get a positive start number
while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    
    if start <= 0 or end <= 0:
        print("Start and end must be positive")
    elif end <= start:
        print("End number must be greater than start number")
    else:
        break
    print()
print()
for num in range(start, end + 1):
    if num == 1:
        continue
    else:
        is_prime = True # Assume prime number 

        # Go through all numbers between start and end
        for i in range (2, num):
            if num % i == 0:
                is_prime = False # Not prime number
                break
        if is_prime:
            print(num)



    
