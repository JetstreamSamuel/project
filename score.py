import pygame


class Score:
    def __init__(self, screen):
        self.score = 0
        self.screen = screen
        self.font = pygame.font.Font(None, 50)

    def up_one(self):
        self.score += 1

    def draw_score(self):
        text = self.font.render(f"Score: {self.score}", True, pygame.color.Color("white"))
        self.screen.blit(text, (10, 10))
