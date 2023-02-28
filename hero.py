import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, group, screen):
        super().__init__(group)

        self.cd_shot = 1

        self.speed = 3
        self.screen = screen

        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0

        self.image = self.frames[self.cur_frame]

        self.rect = self.rect.move(384, 880)

        self.mright = False
        self.mleft = False
        self.alive = True

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def return_bullet_pos(self):
        return self.rect.centerx - 20, self.rect.top - 72

    def update(self):
        if self.cd_shot > 0:
            self.cd_shot -= 0.030
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.mright and self.rect.right <= self.screen.get_size()[0] - self.speed:
            self.rect.x += self.speed
        if self.mleft and self.rect.left >= self.speed:
            self.rect.x -= self.speed
