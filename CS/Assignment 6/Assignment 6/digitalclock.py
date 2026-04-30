# Name: Estella Cheng
# Date: October 17, 2025
# Class Section: 001
# Assignment 06_Problem #2

import random
#———————————— Problem 2a ———————————————
# function: horizontal_line
# input: a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output: returns the generated pattern (string)
def horizontal_line(width,char):
    return width*char + "\n"

# function: vertical_line
# input: a shift value and a height value (both integers) and a single character (string)
# processing: generates a single vertical line of the desired height. the line is
# offset from the left side of the screen using the shift value
# output: returns the generated pattern (string)
def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift*" " + char + "\n"
    return pattern

# function: two_vertical_lines
# input: a width value and a height value (both integers) and a single character (string)
# processing: generates two vertical lines. the first line is along the left side of
# the screen. the second line is offset using the "width" value supplied
# output: returns the generated pattern (string)
def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " "*(width-2) + char + "\n"
    return pattern


#———————————— Problem 2b ———————————————
# function: number_0
# input: a width value (integer) and a single character (string)
# processing: generates the number 0 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_0(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 3, character)
    pattern += horizontal_line(width, character)
    return pattern

# function: number_1
# input: a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_1(width, character):
    pattern = vertical_line(width-1, 5, character)
    return pattern

# function: number_2
# input: a width value (integer) and a single character (string)
# processing: generates the number 2 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_2(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

# function: number_3
# input: a width value (integer) and a single character (string)
# processing: generates the number 3 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_3(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

# function: number_4
# input: a width value (integer) and a single character (string)
# processing: generates the number 4 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_4(width, character):
    pattern = ""
    pattern += two_vertical_lines(width, 2, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 2, character)
    return pattern

# function: number_5
# input: a width value (integer) and a single character (string)
# processing: generates the number 5 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_5(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

# function: number_6
# input: a width value (integer) and a single character (string)
# processing: generates the number 6 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_6(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

# function: number_7
# input: a width value (integer) and a single character (string)
# processing: generates the number 7 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_7(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 4, character)
    return pattern

# function: number_8
# input: a width value (integer) and a single character (string)
# processing: generates the number 8 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_8(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

# function: number_9
# input: a width value (integer) and a single character (string)
# processing: generates the number 9 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)
def number_9(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 2, character)
    return pattern


#———————————— Problem 2c ———————————————
# function: print_number
# input: a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output: does not return anything
def print_number(num: int, width: int, character: str):
    if num == 0:
        print(number_0(width, character))
    elif num == 1:
        print(number_1(width, character))
    elif num == 2:
        print(number_2(width, character))
    elif num == 3:
        print(number_3(width, character))
    elif num == 4:
        print(number_4(width, character))
    elif num == 5:
        print(number_5(width, character))
    elif num == 6:
        print(number_6(width, character))
    elif num == 7:
        print(number_7(width, character))
    elif num == 8:
        print(number_8(width, character))
    else:
        print(number_9(width, character))


#———————————— Problem 2d ———————————————
# function: plus
# input: a width value (integer) and a single character (string)
# processing: prints the plus sign to the screen using the supplied width value
# output: returns the plus sign pattern (5 units high) (string)
def plus(width: int, character: str):
    pattern = ""
    mid = width // 2
    for row in range (5):
        if row == 2:
            pattern += horizontal_line(width, character)
        else:
            if width % 2 == 0:
                pattern += vertical_line(mid-1, 1, character*2)
            else:
                pattern += vertical_line(mid, 1, character)
    return pattern

# function: minus
# input: a width value (integer) and a single character (string)
# processing: prints the minus sign to the screen using the supplied width value
# output: returns the minus sign  pattern (5 units high) (string)
def minus(width: int, character: str):
    pattern = ""
    for row in range (5):
        if row == 2:
            pattern += horizontal_line(width, character)
        else:
            pattern += horizontal_line(width, " ")
    return pattern


#———————————— Problem 2e ———————————————
# function: check_answer
# input: two numbers (number1 & number2, both integers);
#       an answer (an integer)
#     and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct. for example,
#             if the operator is "+", number1 = 1, number2 = 2 and answer = 3
#             then the expression is correct
#             (1 + 2 = 3)
# output:     returns True if the expression is correct, False if it is not correct
def check_answer(num1: int, num2: int, answer: int, operator: str) -> bool:
    if operator == "+":
        correct = num1 + num2
    else:
        correct = num1 - num2
    return correct == answer


#———————————— Problem 2f ———————————————
# function: get_problem
# input: two numbers (number1 & number2, both integers);
#        and an operator (+ or -, expressed as a String)
# processing: let the computer randomly select 2 numbers from 0 to 9
#             let the computer randomly select an operator (+ or -)
# output: return
def get_problem():
    num1 = random.randint(0,9)
    num2 = random.randint(0, 9)
    operator = random.choice(["+", "-"])
    return num1, num2, operator

# function: print_problem
# input: num1 (the first integer), num2 (the second integer), operator ("+" or "-"), width, character
# processing:
# 1. Prints a header line: "What is ....."
# 2. Calls print_number() to show the first number.
# 3. Calls plus(width, character) if the operator is "+". Calls minus(width, character) otherwise.
# 4. Prints the operator pattern.
# 5. Calls print_number() again to show the second number.
# output: displays the problem on the screen using pattern characters.
def print_problem(num1:int, num2:int, operator:str, width:int, character:str):
    print('\nWhat is .....\n')
    print_number(num1, width, character)
    if operator == "+":
        op_pattern = plus(width, character)
    else:
        op_pattern = minus(width, character)
    print(op_pattern)
    print_number(num2, width, character)

def main():
    correct_count = 0
    while True:
        num_problems = int(input("How many problems would you like to attempt? "))
        if num_problems <= 0:
            print("Invalid number, try again")
        else:
            break

    while True:
        width = int(input("How wide do you want your digits to be? 5-10: "))
        if width < 5 or width > 10:
            print("Invalid width, try again")
        else:
            break

    while True:
        character = input("What character would you like to use? ")
        if len(character) != 1:
            print("String too long, try again")
        else:
            break

    print("Here we go!")

    for i in range(num_problems):
        num1, num2, operator = get_problem()
        print_problem(num1, num2, operator, width, character)
        answer = int(input("="))
        if check_answer(num1, num2, answer, operator):
            print("Correct!")
            correct_count += 1
        else:
            print("Sorry, that's not correct.")

    print("\nYou got", correct_count, "out of", num_problems, "correct!")



if __name__ == '__main__':
    main()
    


    
    
    
