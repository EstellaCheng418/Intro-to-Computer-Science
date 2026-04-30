# Name: Estella Cheng
# Date: September 25, 2025
# Class Section: 001
# Assignment 03_Problem #3：Daily Schedule 

# Ask the user for time 
time = int(input("What time is it? "))

# Ask the user for the day of the week
day = input("What day of the week is it? ")

# Normalize input 
day = day.lower()

# Determine if it is a weekday or weekend
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekends = ["saturday", "sunday"]
    
# Check if the time is valid (must be between 0 and 23)
if time < 0 or time > 23:
    print ("You have entered an invalid time!")

# Determine activity based on time
elif 8 <= time <= 15:
    print("During this time, you have class")
elif 16 <= time <= 18:
    print("During this time, you have free time")
elif 19 <= time <= 21:
    if day in weekdays:
        print("During this time, you cook and eat dinner")
    elif day in weekends:
        print("During this time, you go out for dinner with friends")
    else:
        print("Invalid day entered")
elif (22 <= time <= 23) or (0 <= time <= 7):
    print("During this time, you sleep")
else:
    print("During this time, you sleep")
       
