# Name: Estella Cheng
# Date: September 19, 2025
# Class Section: 001
# Assignment 02_Problem #0: Lottery Winning Calculator (Warm-up)

# Get user input: total winnings, number of people, and tax rate
total_winnings = float(input("How much money did you win? "))
num_people = int(input("How many people are splitting the winnings? "))
tax_rate = int(input("What is the tax rate on winnings? (i.e. 25 = 25%): "))

# Calculate amount of each share 
share = total_winnings / num_people

# Calculate tax per person
tax_per_person = share * (tax_rate / 100)

# Calculate take home amount per person
take_home = share - tax_per_person

# Output
print()
print()
print("In total you won $" + str(format(total_winnings, ",.2f")))
print("Split", str(num_people), "ways that amounts to $" + format (share, ",.2f") + " per person")
print("Tax per person: $" + format(tax_per_person, ",.2f"))
print("Take home amount per person: $" + format(take_home, ",.2f" ))
      

      
 
