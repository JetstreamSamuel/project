import pygame
import sys
from load_image import load_image
from bullet import Bullet


def events_game(hero, screen, bullets):
    """СОБЫТИЯ ИГРЫ"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hero.mright = True
            elif event.key == pygame.K_a:
                hero.mleft = True
            elif event.key == pygame.K_SPACE and hero.cd_shot <= 0:
                bullet = Bullet(load_image("images/bullet.png"), 1, 1, bullets, screen, hero.return_bullet_pos())
                hero.cd_shot = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                hero.mright = False
            elif event.key == pygame.K_a:
                hero.mleft = False


def update_bullets(cont, screen, enemys, scores):
    """РИСУЕМ ПУЛИ"""
    cont.draw(screen)
    cont.update()
    for bullet in cont.copy():
        if bullet.rect.bottom <= 0:
            cont.remove(bullet)
    collisions = pygame.sprite.groupcollide(cont, enemys, True, True)
    if collisions:
        scores.up_one()


def update_hero(cont, screen, enemys):
    """РИСУЕМ ГЕРОЯ"""
    cont.draw(screen)
    cont.update()
    if pygame.sprite.spritecollideany(cont.sprites()[0], enemys):
        lose_game(screen)


def update_enemys(cont, screen):
    """РИСУЕМ ВРАГОВ"""
    cont.draw(screen)
    cont.update()
    if len(cont) == 0:
        win_game(screen)
    else:
        for enemy in cont.sprites():
            if enemy.rect.bottom >= 1275:
                lose_game(screen)


from main import start_game


def lose_game(screen):
    """ЛУЗ"""
    lose_fon = load_image("images/lose_fon.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_game()
        screen.fill((0, 0, 0))
        screen.blit(lose_fon, (0, 300))
        pygame.display.flip()


def win_game(screen):
    """ПОБЕДА"""
    font = pygame.font.Font(None, 100)
    text = font.render("YOU WIN!!", True, (100, 255, 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_game()
        screen.fill((0, 0, 0))
        screen.blit(text, (230, 400))
        pygame.display.flip()
