import random
import pygame

from assets import load_image
from settings import OBSTACLE_START_SPEED


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, layout, nyancat_mode: bool = False, speed: float = OBSTACLE_START_SPEED):
        super().__init__()
        self.layout = layout
        self.nyancat_mode = nyancat_mode
        self.speed = speed

        self.normal_images = [
            load_image("obstacles", "large.png"),
            load_image("obstacles", "tree.png"),
        ]
        self.nyancat_image = load_image("obstacles", "sweet.png")

        self.image = self._pick_image()
        self.rect = self.image.get_rect()
        self.reset_position()

    def _pick_image(self):
        raw = self.nyancat_image if self.nyancat_mode else random.choice(self.normal_images)
        return pygame.transform.scale(raw, self.layout.obstacle_size)

    def reset_position(self):
        self.rect.x = random.choice(self.layout.lane_x)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= self.layout.height:
            self.speed += 0.1
            self.image = self._pick_image()
            self.reset_position()
            return True

        return False