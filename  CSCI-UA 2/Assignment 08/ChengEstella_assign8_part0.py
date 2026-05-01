# Name: Estella Cheng
# Date: November 5, 2025
# Class Section: 001
# Assignment 08_Part #0: Daily Sales

# create list
sales_7day = []

# loop over the list
for i in range(1,8):
    while True: 
        # inside loop —— ask user for sales for each day
        sales = float(input("Sales for day " + str(i) + ": "))
                  
        # validate sales are non-negative
        if sales >= 0:
            # add to our list
            sales_7day.append(sales)
            break
        else:
            print("Sorry, that is not a valid amount. Please try again.")

# After gathering sales for the week, calculate:
# total, average, highest, lowest sales
total = sum(sales_7day)
avg = total/len(sales_7day)
highest = max(sales_7day)
lowest = min(sales_7day)

# print out stats
print("\nTotal sales:", total)
print("Average sales per day:", format(avg,'.2f'))
print("Highest sales day:", highest)
print("Lowest sales day:", lowest)

