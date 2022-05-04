import tkinter as tk
import AdventureDriver as ad
import os
import pyttsx3

# from TangoRobot import *
import time

clear = lambda: os.system('cls')


class GameController:



    def __init__(self):
        self.game = ad.AdventureDriver()
        self.game.outputBoard()
        temp = self.game.getCharacterPosition()
        print("Y = ", temp[0], "X = ", temp[1])

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)
        self.engine.setProperty('rate', 150)

        self.saying()

        self.roundsPlayed = 0
        self.maxRounds = 25

        # tkinter window
        self.win = tk.Tk()
        # setup keybindings
        self.win.bind('<w>', self.move)  # key code: 25
        self.win.bind('<s>', self.move)  # key code: 39
        self.win.bind('<a>', self.move)  # key code: 38
        self.win.bind('<d>', self.move)  # key code: 40
        # start tkinter window
        self.win.mainloop()

    def saying(self):
        moves = self.game.checkForMoves()
        spokenMoves = "You can go"
        if moves[0]:
            spokenMoves += " , North"
        if moves[1]:
            spokenMoves += " , South"
        if moves[2]:
            spokenMoves += " , East"
        if moves[3]:
            spokenMoves += " , North"
        self.engine.say(spokenMoves)
        self.engine.runAndWait()

    def move(self, event):
        keycode = event.keycode
        y = self.game.getCharacterPosition()[0]
        x = self.game.getCharacterPosition()[1]
        yLen = self.game.getSize()[0]
        xLen = self.game.getSize()[1]
        moves = self.game.checkForMoves()
        if self.roundsPlayed <= self.maxRounds:
            self.saying()

            if keycode == 87:
                print("W")
                if moves[0] and y > 0:
                    self.game.move(y - 1, x)
                else:
                    print("That's a wall!")

            if keycode == 83:
                print("S")
                if moves[1] and y < yLen:
                    print("South")
                    self.game.move(y + 1, x)
                else:
                    print("That's a wall!")

            if keycode == 68:
                print("D")
                if moves[2] and x < xLen:
                    print("East")
                    self.game.move(y, x + 1)
                else:
                    print("That's a wall!")

            if keycode == 65:
                print("A")
                if moves[3] and x > 0:
                    print("West")
                    self.game.move(y, x - 1)
                else:
                    print("That's a wall!")

            self.game.outputBoard()
            temp = self.game.getCharacterPosition()
            print("Y = ", temp[0], "X = ", temp[1])

            self.roundsPlayed += 1

        # self.engine.say(spokenMove)
        # self.engine.runAndWait()



#
GameController()
# roundsPlayed += 1
