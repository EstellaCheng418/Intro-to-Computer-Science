# Name: Estella Cheng
# Date: November 5, 2025
# Class Section: 001
# Assignment 08_Part #1: My Contacts

# Create 2 lists to track contact names and associated email address 
names = []
emails = []

# Ask for number of contacts (must be positive integer)
while True:
    num = int(input("How many contacts would you like to add? "))
    if num <= 0:
        print("Invalid, please try again")
    else:
        break

# Collect contact information
i = 1
while i <= num:

    # Name Validation
    while True:
        person_name = input("Please enter the name of contact " + str(i) + ": ")

        # Check there is exactly one space
        if " " in person_name:
            space_location = person_name.index(" ")

            # Make sure no more spaces after the first one
            if " " not in person_name[space_location + 1:]:

                # Slicing to get first and last name
                first = person_name[:space_location]
                last = person_name[space_location + 1:]

                # Check alphabetic only
                if first.isalpha() and last.isalpha():
                    break

        print("Invalid, please try again")


    # Email Validation
    while True:
        e = input("Please enter the email of contact " + str(i) + ": ")

        valid = False

        # Must contain @ and end with .com 
        if ("@" in e) and (e[-4:] == ".com"):

            # Find where @ and dot(.) is
            at_location = e.find("@")
            dot_location = len(e) - 4      

            # Slice username and domain
            username = e[:at_location]
            domain = e[at_location + 1:dot_location]

            # Username must be non-empty, start with letter, and be alphanumeric
            if len(username) > 0 and username[0].isalpha():
                only_alnum = True
                j = 0
                while j < len(username):
                    if not username[j].isalnum():
                        only_alnum = False
                        break
                    j = j + 1

                # Domain must be non-empty and letters only
                only_letters = (len(domain) > 0 and domain.isalpha())

                if only_alnum and only_letters:
                    valid = True

        if valid:
            break
        else:
            print("Invalid, please try again")

    # Store the contact
    names.append(first + " " + last)
    emails.append(e)
    i = i + 1

# Output address book
print("Thanks! Here is your address book:")
k = 0
while k < len(names):
    print("Name: " + names[k] + ", Email: " + emails[k])
    k = k + 1
