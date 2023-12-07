import pygame, sys
from bullet import Bullet
from enemy import Enemy
from hero import Hero
import time


def events(screen, hero, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.move_right = True
            if event.key == pygame.K_LEFT:
                hero.move_left = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, hero)
                bullets.add(new_bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.move_left = False
            if event.key == pygame.K_RIGHT:
                hero.move_right = False


def update(screen, hero, enemys, bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.output()
    enemys.draw(screen)


def update_bullets(screen, enemys, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if len(enemys) == 0:
        bullets.empty()
        create_army(screen, enemys)


def update_enemys(stats, screen, hero, enemys, bullets):
    enemys.update()
    if pygame.sprite.spritecollideany(hero, enemys):
        hero_kill(stats, screen, hero, enemys, bullets)
        enemys_check(stats, screen, hero, enemys, bullets)


def create_army(screen, enemys):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((1000 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((900 - 500 - 2 * enemy_height) / enemy_height)
    for row_num in range(number_enemy_y):
        for enemy_num in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_num
            enemy.y = enemy_height + enemy_height * row_num
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row_num
            enemys.add(enemy)


def hero_kill(stats, screen, hero, enemys, bullets):
    if stats.hero_hp > 0:
        stats.hero_hp -= 1
        enemys.empty()
        bullets.empty()
        create_army(screen, enemys)
        hero.create_hero_again()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def enemys_check(stats, screen, hero, enemys, bullets):
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom > screen_rect.bottom:
            hero_kill(stats, screen, hero, enemys, bullets)
            break