# Name: Estella Cheng
# Date: October 1, 2025
# Class Section: 001
# Assignment 04_Problem #3: Math Quiz

import random

score = 0
operations = ["+", "-", "*"]

# Ask 5 questions
for question_num in range(1,6):
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    operation = random.choice(operations)

    # Ways of getting correct answer
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    # Present the question
    print("Question " + str(question_num) + ".", num1, operation, num2)
    user_answer = float(input("What is the answer? ")) 

    # Check correctness
    if user_answer == correct_answer:
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect!\n")

# Final results
print("You received", str(score), "out of a possible 5 points.")

# Convert score to grade
if score == 5:
    grade = "A"
elif score == 4:
    grade = "B"
elif score == 3:
    grade = "C"
elif score == 2:
    grade = "D"
else:
    grade = "F"

print("You scored a " + grade + ".")
        
        
    
                      
    
