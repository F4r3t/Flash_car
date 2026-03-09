import random
import pygame

from assets import load_font, gameplay_music_path, nyancat_music_path
from settings import WIDTH, HEIGHT, WHITE, BLACK
from sprites.car import Car
from sprites.obstacle import Obstacle
from sprites.road import Road
from states.base_state import BaseState
from utils.layout import build_game_layout


class GameState(BaseState):
    def __init__(self, game, code="green", **kwargs):
        super().__init__(game)
        self.game.resize_window(WIDTH, HEIGHT)

        current_width = self.game.screen.get_width()
        current_height = self.game.screen.get_height()
        self.layout = build_game_layout(current_width, current_height)

        self.code = code
        self.nyancat_mode = code == "nyancat"

        self.all_sprites = pygame.sprite.Group()
        self.road_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()

        self.car = Car(code, self.layout)
        self.obstacle = Obstacle(self.layout, nyancat_mode=self.nyancat_mode)

        for x, y, segment_height in self.layout.road_segments:
            road = Road(self.layout, x, y, segment_height)
            self.all_sprites.add(road)
            self.road_group.add(road)

        self.all_sprites.add(self.car)
        self.all_sprites.add(self.obstacle)
        self.obstacle_group.add(self.obstacle)

        font_size = max(24, min(50, int(self.layout.height * 0.055)))
        self.font = load_font("pixel.ttf", font_size)
        self.score = 0

        self._start_music()

    def _start_music(self):
        if self.nyancat_mode:
            pygame.mixer.music.load(str(nyancat_music_path()))
        else:
            index = random.randint(1, 24)
            pygame.mixer.music.load(str(gameplay_music_path(index)))
        pygame.mixer.music.play(-1)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.car.move_left()
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.car.move_right()
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                self.game.change_state("game_over", score=self.score, code=self.code)

    def update(self):
        self.road_group.update()

        passed = self.obstacle.update()
        if passed:
            self.score += 1

        if pygame.sprite.spritecollideany(self.car, self.obstacle_group):
            pygame.mixer.music.stop()
            self.game.change_state("game_over", score=self.score, code=self.code)

    def draw(self, screen):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)

        score_surface = self.font.render(str(self.score), True, WHITE)
        score_rect = score_surface.get_rect(center=(self.layout.width // 2, self.layout.score_y))
        screen.blit(score_surface, score_rect)