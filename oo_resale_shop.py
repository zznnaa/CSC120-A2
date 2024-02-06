from computer import Computer

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
    # def update_price(self, item_id: int, new_price: int):
    # if item_id in self.inventory:
    #     self.inventory[item_id]["price"] = new_price
    # else:
    #     print("Item", item_id, "not found. Cannot update price.")

    #sell a computer
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    #refurbish computer
    #update computer os
    #print inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id].__dict__}')
        else:
            print("No inventory to display.")

def main():
    computer_resale_store = ResaleShop({}, 0)
    computer1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    computer2 = Computer("test", "test", 1111, 11, "test", 1111, 1111)
    computer_resale_store.buy(computer1)
    computer_resale_store.buy(computer2)
    print(computer_resale_store.itemID)
    item_id : int
    item_id = 1
    computer_resale_store.sell(item_id)
    computer_resale_store.print_inventory()

##computer 1 and item_id placeholders here until I figure out the main.py code


if __name__ == "__main__":
    main()
