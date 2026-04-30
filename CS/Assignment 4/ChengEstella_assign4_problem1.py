# Name: Estella Cheng
# Date: September 30, 2025
# Class Section: 001
# Assignment 04_Problem #1: Roll the Dice

import random

# Part 1: Determine number of sides on dice 
while True:
    sides = int(input("How many sides on your dice (4, 6, 8)? "))
    if sides not in (4, 6, 8):
        print("Invalid size, try again.")
    else:
        break
    
print("\nThanks, here we go!\n")

# Part 2: Roll the die until snake eyes 
# Statistics for the game
total_roll = 0
total_die1 = 0
total_die2 = 0

doubles = 0 # Both dice have the same number
high_rolls = 0 # Both dice have their highest number
high_low_rolls = 0 # One die is 1, other die has highest number 
even_rolls = 0 # Both dice are even
odd_rolls = 0 # Both dice are odd
sum_value_rolls = 0 # sum = size of current die 

while True:
    die1 = random.randint (1, sides)
    die2 = random.randint (1, sides)
    total_roll += 1
    total_die1 += die1
    total_die2 += die2

    # Check conditions
    special_message = ""
    
    if die1 == sides and die2 == sides:
        special_message += " High roll!"
        high_rolls += 1
        
    if (die1 == sides and die2 == 1) or (die1 == 1 and die2 == sides): 
        special_message += " High/Low!"
        high_low_rolls += 1

    if die1 % 2 == 0 and die2 % 2 == 0:
        special_message += " Evens!"
        even_rolls += 1
        
    if die1 % 2 == 1 and die2 % 2 == 1:
        special_message += " Odds!"
        odd_rolls += 1
   
    if die1 == die2: 
        special_message += " Doubles!"
        doubles += 1
        
    if die1 + die2 == sides:
        special_message += " Sum value is size value!" 
        sum_value_rolls += 1

    if die1 == 1 and die2 == 1:
        special_message += " Snake Eyes!"
        print("die #1 is *" + str(die1) + "* and die #2 is *" + str(die2) + "*" + special_message)
        break

    print("die #1 is *" + str(die1) + "* and die #2 is *" + str(die2) + "*" + special_message)

# Part 3: Results
print("You finally got snake eyes on roll #", total_roll) 

print("Along the way you rolled DOUBLES " + str(doubles) + " times. (" + format((doubles / total_roll) * 100, ".2f") + "% of all rolls were doubles)")
print("Along the way you rolled TWO HIGH VALUES " + str(high_rolls) + " times. (" + format((high_rolls / total_roll) * 100, ".2f") + "% of all rolls were two high values)")
print("Along the way you rolled TWO EVENS " + str(even_rolls) + " times. (" + format((even_rolls / total_roll) * 100, ".2f") + "% of all rolls were two evens)")
print("Along the way you rolled TWO ODDS " + str(odd_rolls) + " times. (" + format((odd_rolls / total_roll) * 100, ".2f") + "% of all rolls were two odds)")
print("Along the way you rolled HIGH / LOW " + str(high_low_rolls) + " times. (" + format((high_low_rolls / total_roll) * 100, ".2f") + "% of all rolls were high/low)")
print("Along the way you rolled A SUM VALUE " + str(sum_value_rolls) + " times. (" + format((sum_value_rolls / total_roll) * 100, ".2f") + "% of all rolls were a sum value)")


# Average rolls
print("Average roll for die #1: " + format(total_die1/total_roll, ".2f"))
print("Average roll for die #2: " + format(total_die2/total_roll, ".2f"))

      
    





