import random
from random import randint

# pick a random integer
secret_num = randint(1,10)

# get number from user
num = int(input("What is my secret number? "))

# compare user number to secret number
if num == secret_num:
          print("you guessed my number!")
elif num < secret_num:
          print("Your number is too low!")
else:
          print("Your number is too high!")

# show the user the secret number
print("My number was", secret_num)
          


    
