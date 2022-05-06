import tkinter as tk
import AdventureDriver as ad
import os
import pyttsx3
import speech_recognition as sr


#from TangoRobot import *
import time as timeLib

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
        self.engine.setProperty('voice', 'english')

        self.saying()

        self.roundsPlayed = 0
        self.maxRounds = 25

        self.listening = True

        self.output = ""


        '''
        # tkinter window
        self.win = tk.Tk()
        # setup keybindings
        self.win.bind('<w>', self.move)  # key code: 25
        self.win.bind('<s>', self.move)  # key code: 39
        self.win.bind('<a>', self.move)  # key code: 38
        self.win.bind('<d>', self.move)  # key code: 40
        # start tkinter window
        self.win.mainloop()
        '''

    def saying(self):
        moves = self.game.checkForMoves()
        print(moves)
        spokenMoves = ",, You can go"
        if moves[0]:
            spokenMoves += " , North"
        if moves[1]:
            spokenMoves += " , South"
        if moves[2]:
            spokenMoves += " , East"
        if moves[3]:
            spokenMoves += " , West"
        self.engine.say(spokenMoves)
        self.engine.runAndWait()

    def move(self, word):
        y = self.game.getCharacterPosition()[0]
        x = self.game.getCharacterPosition()[1]
        yLen = self.game.getSize()[0]
        xLen = self.game.getSize()[1]
        moves = self.game.checkForMoves()
        self.output = " "

        if word in "North":
            if moves[0] and y-4 > 0:
                time.sleep(.2)
                time.sleep(0.2)
                runTimeD = 0
                waitTimeD = 3

                while runTimeD <= waitTimeD:
                    timeStartD = timeLib.time()
                    robot.driveForward()
                    timeEndD = timeLib.time()
                    runTimeD += timeEndD - timeStartD
                robot.resetWheels()
                robot.speed = 6000

                self.game.move(y - 4, x)
            else:
                self.output = "That's a wall!"

        if word in "South":
            if moves[1] and y+4 < yLen:
                self.game.move(y + 4, x)
                waitTime = 22
                runTime = 0
                while runTime <= waitTime:
                    timeStart = timeLib.time()
                    robot.turnLeft()
                    timeEnd = timeLib.time()
                    runTime += timeEnd - timeStart
                runTimeD = 0
                waitTimeD = 3
                time.sleep(0.2)
                robot.speed(6500)
                while runTimeD <= waitTimeD:
                    timeStartD = timeLib.time()
                    self.guiRobot.driveForward()
                    timeEndD = timeLib.time()

                    runTimeD += timeEndD - timeStartD
                robot.resetWheels()
                robot.speed = 6000
            else:
                self.output = "That's a wall!"

        if word in "East":
            if moves[2] and x+4 < xLen:
                self.game.move(y, x + 4)
                waitTime = 5
                runTime = 0
                while runTime <= waitTime:
                    timeStart = timeLib.time()
                    robot.turnRight()
                    timeEnd = timeLib.time()
                    runTime += timeEnd - timeStart
                time.sleep(0.2)
                runTimeD = 0
                waitTimeD = 3
                robot.speed(6500)
                while runTimeD <= waitTimeD:
                    timeStartD = timeLib.time()
                    robot.driveForward()
                    timeEndD = timeLib.time()
                    runTimeD += timeEndD - timeStartD
                robot.resetWheels()
                robot.speed = 6000
            else:
                self.output = "That's a wall!"

        if word in "West":
            if moves[3] and x-4 > 0:
                self.game.move(y, x - 4)
                waitTime = 5
                runTime = 0
                while runTime <= waitTime:
                    timeStart = timeLib.time()
                    robot.turnLeft()
                    timeEnd = timeLib.time()
                    runTime += timeEnd - timeStart
                time.sleep(0.2)
                runTimeD = 0
                waitTimeD = 3
                robot.speed(6500)
                while runTimeD <= waitTimeD:
                    timeStartD = timeLib.time()
                    robot.driveForward()
                    timeEndD = timeLib.time()
                    runTimeD += timeEndD - timeStartD
                robot.resetWheels()
                robot.speed = 6000
            else:
                self.output = "That's a wall!"

        self.engine.say(self.output)
        self.engine.runAndWait()
        self.game.outputBoard()
        temp = self.game.getCharacterPosition()
        print( "Y = ", temp[0], "X = ", temp[1] )

        self.roundsPlayed += 1

    def listen(self):
        while self.listening and self.roundsPlayed <= self.maxRounds:
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.adjust_for_ambient_noise( source )
                r.dynamic_energythreshhold = 3000

                self.output = ""
                self.saying()

                try:
                    print("listening")
                    audio = r.listen(source)
                    print("Got audio")
                    word = r.recognize_google(audio)
                    print(word)
                    self.move(word)
                except sr.UnknownValueError:
                    print( "Word not recognized" )
    '''
    def listen(self):
        while self.roundsPlayed <= self.maxRounds:
            print("...")
            word = input()
            self.saying()
            self.move(word)
    '''

GameController().listen()
