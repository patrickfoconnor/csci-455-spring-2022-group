# Main class that will hold the driver for the adventure-based combat game

from enum import Enum


class AdventureDriver:
    # constructor
    def __init__(self):
        pass

    # Define all of the actions are available for game
    def battle(self, player, enemy):
        pass

    # Get random num between 1-100 if 1-25 fleeing failed, if greater than 25 run successful
    def run(self, player):
        pass

    # Recharge all Hit points for given player
    def rechargeHealth(self, player):
        pass

    # Populate all 9 nodes with 1 start, 1 end, 1 recharge station, 4 weak enemies, 2 hard enemies one with a key
    def populateNodes(self):
        pass


