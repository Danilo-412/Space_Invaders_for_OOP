import pygame


class Superhero():
    def __init__(self, screen):
        '''основные характеристики'''
        self.screen = screen
        self.image = pygame.image.load("images/pixil-frame-0.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        '''отрисовка героя на экране'''
        self.screen.blit(self.image, self.rect)

    def moving(self, screen):
        '''движение героя по оси Х'''
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= 1
        '''обновление экрана после движения для избавления от растягивая изображения'''
        screen.fill(0)

    def create_maincharacter_again(self):
        self.center = self.screen_rect.centerx0