import pygame
import sys
import time
from bullet import Bullet
from enemy import Enemy
image = pygame.image.load("images/back1.jpeg")
image = pygame.transform.scale(image, (800, 800))

def events(screen, hero, bullets):
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                new_bullet = Bullet(screen, hero)
                bullets.add(new_bullet)
    if pygame.key.get_pressed()[pygame.K_a]:  
           
        hero.rect.x -= hero.speed

    if pygame.key.get_pressed()[pygame.K_d]:  
           
        hero.rect.x += hero.speed

    if pygame.key.get_pressed()[pygame.K_w]:  
           
        hero.rect.y -= hero.speed

    if pygame.key.get_pressed()[pygame.K_s]:  
           
        hero.rect.y += hero.speed
def update(screen, hero, bullets, enemies):
    screen.blit(image, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.output_hero()
    enemies.draw(screen)
    pygame.display.flip()
    
def moving_bullets(screen, bullets, enemies):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen, enemies)

def update_enemy(stats, hero, screen, enemies, bullets):
    enemies.update()
    if pygame.sprite.spritecollideany(hero, enemies):
        hero_kill(stats, hero, screen, enemies, bullets)
        enemies_check(stats, hero, screen, enemies, bullets)

def create_army(screen, enemies):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((800 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    
    for i in range(3):
        for enemy_num in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_num
            enemy.y = enemy_height + enemy_height * i
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemies.add(enemy)

def hero_kill(stats, hero, screen, enemies, bullets):
    if stats.hero_hp > 0:
        stats.hero_hp -= 1
        enemies.empty()
        bullets.empty()
        create_army(screen, enemies)
        hero.create_hero_again()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def enemies_check(stats, hero, screen, enemies, bullets):
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom > screen_rect.bottom:
            hero_kill(stats, hero, screen, enemies, bullets)
            break