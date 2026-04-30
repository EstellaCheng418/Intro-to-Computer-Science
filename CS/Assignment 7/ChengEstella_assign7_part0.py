# Name: Estella Cheng
# Date: October 29, 2025
# Class Section: 001
# Assignment 07_Part #0: New User

# whole thing in a while loop to validate the input
while True:
    # 1. get a username
    name = input("Enter a username: ")

    # 2. get the length of the username 
    length = len(name)

    # 3. create accumulator variables 
    upper_count = 0
    lower_count = 0
    digit_count = 0

    # 4. loop through the username and count each thing we need to validate (using str test methods)
    for char in name:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1

    # 5. validate entire string is alphanumeric
    is_alnum = name.isalnum()

    # 6. validate first and last chars are not digits (string indexing and str test method)
    first_last_not_digits = (not name[0].isdigit() and not name[-1].isdigit())

    # 7. print all results
    print("* Length of username:", length)
    print("* All characters are alpha-numeric:", is_alnum)
    print("* First & last characters are not digits:", first_last_not_digits)
    print("* # of uppercase characters in the username:", upper_count)
    print("* # of lowercase characters in the username:", lower_count)
    print("* # of digits in the username:", digit_count)

    # 8. conditional to test if criteria is met
    if (length >= 8 and length <= 15 and is_alnum == True and first_last_not_digits == True
        and upper_count >= 1 and lower_count >= 1 and digit_count >= 1):
        print("Username is valid!")
        break
    else:
        print("Username is invalid, please try again\n")

