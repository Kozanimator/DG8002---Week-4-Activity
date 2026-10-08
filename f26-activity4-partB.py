# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Stephan kozak
# Date: 2026 10 08

# SCENARIO
# You are developing a registration system for a small event
# The organizers have a list of registered attendees and need to check whether someone is permitted to enter.

registered_guests = [
    "Alice",
    "Bob"
]


# TODO 1: Create a while loop thap that continues until all guests are checked in.
checked_in_guests = []
print(f"Registered Guests: {registered_guests}")
while len(checked_in_guests) < len(registered_guests):

    # TODO 2: Ask the user to enter their name
       name = input("What is your name: ").strip()
    
    # TODO 3: Iterate through guest list and check whether their name appears in the registered guests list
  matching_guest = ""
    for guest in registered_guests:
        if name.lower() == guest.lower():
            matching_guest = guest
            break
            
    # TODO 4: If registered and they're not already in checked in, add their name to the checked-in list and print a welcome message
    if matching_guest and matching_guest not in checked_in_guests:
        checked_in_guests.append(matching_guest)
        print(f"Welcome {matching_guest}!")
    elif matching_guest in checked_in_guests:
        print(f"{matching_guest}, you have already checked in.")
        
    # TODO 5: Otherwise, Display an appropriate message for unregistered guests
    else:
        print(f"Sorry {name}, your name isn't on the list.")
        
    # TODO 6: Print the updated checked-in list
    print(f"Checked In Guests: {checked_in_guests}")

# TODO 7: Print a message telling us that all guests have successfully checked in!
print("All guests have been checked in!")

# EXPECTED OUTPUT:
# [ "Alice", "Bob"]
# What is your name:  "Alice"
#    Welcome Alice!
#    Checked In Guests: [ Alice ]
# What is your name:  "Fred"
#    Sorry Fred, your name isn't on the list.
#    Checked In Guests: [ Alice ]
# What is your name:  "Bob"
#    Welcome Bob!
#    Checked In Guests: [ Alice, Bob ]
# All guests have been checked in!
