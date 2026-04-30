# Name: Estella Cheng
# Date: September 23, 2025
# Class Section: 001
# Assignment 03_Problem #2：Rock, Paper, Scissors

import random

print("Rock, Paper, Scissors")

# Ask for user input
player = input("Rock, paper, or scissors? ").lower()

# Check if the input is valid
if player != "rock" and player != "paper" and player != "scissors":
  print("That is not a valid option.")
  print("Please try again!")
else:
    
  # Computer picks a number (0, 1, or 2)
  computer_number = random.randint(0, 2)

  # Translate number into choice
  if computer_number == 0:
      computer = "rock"
  elif computer_number == 1:
      computer = "paper"
  else:
      computer = "scissors"
    
  print("The computer played", computer + ".")

  # Decide winner
  if player == computer:
      print("You tie!")
  elif (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
      print("You win!")
  else:
      print("You lose!")
