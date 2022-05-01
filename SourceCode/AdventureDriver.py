# Main class that will hold the driver for the adventure-based combat game

from enum import Enum


# Base game board

# Numerical = Node, P = Path, W = Wall
# +-----------------+
# |1 P P P 2 P P P 3|
# |W W W W P W W W P|
# |W W W W P W W W P|
# |W W W W P W W W P|
# |W W W W P W W W P|
# |4 P P P 5 W W W 6|
# |P W W W P W W W W|
# |P W W W P W W W W|
# |P W W W P W W W W|
# |7 W W W 8 P P P 9|


class AdventureDriver:

    # constructor
    def __init__(self):
        self.createObjectDict(9)
        self.createGameBoard(2)

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

    def populateGameBoard(baseGameBoard):
        for row in baseGameBoard:
            for col in row:
                if col.isdigit():
                    baseGameBoard[row][col] = baseGameBoard.objectDict[col]

    def createGameBoard(level):
        if level == 1:
            pass
        elif level == 2:
            baseGameBoard = [[1, "P", "P", "P", 2, "P", "P", "P", 3],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             [4, "P", "P", "P", 5, "W", "W", "W", 6],
                             ["P", "W", "W", "W", "P", "W", "W", "W", "W"],
                             ["P", "W", "W", "W", "P", "W", "W", "W", "W"],
                             ["P", "W", "W", "W", "P", "W", "W", "W", "W"],
                             [7, "W", "W", "W", 8, "W", "W", "W", 9]]
            level.populateGameBoard(baseGameBoard)

    ## NEED TO FINISH
    def createObjectDict(objectCount, randomObject=None):
        objectDict = {}
        for i in range(objectCount):
            objectDict[i] = randomObject
