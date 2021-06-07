import time
import pygame as py


class Board:

    def __init__(self, n, env):
        self.board = []
        self.n = n
        self.queen_pos = []
        self.create_board()
        self.env = env

    def check_board(self, i, j):
        if self.board[i][j] == 1:
            return False

        # in the same col and row
        for k in range(0, self.n):
            if self.board[i][k] == 1:
                return False
            if self.board[k][j] == 1:
                return False

        # check for diagonals
        m = i - 1
        n = j - 1
        while m >= 0 and n >= 0:
            if self.board[m][n] == 1:
                return False
            m -= 1
            n -= 1

        m = i + 1
        n = j + 1

        while m < self.n and n < self.n:
            if self.board[m][n] == 1:
                return False
            m += 1
            n += 1

        m = i + 1
        n = j - 1

        while m < self.n and n >= 0:
            if self.board[m][n] == 1:
                return False
            m += 1
            n -= 1

        m = i - 1
        n = j + 1

        while n < self.n and m >= 0:
            if self.board[m][n] == 1:
                return False
            m -= 1
            n += 1

        return True

    def display(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.board[i][j], end="  ")
            print("\n")

    def create_board(self):
        for i in range(0, self.n):
            self.board.insert(i, [0] * self.n)

    def place_the_queen(self, j):
        if j == self.n:
            run = True
            while run:
                for event in py.event.get():
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_SPACE:
                            exit()

        else:
            for i in range(0, self.n):
                if self.check_board(j, i):
                    self.board[j][i] = 1
                    self.queen_pos.append([i, j])
                    self.env.place_queen(self.queen_pos)
                    time.sleep(1)
                    for event in py.event.get():
                        if event.type == py.QUIT:
                            exit()
                    self.place_the_queen(j + 1)
                    self.queen_pos.pop()
                    self.board[j][i] = 0
