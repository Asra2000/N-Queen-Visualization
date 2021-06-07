import pygame as py
from board import Board

BLACK = (0, 0, 0)
BOARD_COLOR = [(255, 150, 173), (255, 245, 253)]
N = 5

IMG = py.image.load('queen.png')
IMG = py.transform.scale(IMG, (30, 30))

class Env:
    def __init__(self, n):
        self.n = n
        self.height = 50 * n
        self.width = 50 * n
        self.screen = py.display.set_mode((self.width, self.height))
        py.display.set_caption("N-Queen")

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()

    def draw_grid(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                py.draw.rect(self.screen, BOARD_COLOR[(i + j) % 2], py.Rect(50 * i, 50 * j, 50, 50))

    def place_queen(self, pos):
        self.draw()
        for i, j in pos:
            self.screen.blit(IMG, (i*50 + 10, j*50+10))

        py.display.update()


if __name__ == '__main__':
    py.init()
    env = Env(N)
    board = Board(N, env)

    run = True
    board.place_the_queen(0)

