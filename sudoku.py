import pygame
from sudoku_algorithm import valid, solve, find_empty
from board import Board
import time
from pause import pause


class Sudoku:
    def __init__(self, level):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 590))
        self.WHITE, self.BLACK = (255, 255, 255), (0, 0, 0)
        pygame.display.set_caption("Sudoku")
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)
        self.level = level
        pygame.display.set_caption("level" + str(self.level))
        self.board = Board(self.screen, self.level)
        self.selected = -1, -1
        self.key_dict = {}
        self.running = True
        self.STARTTIME = time.time()
        self.wrong = 0

    def game_loop(self):
        elapsed = time.time() - self.STARTTIME
        passed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))

        if self.board.board == self.board.solvedBoard:  # user has solved the board
            for i in range(9):
                for j in range(9):
                    self.board.tiles[i][j].selected = False
                self.running = False
            print("successfully solved.")
            exit()
        self.board.redraw(self.key_dict, self.wrong, passed_time)
        self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # allow clicks only while the board hasn't been solved
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(9):
                    for j in range(9):
                        if self.board.tiles[i][j].clicked(mouse_pos):
                            self.selected = i, j
                            self.board.deselect(
                                self.board.tiles[i][j]
                            )  # deselects every tile except the one currently clicked

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

                if self.board.board[self.selected[1]][
                    self.selected[0]
                ] == 0 and self.selected != (-1, -1):
                    if event.key == pygame.K_1:
                        self.key_dict[self.selected] = 1

                    if event.key == pygame.K_2:
                        self.key_dict[self.selected] = 2

                    if event.key == pygame.K_3:
                        self.key_dict[self.selected] = 3

                    if event.key == pygame.K_4:
                        self.key_dict[self.selected] = 4

                    if event.key == pygame.K_5:
                        self.key_dict[self.selected] = 5

                    if event.key == pygame.K_6:
                        self.key_dict[self.selected] = 6

                    if event.key == pygame.K_7:
                        self.key_dict[self.selected] = 7

                    if event.key == pygame.K_8:
                        self.key_dict[self.selected] = 8

                    if event.key == pygame.K_9:
                        self.key_dict[self.selected] = 9

                    elif (
                        event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE
                    ):  # clears tile out
                        if self.selected in self.key_dict:
                            self.board.tiles[self.selected[1]][
                                self.selected[0]
                            ].value = 0
                            del self.key_dict[self.selected]

                    elif (
                        event.key == pygame.K_RETURN and self.selected in self.key_dict
                    ):
                        if (
                            self.key_dict[self.selected]
                            != self.board.solvedBoard[self.selected[1]][
                                self.selected[0]
                            ]
                        ):  # clear tile when incorrect value is inputted
                            self.wrong += 1
                            self.board.tiles[self.selected[1]][
                                self.selected[0]
                            ].value = 0
                            del self.key_dict[self.selected]
                            break
                        # valid and correct entry into cell
                        self.board.tiles[self.selected[1]][
                            self.selected[0]
                        ].value = self.key_dict[
                            self.selected
                        ]  # assigns current grid value
                        self.board.board[self.selected[1]][
                            self.selected[0]
                        ] = self.key_dict[
                            self.selected
                        ]  # assigns to actual board so that the correct value can't be modified
                        del self.key_dict[self.selected]
