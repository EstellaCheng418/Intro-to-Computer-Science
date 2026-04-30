# Name: Estella Cheng
# Date: October 27, 2025
# Class Section: 001
# Assignment 07_Problem #1: Telephone Numbers (part 1)

# Ask the user for a phone number
while True: 
    number = input("What is your phone number? ")

    # Validate length
    if len(number) < 10:
        print("Phone number is too short, please try again!")
    elif len(number) > 10:
        print("Phone number is too long, please try again!")
    else:
        print("Your phone number is +1 (" + number[:3] + ") " + number[3:6] + "-" + number[6:] + ".")
        break
