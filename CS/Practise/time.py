# Time validator and schedule
# Get user input
time = int(input("Enter a military time of a day: "))
day = str(input("What is the day of the week? "))
day = day.lower()
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekends = ["saturday", "sunday"]
          
# Check if time is valid
if time < 0 or time > 23:
    print("You have entered an invalid time.")
elif 8 <= time <= 15:
    print("You are in class")
elif 16 <= time <= 18:
    print("You have free time")
elif 19 <= time <= 21:
    if day in weekdays:
        print("Cook dinner")
    elif day in weekends:
        print("Go out for dinner")
elif (22 <= time <= 23) or (0 <= time <= 7):
    print("You should be sleeping")
