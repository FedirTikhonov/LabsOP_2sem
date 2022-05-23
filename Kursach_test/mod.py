import tkinter as tk
from PIL import ImageTk, Image


class board:
    def __init__(self, x, y, root):
        self.root = root
        self.x = x
        self.solveButton = tk.Button(text='solve', command=lambda: self.copyEverything(600, 52))
        self.solveButton.place(x=x+360, y=y+40)
        self.solveButton["state"] = "disable"
        self.y = y
        self.tileList = matrix(8, 8)
        self.activatedTiles = []
        self.activityMatrix = matrix(8, 8)
        numsAndChars = board.boardLetters(30, 30, root)
        for i in range(0, 8):
            for j in range(0, 8):
                t = board.tile(i, j, x, y, self)
                self.tileList.change(i, j, t)
        self.label = tk.Label(text=f'{8 - len(self.activatedTiles)} queens left')
        self.label.place(x=self.x + 100, y=self.y + 350)

    def updateList(self):
        self.label = tk.Label(text=f'{8 - len(self.activatedTiles)} queens left')
        self.label.place(x=self.x + 100, y=self.y + 350)

    def copyEverything(self, x, y):
        board.boardLetters(self.x + x - 80, self.y - y + 35, self.root)
        for i in range(0, 8):
            for j in range(0, 8):
                tmp = board.tile(i, j, x, y, self)
                tmp.button["state"] = "disable"
                if self.activityMatrix.get(i, j) == 1:
                    tmp.activate(self)

    class boardLetters:
        def __init__(self, x, y, root):
            for i in range(1, 9):
                label = tk.Label(root, text=f'{i}')
                label.place(x=x, y=y+i*35.5 - 15)
            for i in range(1, 9):
                label = tk.Label(root, text=f'{chr(i + 64)}')
                label.place(x=x+i*36, y=y + 300)

    class tile:
        def __init__(self, x, y, move_x, move_y, someBoard):
            self.x = x
            self.y = y
            self.move_x = move_x
            self.move_y = move_y
            self.bl = ImageTk.PhotoImage(Image.open("Black.png"))
            self.wh = ImageTk.PhotoImage(Image.open("White.png"))
            self.bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            if x % 2 == 1:
                if y % 2 == 1:
                    self.color = self.wh
                else:
                    self.color = self.bl
            else:
                if y % 2 == 1:
                    self.color = self.bl
                else:
                    self.color = self.wh
            self.button = tk.Button(someBoard.root, image=self.color, command=lambda: self.place_queen(someBoard))
            self.button.place(x=35 * x + move_x, y=35 * y + move_y)

        def place_queen(self, someBoard):
            someBoard.activityMatrix.change(self.x, self.y, 1)
            print(self.x+1, self.y+1)
            self.button.destroy()
            if self.color == self.wh:
                self.color = self.wh_q
            else:
                self.color = self.bl_q
            self.button = tk.Button(someBoard.root, image=self.color, command=lambda: self.remove_queen(someBoard))
            self.button.place(x=35 * self.x + self.move_x, y=35 * self.y + self.move_y)
            someBoard.activatedTiles.append(self)
            someBoard.updateList()
            if len(someBoard.activatedTiles) >= 8:
                for i in range(0, 8):
                    for j in range(0, 8):
                        someBoard.tileList.get(i, j).button["state"] = "disable"
                for i in range(len(someBoard.activatedTiles)):
                    someBoard.activatedTiles[i].button["state"] = "normal"
                someBoard.solveButton["state"] = "normal"

        def activate(self, someBoard):
            self.bl_q = ImageTk.PhotoImage(Image.open("BlackWithQ.png"))
            self.wh_q = ImageTk.PhotoImage(Image.open("WhiteWithQ.png"))
            self.button.destroy()
            if self.color == self.wh:
                self.color = self.wh_q
            else:
                self.color = self.bl_q
            self.button = tk.Button(someBoard.root, image=self.color, command=lambda: self.place_queen(someBoard))
            self.button.place(x=35 * self.x + self.move_x, y=35 * self.y + self.move_y)
            self.button["state"] = "disable"

        def remove_queen(self, someBoard):
            someBoard.activityMatrix.change(self.x, self.y, 0)
            self.button.destroy()
            if self.color == self.bl_q:
                self.color = self.bl
            else:
                self.color = self.wh
            newButton = tk.Button(someBoard.root, image=self.color, command=lambda: self.place_queen(someBoard))
            newButton.place(x=35 * self.x + self.move_x, y=35 * self.y + self.move_y)
            self.button = newButton
            someBoard.activatedTiles.remove(self)
            someBoard.updateList()
            if len(someBoard.activatedTiles) < 8:
                for i in range(0, 8):
                    for j in range(0, 8):
                        someBoard.tileList.get(i, j).button["state"] = "normal"
                someBoard.solveButton["state"] = "disable"


class matrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.matrix = []

        for i in range(0, x):
            self.matrix.append([])

        for i in range(0, x):
            for j in range(0, y):
                self.matrix[i].append(0)

    def appToCol(self, x, val):
        self.matrix[x].append(val)

    def appNewList(self, lst):
        self.matrix.append(lst)
        self.x += 1

    def change(self, x, y, value):
        self.matrix[x][y] = value

    def fill(self, value):
        for i in range(self.x):
            for j in range(self.y):
                self.matrix[i][j] = value

    def print(self):
        for i in range(0, len(self.matrix)):
            print('|', end='')
            for j in range(0, len(self.matrix[i]) - 1):
                print(self.matrix[i][j], end=', ')
            print(f'{self.matrix[i][len(self.matrix[i]) - 1]}|')
        print('\n')

    def get(self, x, y):
        return self.matrix[x][y]

