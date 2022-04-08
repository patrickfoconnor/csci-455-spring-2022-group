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
    if humanInput == "exit": # exits program
        sys.exit()
    return humanInput

# Return the human data previously recorded
def getHumanData(varName, dict):
    if varName in dict.keys():
        humanData = dict.get(varName)
    else:
        humanData = "I Dont Know"
    return humanData


def typeBack(out, dict, varName):
    # Thinking that checking here for the $ sign
    if isinstance(out, list) and bool(out): # if response is list
        output = random.choice(out)
        if "$" in output:
            humanData = getHumanData(varName, dict)
            if humanData is None:
                print(output.replace(varName, "I don't know"))
            elif humanData is not "":
                print(output.replace(varName, humanData))
        else:
            print(output)
    else:
        if varName is not "":
            humanData = getHumanData(varName, dict)
            if humanData is not "":
                print(humanData)
            else:
                print("I don't know")
        else:
            print(out) # if response is string


def checkForVariables(humanInput, humanRes):
    #if "_" in humanRes:
    grabbingVarName = True
    parsedHumanVar = ""
    varIndex = humanRes.find("_")
    if (humanInput[:varIndex] == humanRes[:varIndex]):
        while grabbingVarName:
            if (varIndex < len(humanInput) and humanInput[varIndex].isalpha()):
                parsedHumanVar += humanInput[varIndex]
                varIndex += 1
            else:
                grabbingVarName = False
        return parsedHumanVar


def getVarName(out):
    output = random.choice(out)
    if "$" in output:
        varName = "$"
        varFound = False
        for i in range (0, len(output)):
            if output[i] == "$":
                varFound = True
            if varFound and output[i].isalpha():
                varName += output[i]
        return varName


def main():
    level = 0
    i = 0
    humanDataDict = {}
    humanInput = typing()
    breaking = False
    varName = ""
    while not breaking: # this while loop checks the top level of options
        humanRes = rulesList[i][1] # what the robot is looking to respond to
        if int(rulesList[i][0]) > 0: # if the level is higher that first level it skips the loop.
            pass
        elif isinstance(humanRes, str): # if human option is a str
            if "_" in humanRes:
                humanData = checkForVariables(humanInput, humanRes)
                if humanData != "":
                    varName = getVarName(rulesList[i][2])
                    humanDataDict[varName] = humanData
                    typeBack(rulesList[i][2], humanDataDict, varName)
                    breaking = True
            elif humanInput == humanRes:
                # Thinking right here is a good place to have insertion of var in dict
                typeBack(rulesList[i][2], humanDataDict, varName)
                breaking = True
        elif isinstance(humanRes, list): # if human option is a list
            for word in humanRes:
                if "_" in humanRes:
                    humanData = checkForVariables(humanInput, humanRes)
                    if humanData != "":
                        varName = getVarName(rulesList[i][2])
                        humanDataDict[varName] = humanData
                        typeBack(rulesList[i][2], humanDataDict, varName)
                        breaking = True
                elif humanInput == word:
                    # Thinking right here is a good place to have insertion of var in dict
                    typeBack(rulesList[i][2], humanDataDict, varName)
                    breaking = True
        i += 1
    level = 1
    nextList = []
    currentLevel = 1 # currentLevel is the level we want to look at
    while len(rulesList) > 0: # while there are still rules (might not be needed)
        currentList = nextList
        while currentLevel <= level and i < len(rulesList):
            if int(rulesList[i][0]) == level: # places rules into the current list if it is the level we are looking at
                currentList.append(rulesList[i])
            else:
                if int(rulesList[i][0]) < currentLevel: # if nothing left on lower levels, leaves and goes to responses
                    currentLevel += 1
                else:
                    nextList.append(rulesList[i]) # places rules into the list to look at next

            i += 1
        humanInput = typing()
        for j in range(0, len(currentList)):
            if humanInput == currentList[j][1]: # checks to see if input is in list
                typeBack(currentList[j][2], humanDataDict, varName) # responds
                if len(nextList) > 0: # if there is nothing in the list go to the next one
                    level += 1
                    break
        i += 1

main()