import tkinter as tk
from PIL import ImageTk, Image
import sys
sys.setrecursionlimit(100000)


class board:
    def __init__(self, x, y, root):
        self.root = root
        self.x = x
        self.solveButton = tk.Button(text='RBFS', command=lambda: self.RBFS_button(600, 52))
        self.solveButton.place(x=x + 360, y=y + 40)
        self.solveButton["state"] = "disable"
        self.y = y
        self.activatedTiles = []
        self.activityMatrix = []
        for a in range(0, 8):
            self.activityMatrix.append([])
            for j in range(0, 8):
                self.activityMatrix[a].append(0)
        board.boardLetters(30, 30, root)
        self.tileList = []
        for a in range(0, 8):
            self.tileList.append([])
            for j in range(0, 8):
                t = board.tile(a, j, x, y, self)
                self.tileList[a].append(t)
        self.remainingQueensLabel = tk.Label(text=f'{8 - len(self.activatedTiles)} queens left')
        self.remainingQueensLabel.place(x=self.x + 100, y=self.y + 350)

    def updateList(self):
        self.remainingQueensLabel = tk.Label(text=f'{8 - len(self.activatedTiles)} queens left')
        self.remainingQueensLabel.place(x=self.x + 100, y=self.y + 350)

    def RBFS_button(self, x, y):
        matrix = copy(self.activityMatrix)
        matrix = RBFS_solution(matrix)
        for i in range(0, 8):
            print(matrix[i])
        matrix = placeQueensOnDifferentRows(matrix)
        board.boardLetters(self.x + x - 80, self.y - y + 35, self.root)
        for b in range(0, 8):
            for j in range(0, 8):
                tmp = board.tile(b, j, x, y, self)
                tmp.button["state"] = "disable"
                if matrix[b][j] == 1:
                    tmp.activate(self)
        matrix.clear()

    class boardLetters:
        def __init__(self, x, y, root):
            for c in range(1, 9):
                __label = tk.Label(root, text=f'{c}')
                __label.place(x=x, y=y + c * 35.5 - 15)
            for c in range(1, 9):
                __label = tk.Label(root, text=f'{chr(c + 64)}')
                __label.place(x=x + c * 36, y=y + 300)

    class tile:
        def __init__(self, x, y, move_x, move_y, someBoard):
            self.x = x
            self.y = y
            self.move_x = move_x
            self.move_y = move_y
            self.__bl = ImageTk.PhotoImage(Image.open("Black.png"))
            self.__wh = ImageTk.PhotoImage(Image.open("White.png"))
            self.__bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.__wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            if x % 2 == 1:
                if y % 2 == 1:
                    self.color = self.__wh
                else:
                    self.color = self.__bl
            else:
                if y % 2 == 1:
                    self.color = self.__bl
                else:
                    self.color = self.__wh
            self.button = tk.Button(someBoard.root, image=self.color, command=lambda: self.place_queen(someBoard))
            self.button.place(x=35 * x + move_x, y=35 * y + move_y)

        def place_queen(self, someBoard):
            someBoard.activityMatrix[self.x][self.y] = 1
            self.button.destroy()
            if self.color == self.__wh:
                self.color = self.__wh_q
            else:
                self.color = self.__bl_q
            self.button = tk.Button(someBoard.root, image=self.color, command=lambda: self.remove_queen(someBoard))
            self.button.place(x=35 * self.x + self.move_x, y=35 * self.y + self.move_y)
            someBoard.activatedTiles.append(self)
            print(someBoard.activatedTiles[len(someBoard.activatedTiles) - 1].x,
                  someBoard.activatedTiles[len(someBoard.activatedTiles) - 1].y)
            someBoard.updateList()
            if len(someBoard.activatedTiles) >= 8:
                for d in range(0, 8):
                    for j in range(0, 8):
                        someBoard.tileList[d][j].button["state"] = "disable"
                for d in range(len(someBoard.activatedTiles)):
                    someBoard.activatedTiles[d].button["state"] = "normal"
                someBoard.solveButton["state"] = "normal"

        def activate(self, someBoard):
            self.__bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.__wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            self.button.destroy()
            if self.color == self.__wh:
                self.color = self.__wh_q
            else:
                self.color = self.__bl_q
            self.button = tk.Button(someBoard.root, image=self.color, command=lambda: self.place_queen(someBoard))
            self.button.place(x=35 * self.x + self.move_x, y=35 * self.y + self.move_y)
            self.button["state"] = "disable"

        def remove_queen(self, someBoard):
            someBoard.activityMatrix[self.x][self.y] = 0
            self.button.destroy()
            if self.color == self.__bl_q:
                self.color = self.__bl
            else:
                self.color = self.__wh
            newButton = tk.Button(someBoard.root, image=self.color, command=lambda: self.place_queen(someBoard))
            newButton.place(x=35 * self.x + self.move_x, y=35 * self.y + self.move_y)
            self.button = newButton
            someBoard.activatedTiles.remove(self)
            someBoard.updateList()
            if len(someBoard.activatedTiles) < 8:
                for k in range(0, 8):
                    for j in range(0, 8):
                        someBoard.tileList[k][j].button["state"] = "normal"
                someBoard.solveButton["state"] = "disable"


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


