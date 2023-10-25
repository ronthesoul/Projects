import re

# First of all, I defined an id_counter so it wouldn't overlap menu dict where the key is the category
# and the value is another dict inside the second dict, the key is the id number, and the value is another dict
# where every value of the product is categorized
# and last, I made a shopping cart list to hold the cart products

id_options = list(range(1, 10001))
menu = {
    "Meat": {
        id_options.pop(0): {"name": "Chicken", "calories": "200K", "protein": "50P", "price": "15$"},
        id_options.pop(0): {"name": "Beef", "calories": "350K", "protein": "62P", "price": "18$"}
    },
    "Dairy": {
        id_options.pop(0): {"name": "Cheese", "calories": "320K", "protein": "5P", "price": "6$"},
        id_options.pop(0): {"name": "Blue Cheese", "calories": "120K", "protein": "8P", "price": "8$"}
    }
}
shopping_cart = []


# This function receives a name and adds a category to the menu and creates an empty dict
def add_category():
    category_name = input("Enter the category name: ")
    menu[category_name] = {}
    print(f"{category_name} category added to the menu.")


# This function inputs a category checks if it's in the menu and asks for the product values
# It uses the re lib to ensure that the price is in the num$ format
def add_product():
    category_name = input("Enter the category name: ")
    if category_name not in menu:
        print("Category not found. Please add the category first.")
    else:
        product_name = input("Enter the product name: ")
        calories = input("Enter calories: ")
        protein = input("Enter protein: ")
        price = input("Enter price: ")
        if not re.match(r'^\d+\$$', price):
            print("The price should be a number and $ (e.g., 8$)")
        else:
            menu[category_name][id_options.pop(0)] = {
                "name": product_name,
                "calories": calories,
                "protein": protein,
                "price": price
            }
            print(f"{product_name} added to {category_name} category.")


# this functions asks for a name or ID number and removes the item
def remove_product():
    product_input = input("Enter the product name or ID: ")

    if product_input.isdigit():
        product_id = int(product_input)
        for category, products in menu.items():
            if product_id in products:
                product_name = menu[category][product_id]["name"]
                del menu[category][product_id]
                id_options.append(product_id)
                print(f"Product with ID {product_id} ({product_name}) removed from the menu.")
                return
        print(f"Product with ID {product_id} not found in the menu.")
    else:
        product_name = product_input.lower()
        found = False
        for category, products in menu.items():
            for product_id, product_info in products.items():
                if product_info["name"].lower() == product_name:
                    del menu[category][product_id]
                    id_options.append(product_id)
                    found = True
                    print(f"{product_name.capitalize()} removed from the menu.")
                    break
        if not found:
            print("Product not found in the menu.")


# This function asks for a name and updates it with new inputs
def update_product():
    product_name = input("Enter the product name: ")
    for category, products in menu.items():
        for product_id, product_info in products.items():
            if product_info["name"].lower() == product_name.lower():
                product_info["name"] = input("Enter new product name: ")
                product_info["calories"] = input("Enter new calories: ")
                product_info["protein"] = input("Enter new protein: ")
                product_info["price"] = input("Enter new price: ")
                print(f"{product_name} updated in the menu.")
                return
    print("Product not found in the menu.")


# This functions asks for a name and quantit and adds is to the shopping cart array
def add_to_cart():
    product_name = input("Enter the product name: ")
    quantity_input = input("Enter the quantity: ")

    # Check if the input is empty or not a number
    if not product_name or not quantity_input or not quantity_input.isdigit():
        print("Invalid input. Please enter a valid product name and quantity.")
        return

    quantity = int(quantity_input)

    for category, products in menu.items():
        for product_id, product_info in products.items():
            if product_info["name"].lower() == product_name.lower():
                total_price = float(product_info["price"].replace("$", "")) * quantity
                shopping_cart.append({
                    "name": product_info["name"],
                    "quantity": quantity,
                    "price": product_info["price"],
                })
                print(f"{quantity} {product_name} added to the cart.")
                return
    print("Product not found in the menu.")


# this function asks for a name and removes the item
def remove_from_cart():
    product_name = input("Enter the product name: ")
    for item in shopping_cart:
        if item["name"].lower() == product_name.lower():
            shopping_cart.remove(item)
            print(f"{product_name} removed from the cart.")
            return
    print("Product not found in the cart.")


# This function prints the shopping cart as a tables (i learned how to do the table format with chat gpt so don't think i am that good)
#But now i know how to do it
def view_cart():
    if not shopping_cart:
        print("Shopping cart is empty.")
    else:
        print("\nShopping Cart:")
        print("{:<10} {:<20} {:<10} {:<10}".format("Quantity", "Name", "Price", "Total Price"))
        for item in shopping_cart:
            total_price = float(item["price"].replace("$", "")) * item["quantity"]
            print("{:<10} {:<20} {:<10} {:<10}".format(item["quantity"], item["name"], item["price"], f"${total_price:.2f}"))


# this function makes the price a float the strips the $ so it could do the math and give me the amount you have to pay
def purchase(shopping_cart):
    total_price = 0

    for item in shopping_cart:
        item_price = float(item["price"].replace("$", ""))
        item_total_price = item_price * item["quantity"]
        total_price += item_total_price

    total_price_with_maam = total_price * 1.17
    print(f"The total price is {total_price_with_maam:.2f} including maam")


# This is the main loop it asks for an input so you could go between the product menu and shopping menu
while True:
    print("\nSV Super Market")
    print("1. Product Menu")
    print("2. Shopping Cart")
    print("3. Exit")
    choice = input("Select an option: ")
# prints the menu as table as i did in the shopping cart so all th products could be displayed
    if choice == "1":
        flag = False
        while not flag: # this is the menu while loop so it would keep going until you go back
            print("\nProduct Menu:")
            print("{:<10} {:<10} {:<20} {:<10} {:<10} {:<10}".format("Category", "ID", "Name", "Calories", "Protein", "Price"))
            for category, products in menu.items():
                for product_id, product_info in products.items():
                    print("{:<10} {:<10} {:<20} {:<10} {:<10} {:<10}".format(category, product_id,
                                                                              product_info["name"],
                                                                              product_info["calories"],
                                                                              product_info["protein"],
                                                                              product_info["price"]))
            print("\n1. Add Category")
            print("2. Add Product")
            print("3. Remove Product")
            print("4. Update Product")
            print("5. Print Menu")
            print("6. Back")
            submenu_choice = input("Select an option: ")

            if submenu_choice == "1":
                add_category()
            elif submenu_choice == "2":
                add_product()
            elif submenu_choice == "3":
                remove_product()
            elif submenu_choice == "4":
                update_product()
            elif submenu_choice == "5":
                continue
            elif submenu_choice == "6":
                flag = True
            else:
                print("Invalid choice. Please select a valid option.")

    elif choice == "2":
        flag = False
        while not flag: # this is the shopping cart menu while loop
            print("\nShopping Cart:")
            view_cart()
            print("\n1. Add to Cart")
            print("2. Remove from Cart")
            print("3. Purchase")
            print("4. Back")
            cart_choice = input("Select an option: ")

            if cart_choice == "1":
                add_to_cart()
            elif cart_choice == "2":
                remove_from_cart()
            elif cart_choice == "3":
                purchase(shopping_cart)
            elif cart_choice == "4":
                flag = True
            else:
                print("Invalid choice. Please select a valid option.")

    elif choice == "3":
        print("Bye")
        break
    else:
        print("Invalid choice. Please select a valid option.")



#Note most of the script was written by myself i used chatgpt to fix small mistakes and also learn about libs and other
#concepts i didn't know before ;))
