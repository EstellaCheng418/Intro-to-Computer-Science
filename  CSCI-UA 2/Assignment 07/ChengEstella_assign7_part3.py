# Name: Estella Cheng
# Date: October 30, 2025
# Class Section: 001
# Assignment 07_Part 3: Identity Check

while True:
    ssn = input("What is your SSN? ")
    violations = ""

    # Check if there are any non-digit characters
    has_alpha = False
    for char in ssn:
        if not (char.isdigit() or char == '-'):
            has_alpha = True
            break
    if has_alpha:
        violations += "Only digits allowed. "

    # Check the number and position of hyphens
    hyphen_count = 0
    for char in ssn:
        if char == '-':
            hyphen_count += 1

    if hyphen_count != 2:
        violations += "Missing hyphen(s). "
        hyphen_correct = False
    else:
        # Ensure ssn is long enough to check char at index 3 and 6 without error
        hyphen_correct = (len(ssn) >= 7 and ssn[3] == '-' and ssn[6] == '-')

        if not hyphen_correct:
            violations += "Missing hyphen(s). "

    # Only check number rules if the length and format are valid
    if len(ssn) == 11 and ssn[3] == '-' and ssn[6] == '-' and not has_alpha:
        # Extract each section
        area = int(ssn[0:3])
        group = int(ssn[4:6])

        # Check area number
        if area == 0 or area == 666 or (900 <= area <= 999):
            violations += "Area number violated. "

        # Check group number
        if 1 <= area <= 499:
            if group % 2 != 0:
                violations += "Group number violated. "
        elif 500 <= area <= 899:
            if group % 2 == 0:
                violations += "Group number violated. "

    # Output
    if violations == "":
        print("Valid SSN.")
        break
    else:
        print("Invalid SSN, try again! " + violations)
        
        

    
    
    
    
    
