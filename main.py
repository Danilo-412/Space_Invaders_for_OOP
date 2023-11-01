import pygame
import sys
from main_character import MainCharacter


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaxeX by Pushkova")
    maincharacter = MainCharacter(screen)

    flag = True
    while flag:
        '''обработка событий игрока'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    maincharacter.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    maincharacter.move_right = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    maincharacter.move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    maincharacter.move_left = False

        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

