def sortStrings(StringList):
    for i in range(len(StringList)):
        for j in range(len(StringList) - i - 1):
            if countChars(StringList[j]) < countChars(StringList[j + 1]):
                StringList[j], StringList[j + 1] = StringList[j + 1], StringList[j]
    return StringList


def countChars(line):
    i = 0
    for char in line:
        if char != ' ':
            i += 1
    return i


def fileToList(fileName):
    lineList = []
    with open(fileName, 'r') as file:
        for line in file:
            lineList.append(line)
    return lineList


def pushLinesToFile(fileName):
    with open(fileName, 'a') as file:
        answer = ""
        line = ""
        while answer != "STOP":
            line = input("Enter a line:\n")
            file.write(line + "\n")
            answer = input("If you are done writing, type \"STOP\"\n")
    return None


def listToFile(lineList, newFileName):
    with open(newFileName, 'w') as file:
        for line in lineList:
            newLine = "The length of this line equals to " + str(countChars(line)) + " " + line
            file.write(newLine)
    return None


def askToDelete(sourceFileName, newFileName):
    answer = input("Do you want to save your work?\nType \"DO\" not to.")
    if answer == "DO":
        sourceFile = open(sourceFileName, 'w')
        sourceFile.close()
        newFile = open(newFileName, 'w')
        newFile.close()
        print("New File and Source File have been deleted.\n")
    return None
