import random
import pygame

from assets import load_font, game_over_music_path
from settings import GAME_OVER_WIDTH, GAME_OVER_HEIGHT, WHITE, GOLD
from states.ui_screen_state import UIScreenState
from utils.ui import draw_text, Button, get_font_sizes
from utils.save_manager import load_best_score, save_best_score


class GameOverState(UIScreenState):
    def __init__(self, game, score=0, code="green", **kwargs):
        super().__init__(game)
        self.game.resize_window(GAME_OVER_WIDTH, GAME_OVER_HEIGHT)

        self.score = score
        self.code = code

        save_best_score(score)
        self.best_score = load_best_score()

        title_size, text_size, _ = get_font_sizes(self.game.screen)
        self.title_font = load_font("pixel.ttf", title_size)
        self.text_font = load_font("pixel.ttf", text_size)

        self.restart_button = Button(0.5, 0.52, 0.28, 0.09, "RESTART", self.text_font)
        self.menu_button = Button(0.5, 0.64, 0.28, 0.09, "MAIN MENU", self.text_font)
        self.quit_button = Button(0.5, 0.76, 0.28, 0.09, "QUIT", self.text_font)

        index = random.randint(1, 2)
        pygame.mixer.music.load(str(game_over_music_path(index)))
        pygame.mixer.music.play(0)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pygame.mixer.music.stop()
                self.game.change_state("game", code=self.code)
            elif event.key == pygame.K_m:
                pygame.mixer.music.stop()
                self.game.change_state("menu")
            elif event.key == pygame.K_ESCAPE:
                self.game.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.restart_button.is_clicked(self.game.screen, event.pos):
                pygame.mixer.music.stop()
                self.game.change_state("game", code=self.code)
            elif self.menu_button.is_clicked(self.game.screen, event.pos):
                pygame.mixer.music.stop()
                self.game.change_state("menu")
            elif self.quit_button.is_clicked(self.game.screen, event.pos):
                self.game.quit()

    def update(self):
        pass

    def draw(self, screen):
        width = screen.get_width()
        height = screen.get_height()

        self.fill_background(screen)
        draw_text(screen, "GAME OVER", self.title_font, WHITE, (width * 0.5, height * 0.16))
        draw_text(screen, f"Score: {self.score}", self.text_font, WHITE, (width * 0.5, height * 0.30))
        draw_text(screen, f"Best: {self.best_score}", self.text_font, GOLD, (width * 0.5, height * 0.38))

        self.restart_button.draw(screen)
        self.menu_button.draw(screen)
        self.quit_button.draw(screen)