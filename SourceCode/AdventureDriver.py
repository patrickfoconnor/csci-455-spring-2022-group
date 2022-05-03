# Main class that will hold the driver for the adventure-based combat game
import random
import time
#from enum import Enum

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
#import self as self

from SourceCode.Character import Player, Easy, Hard


def populateGameBoard(baseGameBoard, objectArray):
    objectsPlaced = 0
    startingPositionX, startingPositionY = 0, 0
    for i in range(len(baseGameBoard)):
        for j in range(len(baseGameBoard[i])):
            if isinstance(baseGameBoard[i][j], int):
                if objectArray[objectsPlaced] == "S":
                    startingPositionX = j
                    startingPositionY = i
                baseGameBoard[i][j] = objectArray[objectsPlaced]
                objectsPlaced += 1
    return baseGameBoard, startingPositionX, startingPositionY


def checkNorth(player, gameBoard):
    playerX, playerY = player.getPosition()
    if playerY > 0:
        print("North True", playerX, playerY, len(gameBoard))
        print(gameBoard[playerX][playerY - 1])
        if gameBoard[playerX][playerY - 1] != "W":
            return True
    return False

def checkSouth(player, gameBoard):
    playerX, playerY = player.getPosition()
    if playerY < len(gameBoard[1])-1:
        print("South True", playerX, playerY, len(gameBoard))
        if gameBoard[playerX][playerY + 1] != "W":
            return True
    return False

def checkEast(player, gameBoard):
    playerX, playerY = player.getPosition()
    if playerX < len(gameBoard)-1:
        print("East", playerX, playerY, len(gameBoard))
        if gameBoard[playerX + 1][playerY] != "W":
            return True
    return False

def checkWest(player, gameBoard):
    playerX, playerY = player.getPosition()
    if playerX > 0:
        print("West", playerX, playerY, len(gameBoard))
        if gameBoard[playerX - 1][playerY] != "W":
            return True
    return False








class AdventureDriver:

    # constructor
    def __init__(self):
        # Create the player
        self.player = Player()
        self.player.name = "Player01"

        self.player.flvrtxt = "Just a trying to finish the semester"
        self.objectArray = self.createObjectArray()
        self.gameBoard, self.startingPositionX, self.startingPositionY = self.createGameBoard(2)
        self.player.setPosition( self.startingPositionX, self.startingPositionY )
        self.player.setPosition(self.startingPositionX, self.startingPositionY)

    def getCharacterPosition(self):
        return self.player.getPosition();

    def setCharacterPosition(self, x, y):
        self.player.setPosition(x, y)

    def getSize(self):
        return len(self.gameBoard), len(self.gameBoard[0])

    def checkForMoves(self):
        print(self.player.getPosition())
        availableActions = [checkNorth(self.player, self.gameBoard), checkSouth(self.player, self.gameBoard), checkEast(self.player, self.gameBoard), checkSouth(self.player, self.gameBoard)]
        return availableActions

    # Define all of the actions are available for game
    def battle(self, player, enemy):
        playersAtackValue = random.randint(0, player.attack)
        enemyAttackValue = random.randint(0, enemy.attack)
        player.HP -= enemyAttackValue
        enemy.HP -= playersAtackValue

    # Get random num between 1-100 if 1-25 fleeing failed, if greater than 25 run successful
    def run(self, player):
        runChance =  random.randint(0, 100)
        if runChance < 25:
            print("Run Fail")
        else:
            print("Run Success new position is: ")

    # Recharge all Hit points for given player
    def rechargeHealth(self, player):
        player.setHP(100)

    # def populateGameBoard(baseGameBoard):
    def createGameBoard(self, level):
        if level == 1:
            pass
        elif level == 2:
            baseGameBoard = [[ 1 , "P", "P", "P",  2 , "P", "P", "P",  3 ],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             ["W", "W", "W", "W", "P", "W", "W", "W", "P"],
                             [ 4 , "P", "P", "P",  5 , "W", "W", "W",  6 ],
                             ["P", "W", "W", "W", "P", "W", "W", "W", "W"],
                             ["P", "W", "W", "W", "P", "W", "W", "W", "W"],
                             ["P", "W", "W", "W", "P", "W", "W", "W", "W"],
                             [ 7 , "W", "W", "W",  8 , "P", "P", "P",  9 ]]
            return populateGameBoard(baseGameBoard, self.objectArray)

    # The array will be created and then shuffled
    #   Each index will then hold the object
    #  Start = S
    #  End = E
    #  Recharge Station = R
    #  (4) Weak Bad Guys = Y
    #  (2) Hard bad guys = H
    def createObjectArray(self):

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

    def outputBoard(self):
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if isinstance(self.gameBoard[i][j], str):
                    print(self.gameBoard[i][j], end=" ")
                else:
                    print("?", end=" ")
            print("")


adventure01 = AdventureDriver()

adventure01.outputBoard()
print(adventure01.startingPositionX, adventure01.startingPositionY)
print(adventure01.checkForMoves())


