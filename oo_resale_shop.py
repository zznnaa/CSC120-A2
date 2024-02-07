from computer import Computer
from typing import Optional

class ResaleShop:

    # What attributes will it need?
    inventory: dict
    itemID: int
    
    #inventory = [] #computer objects will go in here
    #itemID = 0
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID

    # What methods will you need?
    #buy a computer
    def buy(self, computer: Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    #update computer price
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            ##here need to update price through computer class instead of through dictionary (success)
            self.inventory[item_id].price = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    #sell a computer
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    #refurbish computer
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            if self.inventory[item_id].year_made < 2000:
                self.inventory[item_id].price = 0 # too old to sell, donation only
            elif self.inventory[item_id].year_made < 2012:
                self.inventory[item_id].price = 250 # heavily-discounted price on machines 10+ years old
            elif self.inventory[item_id].year_made < 2018:
                self.inventory[item_id].price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.inventory[item_id].price = 1000 # recent stuff
            
            if new_os is not None:
                self.inventory[item_id].operating_system = new_os
                #computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    ##finish the update the os part of this function tmrw
                
    #     computer = inventory[item_id] # locate the computer
    #     if int(computer["year_made"]) < 2000:
    #         computer["price"] = 0 # too old to sell, donation only
    #     elif int(computer["year_made"]) < 2012:
    #         computer["price"] = 250 # heavily-discounted price on machines 10+ years old
    #     elif int(computer["year_made"]) < 2018:
    #         computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
    #     else:
    #         computer["price"] = 1000 # recent stuff

    #     if new_os is not None:
    #         computer["operating_system"] = new_os # update details after installing new OS
    # else:
    #     print("Item", item_id, "not found. Please select another item to refurbish.")

    #print inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                ## .__dict__ is to list all the attributes of the computer in a dictionary
                print(f'Item ID: {item_id} : {self.inventory[item_id].__dict__}')
        else:
            print("No inventory to display.")

def main():
    computer_resale_store = ResaleShop({}, 0)
    computer1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    computer2 = Computer("test", "test", 1111, 11, "test", 2015, 1111)
    computer_resale_store.buy(computer1)
    computer_resale_store.buy(computer2)
    print(computer_resale_store.itemID)
    item_id : int
    item_id = 1
    computer_resale_store.sell(item_id)
    computer_resale_store.print_inventory()
    new_price : int
    new_price = 9
    computer_resale_store.update_price(2, new_price)
    computer_resale_store.print_inventory()
    new_os = "new_os"
    computer_resale_store.refurbish(2, new_os)
    computer_resale_store.print_inventory()

##computer 1 and item_id placeholders here until I figure out the main.py code


if __name__ == "__main__":
    main()
