import tkinter as tk
import AdventureDriver as ad
#from TangoRobot import *
import time


class KeyboardController:

    def __init__(self):
        # tkinter window
        self.win = tk.Tk()
        self.game = ad.AdventureDriver()
        # setup keybindings
        self.win.bind('<w>', self.move)  # key code: 25
        self.win.bind('<s>', self.move)  # key code: 39
        self.win.bind('<a>', self.move)  # key code: 38
        self.win.bind('<d>', self.move)  # key code: 40
        # start tkinter window
        self.win.mainloop()

    def move(self, event):
        keycode = event.keycode
        x = self.game.getCharacterPosition()[0]
        y = self.game.getCharacterPosition()[1]
        xLen = self.game.getSize()[0]
        yLen = self.game.getSize()[1]
        moves = self.game.checkForMoves()
        print(keycode)
        if keycode == 87:
            print("W")
            if moves[0] and x > 0:
                print("North")
                self.game.setCharacterPosition(x-1, y)
            else:
                print("That's a wall!")

        if keycode == 83:
            print("S")
            if moves[1] and x < xLen:
                print("South")
                self.game.setCharacterPosition(x+1, y)
            else:
                print("That's a wall!")

        if keycode == 68:
            print("D")
            if moves[2] and y < yLen:
                print("East")
                self.game.setCharacterPosition(x, y+1)
            else:
                print("That's a wall!")

        if keycode == 65:
            print("A")
            if moves[3] and y > 0:
                print("West")
                self.game.setCharacterPosition(x, y-1)
            else:
                print("That's a wall!")

        print(self.game.getCharacterPosition())

KeyboardController()
