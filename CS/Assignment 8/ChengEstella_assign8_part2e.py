# Name: Estella Cheng
# Date: November 5, 2025
# Class Section: 001
# Assignment 08_Part #2e

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_stock = [10, 5, 20] # 10 soft drinks, 5 onion rings, 20 small fries 

while True:
    choice = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: ")

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
        print(format("Product", "<20"), format("Price", ">8"), format("Quantity", ">9"))
        i = 0
        while i < len(product_names):
            print(
            format(product_names[i], "<20"),
            format(product_costs[i], ">8.2f"),
            format(product_stock[i], ">9"))
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

    elif choice == "r":
        # Remove a product if it exists
        remove_name = input("Enter a product name: ")
        if remove_name in product_names:
            index = product_names.index(remove_name)
            del product_names[index]
            del product_costs[index]
            del product_stock[index]
            print("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
        print()

    elif choice == "u":
        # Update an existing product (name, cost, or quantity)
        updated_product = input("Enter a product name: ")

        if updated_product not in product_names:
            print("Product doesn't exist. Can't update.")
            print()
        else:
            idx = product_names.index(updated_product)
            print("What would you like to update?")
            changes = input("(n)ame, (c)ost or (q)uantity: ")

            if changes == "n":
                # Keep asking until the new name is not a duplicate of another product
                while True:
                    new_name = input("Enter a new name: ")
                    if (new_name in product_names) and (new_name != product_names[idx]):
                        print("Duplicate name!")
                    else:
                        product_names[idx] = new_name
                        print("Product name has been updated")
                        break
                print()

            elif changes == "c":
                # Update cost (>0). Keep asking until valid.
                while True:
                    new_cost = float(input("Enter a new cost: "))
                    if new_cost > 0:
                        product_costs[idx] = new_cost
                        print("Product cost has been updated")
                        break
                    else:
                        print("Invalid cost!")
                print()

            elif changes == "q":
                # Update quantity (>0). Keep asking until valid.
                while True:
                    new_quantity = int(input("Enter a new quantity: "))
                    if new_quantity > 0:
                        product_stock[idx] = new_quantity
                        print("Product quantity has been updated")
                        break
                    else:
                        print("Invalid quantity!")
                print()
                
            else:
                print("Invalid option")
                print()
                         
    else:
        print("Invalid option, try again")
        print()
        
            
        
        
    
    
