# Name: Estella Cheng
# Date: November 15, 2025
# Class Section: 001
# Assignment 10_Part #2

import random
rows = 4
cols = 5
# -------------------------------
# Problem 2a — Create two 4×5 boards，filled with "."
# -------------------------------

# Create user board
user_board = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(".")
    user_board.append(row)

# Create computer board
computer_board = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(".")
    computer_board.append(row)

# -------------------------------
# Functions to print boards
# -------------------------------
# function: print_user_board
# input: the user's board (4×5) containing ".", "S", "X", or "O"
# processing: loop through rows and columns, print each cell on the same line,
#             then print "-----" after each row
# output: a visual representation of the board

# Show everything on the user's board
def print_user_board(board):
    for i in range(rows):
        for j in range(cols):
            print(board[i][j], end="")
        print()
        print("-----")

# print_user_board(user_board)


# -------------------------------
# Problem 2b — User places 5 ships on user_board
# -------------------------------
ships_placed = 0

while ships_placed < 5:
    # get a valid row (0–3)
    while True:
        try:
            r = int(input("Please enter a row: "))
            if 0 <= r < rows:
                break
            else:
                print("Invalid, try again!")
        except:
            print("Invalid input, please enter a valid number")

    # get a valid column (0–4)
    while True:
        try:
            c = int(input("Please enter a column: "))
            if 0 <= c < cols:
                break
            else:
                print("Invalid, try again!")
        except:
            print("Invalid input, please enter a valid number")

    # check if a ship is already there
    if user_board[r][c] == "S":
        print("Ship already exists in that location.")
    else:
        user_board[r][c] = "S"
        ships_placed += 1
        print("Ship " + str(ships_placed) + " placed.")

# ----- print final user board -----
print("Here is your board:")
print_user_board(user_board)


# -------------------------------
# Problem 2c — Computer places 5 ships on computer_board randomly
# -------------------------------

# function: print_computer_board
# input: the computer’s board (4x5)
# processing: loop through rows and columns,
# .           replacing "S" with "." and print all other characters
# output: a hidden-ship version of the computer board

# Hide computer ships: show "." instead of "S"
def print_computer_board(board):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "S":
                print(".", end="")
            else:
                print(board[i][j], end="")
        print()
        print("-----")

comp_ships = 0
while comp_ships < 5:
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)

    if computer_board[r][c] == ".":
        computer_board[r][c] = "S"
        comp_ships += 1

# print("Here is the computer's board:")
# print_computer_board(computer_board)


# -------------------------------
# Problem 2d — Play the game
# -------------------------------
user_hits = 0
comp_hits = 0
user_turns = 0

print("Let's play!")
while user_hits < 5 and comp_hits < 5: 
    # ----------------- User's turn -----------------
    while True:
        print("User's turn...")
        # valid row
        while True:
            try:
                r = int(input("Please enter a row: "))
                if 0 <= r < rows:
                    break
                else:
                    print("Invalid, try again!")
            except:
                print("Invalid input, please enter a valid number")
        # column
        while True:
            try:
                c = int(input("Please enter a column: "))
                if 0 <= c < cols:
                    break
                else:
                    print("Invalid, try again!")
            except:
                print("Invalid input, please enter a valid number")
        if computer_board[r][c] == "X" or computer_board[r][c] == "O":
            print("You've already gone here, please try again.")
        else:
            break
    
    # resolve shot
    if computer_board[r][c] == "S":
        print("Hit!")
        computer_board[r][c] = "X"
        user_hits += 1
    else:
        print("Miss!")
        computer_board[r][c] = "O"

    user_turns += 1

    # print computer board with ships hidden
    print("Computer's board:")
    print_computer_board(computer_board)

    # if user has sunk all ships, game ends before computer turn
    if user_hits == 5:
        break

    # ----------------- Computer's turn -----------------
    print("Computer's turn...")

    # pick a random, not-yet-used target
    while True:
        cr = random.randint(0, rows - 1)
        cc = random.randint(0, cols - 1)
        if user_board[cr][cc] != "X" and user_board[cr][cc] != "O":
            break

    if user_board[cr][cc] == "S":
        print("Hit!")
        user_board[cr][cc] = "X"
        comp_hits += 1
    else:
        print("Miss!")
        user_board[cr][cc] = "O"

    # print user's board
    print("User's board:")
    print_user_board(user_board)

# -------------------------
# GAME OVER
# -------------------------

# User_hits>=5 or comp_hits >=5
if user_hits == 5:
    print("User won in " + str(user_turns) + " turns!")
else:
    print("Computer won in " + str(user_turns) + " turns!")
