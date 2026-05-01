# Name: Estella Cheng
# Date: October 17, 2025
# Class Section: 001
# Assignment 06_Problem #1b: Number Analyzer 
       
import math
#---------------- Part A: Helper Functions ----------------

# function: is_even
# input: a positive integer
# processing: determines if the supplied number is even
# output: Boolean
def is_even(n: int) -> bool:
    return n > 0 and n % 2 == 0

# function: is_odd
# input: a positive integer
# processing: determines if the supplied number is odd
# output: Boolean
def is_odd(n: int) -> bool:
    return n > 0 and n % 2 != 0

# function: is_prime
# input: a positive integer
# processing: determines if the supplied number is prime (only has 2 factors, 1 and itself)
# output: Boolean
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # test odd divisors up to sqrt(n)
    limit = int(n ** 0.5)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

# function: sum_factors
# input: an integer (whose factors we want to sum)
# processing:
# 1. If n <= 1, return 0 (1 and 0 have no proper factors).
# 2. Start total at 1 (1 is always a factor of any number > 1).
# 3. Go through possible factors from 2 up to the square root of n.
# 4. If a number divides n evenly, add it and its pair (n // d) to the total.
# 5. Avoid double-counting when n is a perfect square
# output: return sum of factors of n (exclude n itself)
def sum_factors(n: int) -> int:
    if n <= 1:
        return 0
    total = 1  
    limit = int(n ** 0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            total += d
            other = n // d
            if other != d:
                total += other
    return total

# function: is_perfect
# input: a positive integer
# processing: determines if the supplied number is perfect.(number = sum of factors)
# output: Boolean
def is_perfect(n: int) -> bool:
    return n > 0 and sum_factors(n) == n

# function: is_abundant
# input: a positive integer
# processing: determines if the supplied number is abundant.(number less than sum of factors)
# output: Boolean
def is_abundant(n: int) -> bool:
    return n > 0 and sum_factors(n) > n

#---------------- Part B: Number Analyzer ----------------
# function: get_positive_int
# input: a positive integer
# processing:
# 1. Continuously asks the user for input until a positive integer is entered.
# 2. If the user enters a non-positive integer, it shows "Invalid, try again" and repeats.
# output: returns the positive integer
def get_positive_int(prompt):
    while True:
        value = int(input(prompt))
        if value > 0:
            return value
        print("Invalid, try again")

# function: get_range
# input: a starting number, an ending number
# processing:
# 1. Calls get_positive_int() to get a positive starting number.
# 2. Continuously prompts the user for an ending number until it is greater than the starting number.
# 3. Displays "Invalid, try again" if the ending number is not greater than the starting number.
# output: returns valid starting number and valid ending number
def get_range():
     start = get_positive_int("Enter starting number (positive only): ")
     while True:
         end = int(input("Enter ending number: "))
         if end > start:
             return start, end
         print("Invalid, try again")

# function: print_heading
# input: title (the type of numbers), starting number, ending number
# processing: prints a blank line, the heading text showing the title and range, and a line of # symbols underneath
# output: displays the formatted heading on the screen
def print_heading(title, start, end):
    print("\nAll " + title + " numbers between " + str(start) + " and " + str(end))
    print("##############")

# function: menu_choice
# input: user enters a menu option (str)
# processing:
# 1. Displays a main menu with four options.
# 2. Prompts the user to enter a choice.
# 3. Checks if the input is one of "1", "2", "3", or "4".
# 4. If the input is invalid, displays "I don't understand that ..." and repeats until a valid choice is entered.
# output: returns the user's menu choice
def menu_choice():
    while True:
        print("\nMain Menu\n")
        print("1 - Find all prime numbers within a given range")
        print("2 - Find all perfect numbers within a given range")
        print("3 - Find all abundant numbers within a given range")
        print("4 - Quit\n")
        choice = input("Your choice: ")
        if choice in ("1", "2", "3", "4"):
            return choice
        print("I don't understand that ...")


def main():
    while True:
        choice = menu_choice()

        if choice == "4":
            print("\nGoodbye!")
            break

        start, end = get_range()

        if choice == "1":
            print("\nAll prime numbers between", start, "and", end)
            print("##############")
            for i in range(start, end + 1):
                if is_prime(i):
                    print(i)
            print("##############")

        elif choice == "2":
            print("\nAll perfect numbers between", start, "and", end)
            print("##############")
            for i in range(start, end + 1):
                if is_perfect(i):
                    print(i)
            print("##############")

        else:
            print("\nAll abundant numbers between", start, "and", end)
            print("##############")
            for i in range(start, end + 1):
                if is_abundant(i):
                    print(i)
            print("##############")


if __name__ == "__main__":
    main()
        
        
        



