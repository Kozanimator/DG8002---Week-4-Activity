# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Stephan Kozak
# Date: October 8, 2026

# SCENARIO
# A restauraunt wants a simple ordering system that allows customers to browse a menu, select items, and calculate their total bill.

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []

# TODO 1: Print out the entire menu and the price of each item
for item in menu:
    print(f"{item}: ${menu[item]:.2f}")

# TODO 2: Start a loop, asking the customer which item they would like to order
requested_item = ""
while requested_item != "Done":
    requested_item = input(
        "What would you like to order? Type Done to finish: "
    ).strip().title()
        
    # TODO 3: If the customer types a word check whether the requested item exists
    if requested_item in menu:

    # TODO 4: Add valid items to the customer's order and let the loop continue
        order.append(requested_item)
        print(f"Added {requested_item}.")
        
    # TODO 5: if the customer types "Done", end the loop and move to end of order
    elif requested_item != "Done":
        print("That item is not on the menu.")
        
# TODO 6: Print out an itemized receipt for the user showing item and cost
print("\nYOUR RECEIPT")
subtotal = 0
for item in order:
    print(f"{item}: ${menu[item]:.2f}")
    subtotal += menu[item]
    
# TODO 7: Print out the subtotal of the entire order
print(f"SUBTOTAL: ${subtotal:.2f}")

# EXPECTED OUTPUT
# Order: Burger - 12.00
#        Fries  -  5.00
#        Drink  -  3.00
#         TOTAL: $20.00
