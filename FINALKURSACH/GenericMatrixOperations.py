import random


def transpose(matrix):
    newMatrix = []
    for i in range(0, 8):
        newMatrix.append([0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, 8):
        for j in range(0, 8):
            newMatrix[i][j] = matrix[j][i]
    return newMatrix


def checkRow(lst):
    for i in range(0, 8):
        if lst[i] == 1:
            return False
    return True


def getListOfFreeRows(matrix):
    lst = []
    for i in range(0, 8):
        if checkRow(matrix[i]) is True:
            lst.append(i)
    return lst


def createEmpty():
    newMatrix = []
    for row in range(0, 8):
        newMatrix.append([])
    for rowID in range(0, 8):
        for colID in range(0, 8):
            newMatrix[rowID].append(0)
    return newMatrix


def eraseRow(matrix, row):
    for i in range(0, 8):
        matrix[row][i] = 0



def createRandom():
    RandomMatrix = []
    for i in range(0, 8):
        RandomMatrix.append([0, 0, 0, 0, 0, 0, 0, 0])
    counter = 0
    while counter != 8:
        RandomX = random.randint(0, 7)
        RandomY = random.randint(0, 7)
        if RandomMatrix[RandomX][RandomY] != 1:
            RandomMatrix[RandomX][RandomY] = 1
            counter += 1
    return RandomMatrix


def split(matrix):
    lst = []
    for i in range(0, 8):
        for j in range(0, 8):
            if matrix[i][j] == 1:
                lst.append([i, j])
    return lst


def placeQueensOnDifferentRows(matrix):
    freeLst = getListOfFreeRows(matrix)
    if len(freeLst) == 0:
        return matrix
    else:
        print(freeLst)
        counter = 0
        lstCounter = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if counter == 0 and matrix[i][j] == 1:
                    counter = 1
                elif counter > 0 and matrix[i][j] == 1:
                    matrix[i][j] = 0
                    matrix[freeLst[lstCounter]][j] = 1
                    lstCounter += 1
                if j == 7:
                    counter = 0
        return matrix


def Check(matrix):
    lst = split(matrix)
    for anItem in lst:
        for item in lst:
            if item != anItem:
                if anItem[0] == item[0]:
                    return False
                if anItem[0] - item[0] == anItem[1] - item[1]:
                    return False
                if anItem[0] + anItem[1] == item[0] + item[1]:
                    return False
                if anItem[1] == item[1]:
                    return False
    return True


def movement(lst):
    directionList = []
    for num in lst:
        if num == 7:
            directionList.append(-1)
        else:
            directionList.append(1)
    return directionList


def findCol(matrix, row):
    for i in range(0, 8):
        if matrix[row][i] == 1:
            return i


def getCols(lst):
    newLst = []
    for item in lst:
        newLst.append(item[1])
    return newLst


def copy(matrix):
    m = []
    for i in range(0, 8):
        m.append([0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, 8):
        for j in range(0, 8):
            m[i][j] = matrix[i][j]
    return m












