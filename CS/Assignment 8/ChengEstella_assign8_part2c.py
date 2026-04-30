# Name: Estella Cheng
# Date: November 5, 2025
# Class Section: 001
# Assignment 08_Part #2c

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_stock = [10, 5, 20] # 10 soft drinks, 5 onion rings, 20 small fries 

while True:
    choice = input("(s)earch, (l)ist, (a)dd or (q)uit: ")

    if choice == "q":
        print("See you soon!")
        break
    
    elif choice == "s":
        product = input("Enter a product name: ")

        if product in product_names:
            index = product_names.index(product)
            cost = product_costs[index]
            stock = product_stock[index]
            
            print("We sell " + product + " at " + str(cost) + " per unit")
            print("We currently have " + str(stock) + " in stock")
        else:
            print("Sorry, we don't sell " + product)
        print()

    elif choice == "l":
        # print headings
        print(format("Product", "<15"), format("Price", ">6"), format("Quantity", ">10"))

        i = 0
        while i < len(product_names):
            print(
            format(product_names[i], "<15"),
            format(product_costs[i], ">6"),
            format(product_stock[i], ">10"))
        
            i += 1
        print()

    elif choice == "a":
        # Get a new product name
        while True:
            new_name = input("Enter a new product name: ")
            if new_name in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                break
            
        # Get a valid positive cost
        while True:
            cost_new_product = float(input("Enter a product cost: "))

            if cost_new_product > 0:
                break
                
            print("Invalid cost. Try again.")
    
        # Get a valid positive quantity
        while True:
            quantity = int(input("How many of these product do we have? "))
            if quantity > 0:
                break
            print("Invalid quantity. Try again.")

        # Store the new product
        product_names.append(new_name)
        product_costs.append(cost_new_product)
        product_stock.append(quantity)
        print("Product added!")
        print()
            
    else:
        print("Invalid option, try again")
        print()
        
            
        
        
    
    
