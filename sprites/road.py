import pygame

from settings import ROAD_SPEED, WHITE


class Road(pygame.sprite.Sprite):
    def __init__(self, layout, x, y, segment_height, speed=ROAD_SPEED):
        super().__init__()
        self.layout = layout
        self.speed = speed

        line_width = max(10, int(self.layout.width * 0.02))
        self.image = pygame.Surface((line_width, segment_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.y >= self.layout.height:
            self.rect.y = -self.rect.height
        else:
            self.rect.y += self.speed