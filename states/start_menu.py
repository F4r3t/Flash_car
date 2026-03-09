import pygame

from assets import load_font
from settings import MENU_WIDTH, MENU_HEIGHT, DEFAULT_CODE, CHEAT_CODES, TITLE, WHITE, RED, GOLD
from states.ui_screen_state import UIScreenState
from utils.ui import draw_text, Button, get_font_sizes


class StartMenuState(UIScreenState):
    def __init__(self, game, **kwargs):
        super().__init__(game)
        self.game.resize_window(MENU_WIDTH, MENU_HEIGHT)

        title_size, text_size, _ = get_font_sizes(self.game.screen)
        self.title_font = load_font("pixel.ttf", title_size)
        self.text_font = load_font("pixel.ttf", text_size)

        self.start_button = Button(0.5, 0.68, 0.28, 0.09, "START", self.text_font)
        self.quit_button = Button(0.5, 0.80, 0.28, 0.09, "QUIT", self.text_font)

        self.entered_code = ""
        self.selected_code = DEFAULT_CODE

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode and event.unicode.isalpha():
                self.entered_code += event.unicode.lower()
                max_len = max(len(code) for code in CHEAT_CODES)
                self.entered_code = self.entered_code[-max_len:]

                for cheat in CHEAT_CODES:
                    if self.entered_code.endswith(cheat):
                        self.selected_code = cheat

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.start_button.is_clicked(self.game.screen, event.pos):
                self.game.change_state("game", code=self.selected_code)
            elif self.quit_button.is_clicked(self.game.screen, event.pos):
                self.game.quit()

    def update(self):
        pass

    def draw(self, screen):
        width = screen.get_width()
        height = screen.get_height()

        self.fill_background(screen)
        draw_text(screen, TITLE, self.title_font, RED, (width * 0.5, height * 0.17))
        draw_text(screen, f"Текущий мод: {self.selected_code}", self.text_font, GOLD, (width * 0.5, height * 0.48))

        self.start_button.draw(screen)
        self.quit_button.draw(screen)