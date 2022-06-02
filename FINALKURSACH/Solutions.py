import GenericMatrixOperations as GMO
import sys
sys.setrecursionlimit(10000)

def isSafe(matrix, row, col):
    coordsLst = GMO.split(matrix)
    for item in coordsLst:
        if not (item[0] == row and item[1] == col):
            if row == item[0]:
                return False
            if row - item[0] == col - item[1]:
                return False
            if row + col == item[0] + item[1]:
                return False
            if col == item[1]:
                return False
    return True


def AStar(SomeMatrix):
    counter = 0
    newMatrix = GMO.createEmpty()
    matrixLst = []
    row = 0
    directionList = GMO.movement(GMO.split(SomeMatrix))
    colList = GMO.getCols(GMO.split(SomeMatrix))
    firstRowCounter = 0
    while firstRowCounter != 7:
        placed = 0
        if directionList[row] == 1:
            for tmpCol in range(colList[row], 8):
                if tmpCol == 7:
                    directionList[row] = -1
                newMatrix[row][tmpCol] = 1
                counter += 1
                if isSafe(newMatrix, row, tmpCol) is True:
                    colList[row] = tmpCol
                    row += 1
                    placed = 1
                    break
                else:
                    newMatrix[row][tmpCol] = 0
        if row != 8:
            for tmpCol in range(colList[row] - 1, -1, -1):
                if placed == 1:
                    break
                newMatrix[row][tmpCol] = 1
                counter += 1
                if isSafe(newMatrix, row, tmpCol) is True:
                    colList[row] = tmpCol
                    placed = 1
                    row += 1
                    break
                else:
                    newMatrix[row][tmpCol] = 0
            if placed != 1:
                if directionList[row - 1] == 1:
                    colList[row - 1] += 1
                else:
                    colList[row - 1] -= 1
                GMO.eraseRow(newMatrix, row)
                colList[row] = 0
                directionList[row] = 1
                GMO.eraseRow(newMatrix, row - 1)
                row -= 1
        if row == 8:
            if GMO.Check(newMatrix) is True and newMatrix not in matrixLst:
                matrixLst.append(GMO.copy(newMatrix))
            GMO.eraseRow(newMatrix, 7)
            if directionList[7] == 1:
                colList[7] += 1
            else:
                colList[7] -= 1
            row -= 1
            if directionList[0] == -1 and colList[0] == 1:
                return matrixLst


def pickClosest(currMatrix, matrices):

    def countDifference(oneMatrix, anotherMatrix):
        sum = 0
        for row in range(0, 8):
            sum += abs(GMO.findCol(oneMatrix, row) - GMO.findCol(anotherMatrix, row))
        return sum

    smallest = countDifference(currMatrix, matrices[0])
    closest = matrices[0]
    for comparedMatrix in matrices:
        if countDifference(currMatrix, comparedMatrix) < smallest:
            smallest = countDifference(currMatrix, comparedMatrix)
            closest = comparedMatrix
    return closest


def AStarSolution(matrix):
    matrix = GMO.placeQueensOnDifferentRows(matrix)
    solvedMatrix = pickClosest(matrix, AStar(matrix))
    return solvedMatrix


def RBFS(newMatrix, colList, direction, row):
    if row >= 8:
        return newMatrix
    else:
        if direction[row] == 1:
            for column in range(colList[row], 8):
                if column == 7:
                    direction[row] = -1
                newMatrix[row][column] = 1
                if isSafe(newMatrix, row, column) is True:
                    colList[row] = column
                    print(row)
                    return RBFS(newMatrix, colList, direction, row + 1)
                else:
                    newMatrix[row][column] = 0
        for column in range(colList[row] - 1, -1, -1):
            newMatrix[row][column] = 1
            if isSafe(newMatrix, row, column):
                colList[row] = column
                print(row)
                return RBFS(newMatrix, colList, direction, row + 1)
            newMatrix[row][column] = 0
        if direction[row-1] == 1:
            colList[row-1] += 1
        else:
            colList[row-1] -= 1
        GMO.eraseRow(newMatrix, row)
        colList[row] = 0
        direction[row] = 1
        GMO.eraseRow(newMatrix, row - 1)
        return RBFS(newMatrix, colList, direction, row - 1)


def RBFS_solution(matrix):
    matrix = GMO.placeQueensOnDifferentRows(matrix)
    matrix = GMO.transpose(matrix)
    colLst = GMO.getCols(matrix)
    directionLst = GMO.movement(colLst)
    newMatrix = GMO.createEmpty()
    matrix = RBFS(newMatrix, colLst, directionLst, 0)
    matrix = GMO.transpose(matrix)
    return matrix