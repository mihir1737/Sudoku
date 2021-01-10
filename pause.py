from sudoku_algorithm import valid, solve, find_empty
from board import Board
from tile import Tile
from copy import deepcopy
from sys import exit
import pygame
import time

def left():
        start_ticks=pygame.time.get_ticks() #starter tick
        quit=True
        while quit:
                screen = pygame.display.set_mode((540, 590))
                screen.fill((0, 0, 0))
                font = pygame.font.SysFont('Bahnschrift', 15)
                text = font.render("Thank You",True, (255,255,255))
                screen.blit(text, (230, 245))
                text = font.render("It's benificial for playing",True, (255,255,255))
                screen.blit(text, (160, 270))
                pygame.display.update()
                seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
                if seconds>5: # if more than 10 seconds close the game
                        break


def pause():

    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                left()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused=False
                elif event.key == pygame.K_q:
                    left()
                    pygame.quit()
                    quit()
        screen = pygame.display.set_mode((540, 590))
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Bahnschrift', 15)
        text = font.render("paused",True, (255,255,255))
        screen.blit(text, (230, 245))
        text = font.render("press C to continue or Q to Quit",True, (255,255,255))
        screen.blit(text, (160, 270))
        pygame.display.update()
