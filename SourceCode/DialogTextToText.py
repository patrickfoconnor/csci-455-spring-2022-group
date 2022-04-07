#from TangoRobot import *
import time
import dialogEngine
import random
import sys
#import speech_recognition as sr

rulesList = dialogEngine.fileReader()
listening = True;
r = random.seed


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
    if humanInput == "exit":
        sys.exit()
    return humanInput


def typeBack(out):
    if isinstance(out, list):
        print(random.choice(out))
    else:
        print(out)


def main():
    level = 0
    i = 0
    humanInput = typing()
    breaking = False
    while not breaking:
        humanRes = rulesList[i][1]
        if int(rulesList[i][0]) > 0:
            pass
        elif isinstance(humanRes, str):
            if humanInput == humanRes:
                typeBack(rulesList[i][2])
                breaking = True
        elif isinstance(humanRes, list):
            for word in humanRes:
                if humanInput == word:
                    typeBack(rulesList[i][2])
                    breaking = True
        i += 1
    level = 1
    nextList = []
    currentLevel = 1
    while len(rulesList) > 0:

        currentList = nextList
        while currentLevel <= level:
            if int(rulesList[i][0]) == level:
                currentList.append(rulesList[i])
            else:
                if int(rulesList[i][0]) < currentLevel:
                    currentLevel += 1
                else:
                    nextList.append(rulesList[i])

            i += 1
        humanInput = typing()
        for j in range(0, len(currentList)):
            if humanInput == currentList[j][1]:
                typeBack(currentList[j][2])
                if len(nextList) > 0:
                    level += 1
                    break
        i += 1

main()