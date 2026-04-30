# Q7

# Given rolls as a string
rolls = "1,5,2,3,5,4,4,3,1,1,1,2,3,1,5,6,2"

# Counters
total_rolls = 0
total_value = 0

# Go through each number separated by commas
current_number = ""
for char in rolls:
    if char != ",":     # build up digits 
        current_number += char
    else:               # reached a comma -> process the number 
        total_rolls += 1
        total_value += int(current_number)
        current_number = ""

# process the last number (since there's no comma after it)
total_rolls += 1
total_value += int(current_number)

# Average
average_roll = total_value / total_rolls

# Output
print("Total number of rolls:", total_rolls)
print("Total value of all rolls:", total_value)
print("Average roll:", average_roll)
