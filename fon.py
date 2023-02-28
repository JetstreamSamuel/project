import pygame


class Fon(pygame.sprite.Sprite):
    def __init__(self, sheet, screen, group, pos):
        super().__init__(group)
        self.screen = screen
        self.image = sheet
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)

    def draw(self):
        self.screen.blit(self.image, (0, 0))
