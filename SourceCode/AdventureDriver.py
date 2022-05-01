# Main class that will hold the driver for the adventure-based combat game
import random
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
import self as self

from SourceCode.Character import Player, Easy, Hard


def populateGameBoard(baseGameBoard, objectArray):
    objectsPlaced = 0
    for i in range(len(baseGameBoard)):
        for j in range(len(baseGameBoard[i])):
            if isinstance(baseGameBoard[i][j], int):
                if objectArray[objectsPlaced] == "S":
                    startingPositionX = i
                    startingPositionY = j
                baseGameBoard[i][j] = objectArray[objectsPlaced]
                objectsPlaced += 1
    return baseGameBoard, startingPositionX, startingPositionY


def checkWest(player):
    pass


def checkNorth():
    pass


def checkEast():
    pass


def checkSouth():
    pass


class AdventureDriver:

    # constructor
    def __init__(self):
        # Create the player
        player = Player()
        player.name = "Player01"

        player.flvrtxt = "Just a trying to finish the semester"

        self.objectArray = self.createObjectArray(9)
        self.gameBoard, self.startingPositionX, self.startingPositionY = self.createGameBoard(2)

    def checkForMoves(self, player):
        northMove = checkNorth(self)
        eastMove = checkEast(self)
        southMove = checkSouth(self)
        westMove = checkWest(self)

    # Define all of the actions are available for game
    def battle(self, player, enemy):
        pass

    # Get random num between 1-100 if 1-25 fleeing failed, if greater than 25 run successful
    def run(self, player):
        pass

    # Recharge all Hit points for given player
    def rechargeHealth(self, player):
        pass

    # def populateGameBoard(baseGameBoard):

    def createGameBoard(self, level):
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
            return populateGameBoard(baseGameBoard, self.objectArray)

    # The array will be created and then shuffled
    #   Each index will then hold the object
    #  Start = S
    #  End = E
    #  Recharge Station = R
    #  (4) Weak Bad Guys = Y
    #  (2) Hard bad guys = H
    def createObjectArray(self, objectCount):

        # Create four bad guys
        easyEnemyTurtle = Easy()
        easyEnemyTurtle.setName("Turtle")
        easyEnemyRabbit = Easy()
        easyEnemyRabbit.setName("Rabbit")
        easyEnemySnail = Easy()
        easyEnemySnail.setName("Snail")
        easyEnemyMagpie = Easy()
        easyEnemyMagpie.setName("Magpie")

        hardEnemyKeyLess = Hard()
        hardEnemyKeyLess.loot = "none"
        hardEnemyKeyBearer = Hard()
        hardEnemyKeyBearer.loot = "Golden Key"

        objectArray = [self.player, easyEnemyTurtle, easyEnemyRabbit, easyEnemySnail, easyEnemyMagpie, hardEnemyKeyLess,
                       hardEnemyKeyBearer, "S", "E", "R"]
        # Randomize the association of index and object
        random.shuffle(objectArray)
        return objectArray


adventure01 = AdventureDriver()
print(adventure01.gameBoard)
print(adventure01.startingPositionX)
print(adventure01.startingPositionY)

