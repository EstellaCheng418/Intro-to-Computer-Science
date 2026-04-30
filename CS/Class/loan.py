salary = int(input("What is your yearly salary? "))

if salary > 100000:
    print("You qualify!")
elif salary <= 50000:
    print("You did not qualify!")
else:
    years = int(input("How long have you been at your job? "))
    if years >= 2:
        print("You qualify!")
    else:
        print("You did not qualify!")
