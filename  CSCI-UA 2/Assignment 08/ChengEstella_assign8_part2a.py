# Name: Estella Cheng
# Date: November 5, 2025
# Class Section: 001
# Assignment 08_Part #2a: Fast Food Restaurant

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]

while True:
    choice = input("(s)earch for product or (q)uit: ")

    if choice == "q":
        print("See you soon!")
        break
    elif choice == "s":
        product = input("Enter a product name: ")

        if product in product_names:
            index = product_names.index(product)
            cost = product_costs[index]
            print("We sell " + product + " at " + str(cost) + " per unit")
        else:
            print("Sorry, we don't sell " + product)
        print()
    else:
        print("Invalid option, try again")
        print()
        
            
        
        
    
    
