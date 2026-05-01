# Name: Estella Cheng
# Date: November 10, 2025
# Class Section: 001
# Assignment 10_Part #1

inventory = {
 'soft drink': [0.99, 10],
 'onion rings': [1.29, 5],
 'small fries': [1.49, 20]
 }

# Main program loop
while True:
    choice = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

    # -------- Quit ----------
    if choice == "q":
        print("See you soon!")
        break


    # -------- Search ----------
    elif choice == "s":
        name = input("Enter a product name: ")

        # Check if product exists
        if name in inventory.keys():
            price = inventory[name][0]
            stock = inventory[name][1]
            print("We sell '" + name + "' at " + str(price) + " per unit")
        else:
            print("Sorry, we don't sell '" + name + "'")


    # -------- List Inventory ----------
    elif choice == "l":
        print(format("Product", "<18"), format("Price", "<8"), format("Quantity", "<9"))

        for key in sorted(inventory.keys()):
            price = inventory[key][0]
            quantity = inventory[key][1]
            print(
                format(key, "<18"),
                format(price, "<8.2f"),
                format(quantity, "<9"))


    # -------- Add Product ----------
    elif choice == "a":
        # Get a new product name
        name = input("Enter a product name: ")
        if name in inventory:
            print("Duplicate product name")
        else:
            # Get a price > 0
            while True:
                try:
                    price = float(input("Enter a price: "))
                    if price > 0:
                        break
                    print("Invalid range, try again")
                except:
                    print("Invalid input, please enter a valid number")

            # Get a quantity > 0 and <= 100
            while True:
                try:
                    quantity = int(input("Enter an inventory amount: "))
                    if quantity > 0 and quantity <= 100:
                        break
                    print("Invalid range, try again")
                except:
                    print("Invalid input, please enter a valid number")

            inventory[name] = [price, quantity]
            print("Product added")


    # -------- Remove Product ----------
    elif choice == "r":
        name = input("Enter a product name: ")

        if name not in inventory:
            print("Unknown product name")
        else:
            del inventory[name]
            print("Product removed")


    # -------- Update Product ----------
    elif choice == "u":
        name = input("Enter a product name: ")

        if name not in inventory:
            print("Unknown product name")

        else:
            changes = input("(n)ame, (p)rice or (a)mount? ")

            # --- Update name ---
            if changes == "n":
                newname = input("Enter a new name: ")
                if newname in inventory:
                    print("Product name already exists")
                else:
                    info = inventory[name]
                    del inventory[name]
                    inventory[newname] = info
                    print("Product renamed")

            # --- Update price ---
            elif changes == "p":
                while True:
                    try:
                        newprice = float(input("Enter a new price: "))
                        if newprice > 0:
                            inventory[name][0] = newprice
                            print("Price updated")
                            break
                        else:
                            print("Invalid range, try again")
                    except:
                        print("Invalid input, please enter a valid number")

            # --- Update quantity ---
            elif changes == "a":
                while True:
                    try:
                        new_quantity = int(input("Enter a new amount: "))
                        if new_quantity > 0 and new_quantity <= 100:
                            inventory[name][1] = new_quantity
                            print("Amount updated")
                            break
                        else:
                            print("Invalid range, try again")
                    except:
                        print("Invalid input, please enter a valid number")

            else:
                print("Invalid option")


    # -------- Report Feature ----------
    elif choice == "e":
        # Find total cost 
        total = 0.0
        for item in inventory:
            total += inventory[item][0] * inventory[item][1]

        # Find max/min price
        keys = sorted(inventory.keys())
        # Assuming the first item is both the max and min
        max_key = keys[0]
        min_key = keys[0]
        for item in keys:
            if inventory[item][0] > inventory[max_key][0]:
                max_key = item
            if inventory[item][0] < inventory[min_key][0]:
                min_key = item

        print("Total cost of all items in inventory:", total)
        print("Highest priced item:", inventory[max_key][0], "is", max_key)
        print("Lowest priced item:", inventory[min_key][0], "is", min_key)


        # -------- Invalid Menu Option ----------
    else:
        print("Unknown command, try again")







