#file in
def_lists = []



def command(commandString, lineNumber):
    level = 0
    humanInput = ""
    robotOutputs = []
    for i in range(len(commandString)):
        if commandString[i].isdigit():
            level = commandString[i]
        if commandString[i] == "(":
            i += 1
            while commandString[i] != ")":
                humanInput += commandString[i]
                i += 1
        if commandString[i] == ":" and commandString[i + 1] == "[":
            i += 1
            while commandString[i] != "]":
                i += 1
                robotOut = ""
                while commandString[i].isalpha() or commandString[i] == "\"":
                    if commandString[i] != "\"":
                        robotOut += commandString[i]
                    else:
                        i += 1
                        while commandString[i] != "\"":
                            robotOut += commandString[i]
                            i += 1
                    i += 1
                if robotOut != "":
                    robotOutputs.append(robotOut)
        elif commandString[i] == ":" and (commandString[i + 1].isalpha() or commandString[i + 1] == " "):
            i += 1
            robotOut = ""
            while i < len(commandString) - 1:
                robotOut += commandString[i]
                i += 1
            robotOutputs.append(robotOut)
    print(level, humanInput, robotOutputs)
    return level, humanInput, robotOutputs


def definition(definitionString, lineNumber):
    variable = ""
    variable_names = []
    variableOptions = []
    for i in range(0,len(definitionString)):
        if definitionString[i] == "~":
            i += 1
            while definitionString[i].isalpha():
                variable += definitionString[i]
                i += 1
            variable_names.append(variable)
        if definitionString[i] == ":" and definitionString[i + 1] == "[":
            i += 1
            while definitionString[i] != "]":
                robotOut = ""
                i += 1
                while definitionString[i].isalpha() or definitionString[i] == "\"":
                    if definitionString[i] != "\"":
                        robotOut += definitionString[i]
                    else:
                        i += 1
                        while definitionString[i] != "\"":
                            robotOut += definitionString[i]
                            i += 1
                    i += 1
                if robotOut != "":
                    variableOptions.append(robotOut)
        elif definitionString[i] == ":" and (definitionString[i + 1].isalpha() or definitionString[i + 1] == " "):
            i += 1
            robotOut = ""
            while i < len(definitionString) - 1:
                robotOut += definitionString[i]
                i += 1
            variableOptions.append(robotOut)
        temp = variable_names, variableOptions
        def_lists.append(temp)
        return ("how the fuck did you get here?")

def lineReader(line, lineNumber):
    lineValue = ""
    for token in line:
        if token == "u":
            lineValue = command(line, lineNumber)
            break
        elif token == "~":
            definition(line, lineNumber)
        elif token == "#":
            print("Comment at line ", lineNumber)
    return lineValue


def fileReader():
    lines = []
    lineNumber = 1

    file = open("../DialogRules/testing.txt")
    for line in file:
        print(line)
        lines.append(lineReader(line, lineNumber))

        lineNumber += 1
        print("")
        print("")
    #for row in lines:
        #print(row)
    print(def_lists)
fileReader()
