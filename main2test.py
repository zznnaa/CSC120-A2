# Import a few useful containers from the typing module
from typing import Dict, Union

#Import computer
from computer import Computer

# Import the functions we wrote in oo_resale_shop.py
from oo_resale_shop import ResaleShop

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""

def main():
    
    ##change "make a computer" function into using object oriented class, but theoretically main should still call all our functions
    ##also might need to change item_id into an attribute of the computer?
    # First, let's make a computer
    computer_resale_store = ResaleShop({}, 0)
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = computer_resale_store.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computer_resale_store.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    computer_resale_store.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computer_resale_store.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    computer_resale_store.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computer_resale_store.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()