import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen): #Инициализация гг
        super(Enemy, self).__init__()
        self.image = pygame.image.load("images/enemy1.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = 1.5
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def output_enemy(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.2
        self.rect.y = self.y
    