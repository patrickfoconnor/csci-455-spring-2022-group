import tkinter as tk
import AdventureDriver as ad
import os
#from TangoRobot import *
import time

clear = lambda: os.system('cls')


class GameController:

    def __init__(self, game):
        # tkinter window
        self.win = tk.Tk()
        # setup keybindings
        self.win.bind('<w>', self.move)  # key code: 25
        self.win.bind('<s>', self.move)  # key code: 39
        self.win.bind('<a>', self.move)  # key code: 38
        self.win.bind('<d>', self.move)  # key code: 40
        # start tkinter window
        self.win.mainloop()
        self.game = game

    def move(self, event):
        keycode = event.keycode
        y = self.game.getCharacterPosition()[0]
        x = self.game.getCharacterPosition()[1]
        yLen = self.game.getSize()[0]
        xLen = self.game.getSize()[1]
        moves = self.game.checkForMoves()
        if keycode == 87:
            print("W")
            if moves[0] and x > 0:
                print("North")
                self.game.setCharacterPosition(y, x-1)
            else:
                print("That's a wall!")

        if keycode == 83:
            print("S")
            if moves[1] and x < xLen:
                print("South")
                self.game.setCharacterPosition(y, x+1)
            else:
                print("That's a wall!")

        if keycode == 68:
            print("D")
            if moves[2] and y < yLen:
                print("East")
                self.game.setCharacterPosition(y+1, x)
            else:
                print("That's a wall!")

        if keycode == 65:
            print("A")
            if moves[3] and y > 0:
                print("West")
                self.game.setCharacterPosition(y-1, x)
            else:
                print("That's a wall!")

        self.display()



game = ad.AdventureDriver()
game.outputBoard()
temp = game.getCharacterPosition()
print("Y = ", temp[0], "X = ", temp[1])
GameController(game)
