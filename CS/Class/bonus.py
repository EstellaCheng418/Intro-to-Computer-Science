# Calculating a bonus
sales = int(input("What were your monthly sales? "))

#Quota
bonus = 0
quota = 10000

# Check if quota met
if sales >= quota:
    bonus = 500
    print("Good job! You met your quota.")

# Commission
if sales > 50000:
    commission = sales * .05
else:
    commission = sales * 0.01

total_pay = bonus + commission

# Output results
print("Your commission is: $", commission)
print("Your bonus is: $", bonus)
print("Your total take-home amount is: $", total_pay)
