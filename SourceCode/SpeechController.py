import speech_recognition as sr
from TangoRobot import *
import time

listening = True;


def arrows(command):
    if "forward" in command:
        print("Up Arrow")
        time.sleep(.2)
        robot.driveForward()
    elif "back" in command:
        print("Down Arrow")
        time.sleep(.2)
        robot.driveBackward()
    elif "left" in command:
        print("Left Arrow")
        time.sleep(.2)
        robot.turnLeft()
    elif "right" in command:
        print("Right Arrow")
        time.sleep(.2)
        robot.turnRight()


def waist(command):
    if "left" in command:
        print("Z (Left)")
        time.sleep(.2)
        robot.waistLeft()
    elif "right" in command:
        print("C (Right)")
        time.sleep(.2)
        robot.waistRight()


def head(command):
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


def stop():
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
            word = r.recognize_google(audio)
            print(word)
        except sr.UnknownValueError:
            print("Word not recognized")

        if "waist" in word:
            waist(word)
        elif "head" in word:
            head(word)
        elif "robot" in word:
            arrows(word)
        elif "stop" in word:
            stop()
        else:
            print("Command not recognized")
