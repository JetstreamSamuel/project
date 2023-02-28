import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, group, screen, pos):
        super().__init__(group)

        self.speed = 0.3

        self.screen = screen

        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0

        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(pos)

        self.y = self.rect.y
        self.x = self.rect.x

        self.alive = True

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.alive:
            self.y += self.speed
        self.rect.y = self.y
