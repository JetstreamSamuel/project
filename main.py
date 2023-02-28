import sys
import pygame

from score import Score
from fon import Fon
from hero import Hero
from enemy import Enemy
from load_image import load_image
from controls import events_game, update_bullets, update_hero, update_enemys

pygame.init()
screen = pygame.display.set_mode((768, 1024))
pygame.display.set_caption("Космические защитники")

clock = pygame.time.Clock()

enemys = pygame.sprite.Group()
group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
fons = pygame.sprite.Group()

FPS = 60


def create_army():
    """СОЗДАЁМ АРМИЮ ЗЛОДЕЕВ"""
    enemy = Enemy(load_image("images/enemy.png"), 1, 1, enemys, screen, (0, 0))
    enemy_width = enemy.rect.width
    enemy_height = enemy.rect.height
    col_enemy_x = int((768 - enemy_width) / enemy_width)
    col_enemy_y = int((700 - enemy_height) / enemy_height)
    enemys.remove(enemys.sprites()[0])
    for row_numb in range(col_enemy_y - 8):
        for enemy_numb in range(col_enemy_x - 6):
            enemy = Enemy(load_image("images/enemy.png"), 1, 1, enemys, screen,
                          (enemy_width + enemy_width * enemy_numb + 40 * enemy_numb,
                           enemy_height + enemy_height * row_numb))


def start_game():
    """ЗАСТАВКА"""
    fon = Fon(load_image("images/fon.png"), screen, fons, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_game()
        fon.draw()
        pygame.display.flip()


def main_game():
    """НАЧАЛО ОСНОВНОГО ГЕЙМЛЕЯ"""
    hero = Hero(load_image("images/hero.png"), 3, 1, group, screen)
    create_army()
    bg_color = (0, 0, 0)
    scores = Score(screen)
    while True:
        events_game(hero, screen, bullets)
        screen.fill(bg_color)
        scores.draw_score()
        update_hero(group, screen, enemys)
        update_bullets(bullets, screen, enemys, scores)
        update_enemys(enemys, screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    start_game()
