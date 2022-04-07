#from TangoRobot import *
import time
import dialogEngine
import random
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
    return humanInput


def typeBack(out):
    if isinstance(out, list):
        print(random.choice(out))
    else:
        print(out)





def main():
    level = 0
    i = 0
    if rulesList[0][0] == level:
        humanRes = rulesList[0][1]
        humanInput = typing()
        if isinstance(humanRes, str):
            if humanInput == humanRes:
                typeBack(rulesList[0][2])

        elif isinstance(humanRes, list):
            for word in humanRes:
                if humanInput == word:
                    typeBack(rulesList[0][2])
        level += 1
        i += 1
        x = i
        currentList = []
        while int(rulesList[i][0]) >= level:
            if int(rulesList[x][0]) == level:
                currentList.append(rulesList[x])
            i += 1
            x += 1
        humanInput = typing()
        for j in range(0, len(currentList)):
            if humanInput == currentList[j][1]:
                typeBack(currentList[j][2])

main()