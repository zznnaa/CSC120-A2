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

    #sell a computer
    #refurbish computer
    #update computer price
    #update computer os

def main():
    computer_resale_store = ResaleShop({}, 0)
    computer1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    computer_resale_store.buy(computer1)
    print(computer_resale_store.itemID)

if __name__ == "__main__":
    main()