def transpose(matrix):
    newMatrix = []
    for i in range(0, 8):
        newMatrix.append([0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, 8):
        for j in range(0, 8):
            newMatrix[i][j] = matrix[j][i]
    return newMatrix


def copy(matrix):
    m = []
    for i in range(0, 8):
        m.append([0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, 8):
        for j in range(0, 8):
            m[i][j] = matrix[i][j]
    return m


def eraseRow(board, row):
    for i in range(0, 8):
        board[row][i] = 0
    return board


def getCols(matrix):
    lst = split(matrix)
    newLst = []
    for item in lst:
        newLst.append(item[1])
    return newLst


def movement(lst):
    l = []
    for num in lst:
        if num == 7:
            l.append(-1)
        else: l.append(1)
    return l


def isSafe(matrix, row, col):
    lst = split(matrix)
    for item in lst:
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


def Check(matrix):
    lst = split(matrix)
    for anItem in lst:
        for item in lst:
            if not item != anItem:
                if anItem[0] == item[0]:
                    print(f'{anItem} beats {item} horizontally')
                if anItem[0] - item[0] == anItem[1] - item[1]:
                    print(f'{anItem} beats {item} diagonally(main)')
                if anItem[0] + anItem[1] == item[0] + item[1]:
                    print(f'{anItem} beats {item} diagonally(side)')
                if anItem[1] == item[1]:
                    print(f'{anItem} beats {item} vertically')
    return True


def split(matrix):
    lst = []
    for i in range(0, 8):
        for j in range(0, 8):
            if matrix[i][j] == 1:
                lst.append([i, j])
    return lst


def printMatrix(m):
    for i in range(len(m)):
        print(m[i])


def RBFS(newMatrix, colList, direction, row, recursionCounter):
    print(recursionCounter)
    recursionCounter += 1
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
                    return RBFS(newMatrix, colList, direction, row + 1, recursionCounter)
                else:
                    newMatrix[row][column] = 0
        for column in range(colList[row] - 1, -1, -1):
            newMatrix[row][column] = 1
            if isSafe(newMatrix, row, column):
                colList[row] = column
                print(row)
                return RBFS(newMatrix, colList, direction, row + 1, recursionCounter)
            newMatrix[row][column] = 0
        if direction[row-1] == 1:
            colList[row-1] += 1
        else:
            colList[row-1] -= 1
        eraseRow(newMatrix, row)
        colList[row] = 0
        direction[row] = 1
        eraseRow(newMatrix, row - 1)
        return RBFS(newMatrix, colList, direction, row - 1, recursionCounter)


def RBFS_solution(matrix):
    matrix = transpose(matrix)
    matrix = placeQueensOnDifferentRows(matrix)
    colLst = getCols(matrix)
    directionLst = movement(colLst)
    newMatrix = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    matrix = RBFS(newMatrix, colLst, directionLst, 0, 0)
    return matrix




