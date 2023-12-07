import pygame, controls
from hero import Hero
from pygame.sprite import Group
from stats import Stats


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SpaceXXX")

    maincharacter = Hero(screen)
    bullets = Group()
    enemys = Group()

    controls.create_army(screen, enemys)
    bg = pygame.image.load("images/bg.png")

    stats = Stats()
    flag = True
    while flag:
        screen.blit(bg, (0, 0))
        controls.events(screen, maincharacter, bullets)
        maincharacter.output()
        maincharacter.moving(screen)

        controls.update(screen, maincharacter, enemys, bullets)
        controls.update_bullets(screen, enemys, bullets)
        controls.update_enemys(stats, screen, maincharacter, enemys, bullets)
        pygame.display.flip()
        screen.fill(0)


start_game()
