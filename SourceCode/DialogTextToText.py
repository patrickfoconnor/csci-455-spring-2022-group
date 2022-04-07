#from TangoRobot import *
import time
import dialogEngine
#import speech_recognition as sr

rulesList = dialogEngine.fileReader()
listening = True;


def listen():
    while self.listening:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source)
            r.dynamic_energythreshhold = 3000
        try:
            print("listening")
            audio = r.listen(source)
            print("Got audio")
            word = r.recognize_google(audio)
            print(word)
            return word
        except sr.UnknownValueError:
            print("Word not recognized")


def typing():
    humanInput = input("Human: ")
    return humanInput


def interpret(self, humanInput):
    pass


def main():
    level = 0
    i = 0
    if rulesList[0][0] == level:
        while rulesList[i][0] < level:
            i += 1

main()