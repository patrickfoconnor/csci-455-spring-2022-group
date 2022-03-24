import speech_recognition as sr
from TangoRobot import *
import time

class SpeechController:
    listening = True;

    def arrows(self, word):
        if "forward" in word:
            print("Up Arrow")
            time.sleep(.2)
            robot.driveForward()
        elif "back" in word:
            print("Down Arrow")
            time.sleep(.2)
            robot.driveBackward()
        elif "left" in word:
            print("Left Arrow")
            time.sleep(.2)
            robot.turnLeft()
        elif "right" in word:
            print("Right Arrow")
            time.sleep(.2)
            robot.turnRight()

    def waist(self, command):
        if "left" in command:
            print("Z (Left)")
            time.sleep(.2)
            robot.waistLeft()
        elif "right" in command:
            print("C (Right)")
            time.sleep(.2)
            robot.waistRight()

    def head(self, command):
        if "up" in command:
            print("W: Head Up")
            time.sleep(.2)
            robot.headUp()
        elif "down" in command:
            print("S: Head Down")
            time.sleep(.2)
            robot.headDown()
        elif "left" in command:
            print("A: Head Left")
            time.sleep(.2)
            robot.headLeft()
        elif "right" in command:
            print("D: Head Right")
            time.sleep(.2)
            robot.headRight()

    def stop(self, event):
        print("Space: Kill Switch")
        robot.resetRobot()

    while listening:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source)
            r.dyanmic_energythreshhold = 3000

            try:
                print("listening")
                audio = r.listen(source)
                print("Got audio")
                command = r.recognize_google(audio)
                print(command)
            except sr.UnknownValueError:
                print("Word not recognized")

            if "waist" in command:
                waist(command)
            elif "head" in command:
                head(command)
            elif "robot" in command:
                arrows(command)
            elif "stop" in command:
                stop()
            else:
                print("Command not recognized")

SpeechController()
