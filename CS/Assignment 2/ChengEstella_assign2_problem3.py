# Name: Estella Cheng
# Date: September 20, 2025
# Class Section: 001
# Assignment 02_Problem #3: Variable Rate Loan

import random

print("This program will project how much a variable interest-rate loan will grow over a 3-month period.\n")

# Get initial loan amount
loan = float(input("To begin, enter how much money you would like to initially borrow (i.e. 20000): "))

# Get lower bound for the interest rate 
lower_bound = int(input("Next, enter a lower bound for the monthly interest rate. For exampele, enter 5 for 5%: "))

# Ask for a upper bound for the interest rate
upper_bound = int(input("Finally, enter an upper bound for the monthly interest rate. For example, enter 10 for 10%: "))
           

print("\n\n------- Calculating -------\n")
print("Month\tStarting Balance\tInterest Rate\tEnding Balance")
    
starting_balance1 = loan
interest_rate1= random.randint(lower_bound, upper_bound)
interst_amount1 = starting_balance1 * (interest_rate1/ 100)
ending_balance1 = starting_balance1 + interst_amount1
print("1\t${:,.2f}\t{}%\t\t${:,.2f}".format(starting_balance1, interest_rate1, ending_balance1))

starting_balance2 = ending_balance1
interest_rate2= random.randint(lower_bound, upper_bound)
interst_amount2 = starting_balance2 * (interest_rate2/ 100)
ending_balance2 = starting_balance2 + interst_amount2
print("2\t${:,.2f}\t{}%\t\t${:,.2f}".format(starting_balance2, interest_rate2, ending_balance2))
     
starting_balance3 = ending_balance2
interest_rate3= random.randint(lower_bound, upper_bound)
interst_amount3 = starting_balance3 * (interest_rate3/ 100)
ending_balance3 = starting_balance3 + interst_amount3
print("3\t${:,.2f}\t{}%\t\t${:,.2f}".format(starting_balance3, interest_rate3, ending_balance3))
      
     
   
    
    


