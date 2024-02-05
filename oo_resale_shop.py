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
    def buy(computer):
    global itemID
    itemID += 1 # increment itemID
    inventory[itemID] = computer
    return itemID

    #sell a computer
    #refurbish computer
    #update computer price
    #update computer os

def main():
    computer_resale_store = ResaleShop({}, 0)

if __name__ == "__main__":
    main()
