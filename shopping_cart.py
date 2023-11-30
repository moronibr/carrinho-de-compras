print("Welcome to the Shopping Cart program \n")

cart = []

while True:

    select = int(input("Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit \n Please enter an action:"))
    
    if select == 1:
        add_item = str(input("What item would you like to add? "))
        item_price = float(input(f"What is the price of {add_item}? "))
        cart.append((add_item, item_price))
        print(f"{add_item} has been added to the cart")
        print()
    elif select == 2:
        if len(cart) == 0:
            print("Your cart is empty")
            print()
        else:
            print("The contents of the shopping cart are: ")
            print()
            item_number = 1  
            for item, price in cart:
                print(f"{item_number} - {item} - ${price}")
                item_number += 1
            print()    
    elif select == 3:
        if len(cart) == 0:
           print("Your cart is empty")
           print()
        else:
            print("The contents of the shopping cart are: ")
            print()
            item_number = 1  
            for item, price in cart:
                print(f"{item_number} - {item} - ${price}")
                item_number += 1
            print()
            remove = int(input("Which item would you like to remove? "))
            if remove <= len(cart):
                removed_item = cart.pop(remove - 1)
                print(f"{removed_item[0]} has been removed from the cart")
            else:
                print("Invalid item number")
    elif select == 4:
        if len(cart) == 0:
            print("Your cart is empty")
            print()
        else:
            print("The contents of the shopping cart are: ")
            print()
            item_number = 1  
            for item, price in cart:
                print(f"{item_number} - {item} - ${price}")
                item_number += 1
            print()
            total = 0
            for item, price in cart:
                total += price
            print(f"The total price of the items in the shopping cart is  ${total}")
            print()
    elif select == 5:
        print("Thank you. Goodbye.")
        break
        