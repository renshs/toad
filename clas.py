import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)))
                    pygame.draw.rect(screen, (0, 0, 0),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)), 1)
                else:
                    pygame.draw.rect(screen, (0, 255, 255),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)))
                    pygame.draw.rect(screen, (0, 0, 0),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)), 1)

    def get_cell(self, pos):
        x, y = pos
        x -= self.left
        y -= self.top
        x = x // self.cell_size
        y = y // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return None

    def get_click(self, pos):
        if self.get_cell(pos) is not None:
            x, y = self.get_cell(pos)
            self.bard[y][x] = (self.board[y][x] + 1) % 2

    def next_move(self):
        pass


class Life(Board):
    def __init__(self, board, width, heighth, left, top, cell_szie):
        super.__init__(self, board, width, heighth, left, top, cell_szie)

    def next_move(self):
        temp_board = self.board.deepcopy()
        for y in range(self.height):
            for x in range(self.width):
                s = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (x + i <= self.width or x + i >= 0) and (y + j <= self.height or y + j >= 0):
                            s += self.board[j][i]
                if s == 3:
                    temp_board[y][x] = (self.board[y][x] + 1) % 2

        self.board = temp_board.deepcopy()


size = width, height = 600, 600
screen = pygame.display.set_mode(size)
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
            elif event.button == 3:
                range = not running


    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
