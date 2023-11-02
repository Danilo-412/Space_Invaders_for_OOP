import pygame, controls
from mr import MainCharacter
from pygame.sprite import Group
from stats import Stats

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("SpaxeX by Pushkova")

    maincharacter = MainCharacter(screen)
    bullets = Group()
    # enemy = Enemy(screen)
    enemys = Group()

    controls.create_army(screen, enemys)

    stats = Stats()
    flag = True
    while flag:
        controls.events(screen, maincharacter, bullets)
        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

        controls.update(screen, maincharacter, enemys, bullets)
        controls.update_bullets(screen, enemys,bullets)
        controls.update_enemys(stats, screen, maincharacter, enemys, bullets)

start_game()

