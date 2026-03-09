import pygame

from assets import load_image


class Car(pygame.sprite.Sprite):
    IMAGES = {
        "red": "car_red.png",
        "green": "car_green.png",
        "black": "car_black.png",
        "nyancat": "nyancat.png",
    }

    def __init__(self, skin_code: str, layout):
        super().__init__()

        filename = self.IMAGES.get(skin_code, "car_green.png")
        raw = load_image("cars", filename)

        size = layout.nyan_car_size if skin_code == "nyancat" else layout.car_size
        self.image = pygame.transform.scale(raw, size)
        self.rect = self.image.get_rect()

        self.layout = layout
        self.lane_index = 1
        self.rect.x = self.layout.lane_x[self.lane_index]
        self.rect.y = self.layout.height - self.rect.height - 20

    def move_left(self):
        if self.lane_index > 0:
            self.lane_index -= 1
            self.rect.x = self.layout.lane_x[self.lane_index]

    def move_right(self):
        if self.lane_index < len(self.layout.lane_x) - 1:
            self.lane_index += 1
            self.rect.x = self.layout.lane_x[self.lane_index]