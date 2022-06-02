import tkinter as tk
from PIL import ImageTk, Image
import GenericMatrixOperations as GMO
import Solutions



class board:
    def __init__(self, x, y, root):
        self._root = root
        self._x = x
        self._solveRBFSButton = tk.Button(text='RBFS', command=lambda: self.__RBFS_button(450, 52))
        self._solveRBFSButton.place(x=x + 300, y=y + 40)
        self._solveRBFSButton["state"] = "disable"
        self._solveAStarButton = tk.Button(text='A*', command=lambda: self.__AStar_button(800, 52))
        self._solveAStarButton.place(x=x + 300, y=y + 80, width=69)
        self._solveAStarButton["state"] = "disable"
        self._y = y
        self._activatedTiles = []
        self._activityMatrix = []
        for a in range(0, 8):
            self._activityMatrix.append([])
            for b in range(0, 8):
                self._activityMatrix[a].append(0)
        board._boardLetters(30, 30, root)
        self._tileList = []
        for a in range(0, 8):
            self._tileList.append([])
            for b in range(0, 8):
                t = board._tile(a, b, x, y, self)
                self._tileList[a].append(t)
        self.__remainingQueensLabel = tk.Label(text=f'{8 - len(self._activatedTiles)} queens remaining')
        self.__remainingQueensLabel.place(x=self._x + 100, y=self._y + 350)

    def _updateList(self):
        self.__remainingQueensLabel = tk.Label(text=f'{8 - len(self._activatedTiles)} queens remaining')
        self.__remainingQueensLabel.place(x=self._x + 100, y=self._y + 350)

    def __RBFS_button(self, x, y):
        label = tk.Label(text="RBFS solution:")
        label.place(y=y-22, x=x+80)
        matrix = GMO.copy(self._activityMatrix)
        if GMO.Check(matrix) is True:
            matrix = matrix
        else:
            matrix = Solutions.RBFS_solution(matrix)
        for i in range(0, 8):
            print(matrix[i])
        board._boardLetters(self._x + x - 80, self._y - y + 35, self._root)
        for b in range(0, 8):
            for j in range(0, 8):
                tmp = board._tile(b, j, x, y, self)
                if matrix[b][j] == 1:
                    tmp._createQ(self)
                else:
                    tmp._createNormal(self)
        matrix.clear()

    def __AStar_button(self, x, y):
        label = tk.Label(text='A* solution:')
        label.place(x=x+80, y=y-22)
        matrix = GMO.copy(self._activityMatrix)
        if GMO.Check(matrix) is True:
            matrix = matrix
        else:
            matrix = Solutions.AStarSolution(matrix)
        for i in range(0, 8):
            print(matrix[i])
        board._boardLetters(self._x + x - 80, self._y - y + 35, self._root)
        for b in range(0, 8):
            for j in range(0, 8):
                tmp = board._tile(b, j, x, y, self)
                if matrix[b][j] == 1:
                    tmp._createQ(self)
                else:
                    tmp._createNormal(self)
        matrix.clear()

    class _boardLetters:
        def __init__(self, x, y, root):
            for c in range(1, 9):
                _label = tk.Label(root, text=f'{c}')
                _label.place(x=x, y=y + c * 35.5 - 15)
            for c in range(1, 9):
                _label = tk.Label(root, text=f'{chr(c + 64)}')
                _label.place(x=x + c * 36, y=y + 300)

    class _tile:
        def __init__(self, x, y, move_x, move_y, someBoard):
            self.__x = x
            self.__y = y
            self.__move_x = move_x
            self.__move_y = move_y
            self.__bl = ImageTk.PhotoImage(Image.open("Black.png"))
            self.__wh = ImageTk.PhotoImage(Image.open("White.png"))
            self.__bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.__wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            if x % 2 == 1:
                if y % 2 == 1:
                    self.__color = self.__wh
                else:
                    self.__color = self.__bl
            else:
                if y % 2 == 1:
                    self.__color = self.__bl
                else:
                    self.__color = self.__wh
            self.__button = tk.Button(someBoard._root, image=self.__color, command=lambda: self.__place_queen(someBoard))
            self.__button.place(x=35 * x + move_x, y=35 * y + move_y)

        def __place_queen(self, someBoard):
            someBoard._activityMatrix[self.__x][self.__y] = 1
            self.__button.destroy()
            if self.__color == self.__wh:
                self.__color = self.__wh_q
            else:
                self.__color = self.__bl_q
            self.__button = tk.Button(someBoard._root, image=self.__color, command=lambda: self.__remove_queen(someBoard))
            self.__button.place(x=35 * self.__x + self.__move_x, y=35 * self.__y + self.__move_y)
            someBoard._activatedTiles.append(self)
            someBoard._updateList()
            if len(someBoard._activatedTiles) >= 8:
                for d in range(0, 8):
                    for j in range(0, 8):
                        someBoard._tileList[d][j].__button["state"] = "disable"
                for d in range(len(someBoard._activatedTiles)):
                    someBoard._activatedTiles[d].__button["state"] = "normal"
                someBoard._solveRBFSButton["state"] = "normal"
                someBoard._solveAStarButton["state"] = "normal"

        def _createQ(self, someBoard):
            self.__bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.__wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            self.__button.destroy()
            if self.__color == self.__wh:
                self.__color = self.__wh_q
            else:
                self.__color = self.__bl_q
            self.__button = tk.Button(someBoard._root, image=self.__color, command=lambda: self.__place_queen(someBoard))
            self.__button.place(x=35 * self.__x + self.__move_x, y=35 * self.__y + self.__move_y)
            self.__button["state"] = "disable"

        def _createNormal(self, someBoard):
            self.__bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.__wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            self.__button.destroy()
            self.__button = tk.Button(someBoard._root, image=self.__color, command=lambda: self.__place_queen(someBoard))
            self.__button.place(x=35 * self.__x + self.__move_x, y=35 * self.__y + self.__move_y)
            self.__button["state"] = "disable"

        def __remove_queen(self, someBoard):
            someBoard._activityMatrix[self.__x][self.__y] = 0
            self.__button.destroy()
            if self.__color == self.__bl_q:
                self.__color = self.__bl
            else:
                self.__color = self.__wh
            newButton = tk.Button(someBoard._root, image=self.__color, command=lambda: self.__place_queen(someBoard))
            newButton.place(x=35 * self.__x + self.__move_x, y=35 * self.__y + self.__move_y)
            self.__button = newButton
            someBoard._activatedTiles.remove(self)
            someBoard._updateList()
            if len(someBoard._activatedTiles) < 8:
                for k in range(0, 8):
                    for j in range(0, 8):
                        someBoard._tileList[k][j].__button["state"] = "normal"
                someBoard._solveRBFSButton["state"] = "disable"






