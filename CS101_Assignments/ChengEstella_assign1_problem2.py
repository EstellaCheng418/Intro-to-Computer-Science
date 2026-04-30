# Name: Estella Cheng
# Date: September 19, 2025
# Class Section: 001
# Assignment 01_Problem #2: Using the print function

# Ask the user to enter three sports
sport_1 = input("Please enter sport #1: ")
sport_2 = input("Please enter sport #2: ")
sport_3 = input("Please enter sport #3: ")
print("\n")

# Output 
print("Here are your sports in every possible order:\n\n")

# 1. Sport 1, Sport 2, Sport 3
print("1. " + sport_1 + ", " + sport_2 + ", " + sport_3 + "\n\n")

# 2. ***Sport 1*** ***Sport 3*** ***Sport 2***
print("2. " + "***" + sport_1 + "*** ***" + sport_3 + "*** ***" + sport_2 + "***\n\n")

# 3. Sport 2:Sport 1:Sport 3
print("3. " + sport_2 + ":" + sport_1 + ":" + sport_3 + "\n\n")

# 4. Sport 2 (new line) Sport 3 (new line) Sport 1
print("4. " + sport_2)
print(sport_3)
print(sport_1 + "\n\n")
    
# 5. Sport 3? (new line) Sport 2! (new line) Sport 1?!
print("5. " + sport_3 + "?")
print("   " + sport_2 + "!")
print("   " + sport_1 + "?!\n\n")
      
# 6. --Sport 3 (new line) -----Sport 1 (new line) -------Sport 2
print("6. " + "--" + sport_3)
print("   -----" + sport_1)
print("   -------" + sport_2)




    
