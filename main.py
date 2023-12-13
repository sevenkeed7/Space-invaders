from email.mime import image
import pygame, controls
from pygame.sprite import Group

from hero import Hero

from stats import Stats
def start_game(): #Основные функции для игры
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("SpaceX")
    image = pygame.image.load("images/back1.jpeg")
    image = pygame.transform.scale(image, (800, 800))
    
 

    hero = Hero(screen)
    bullets = Group()
    enemies = Group()
    stats = Stats()
    controls.create_army(screen, enemies)

    flag = True
    while flag:
        
        controls.events(screen, hero, bullets)
        controls.update(screen, hero, bullets, enemies)
        controls.moving_bullets(screen, bullets, enemies) 
        controls.update_enemy(stats, hero, screen, enemies, bullets)
        
start_game()
