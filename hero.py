import pygame

class Hero():
    def __init__(self, screen): #Инициализация гг
        self.image = pygame.image.load("images/hero1.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = 1
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

    def output_hero(self):
        self.screen.blit(self.image, self.rect)

    def create_hero_again(self):
        self.center = self.screen_rect.centerx