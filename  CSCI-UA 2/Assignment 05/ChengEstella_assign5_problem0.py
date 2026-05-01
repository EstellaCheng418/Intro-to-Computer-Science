# Name: Estella Cheng
# Date: October 6, 2025
# Class Section: 001
# Assignment 05_Problem #0: Pizza Party

# Get info about pizza party from user 
budget = float(input("Enter budget for your party: "))
cost_per_slice = float(input("Cost per slice of pizza: "))
cost_per_pie = float(input("Cost per whole pizza pie (8 slices): "))
people = int(input("How many people will be attending your party? "))

# Set up for loop to get slices for each person
total = 0
for i in range(people):
    # Ask for number of slices and validate that it's positive
    slices = 0
    while slices < 1:
        slices = float(input("Enter number of slices for person #" + str(i+1) + ": "))
        if slices < 1:
            print("Not a valid entry, try again!")
    # Add to total number of slices
    total += slices

# Calculate number of pies and slices we need to purchase
pies = total//8
slices_leftover= total % 8
      
# Calculate cost
cost = pies * cost_per_pie + slices_leftover * cost_per_slice 

# Determine if it fits our budget
print("You want to purchase", pies, "pies and", slices_leftover, "slices.")
if cost > budget:
    print("Your order cannot be completed.")
elif cost == budget:
    print("You will have no money left after your order.")
else:
    print("You will still have", budget - cost, "remaining after your order.")
    

    
