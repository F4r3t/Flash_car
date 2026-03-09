import os
import pygame

from settings import MENU_WIDTH, MENU_HEIGHT, FPS, TITLE
from states.state_factory import StateFactory


class Game:
    def __init__(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()

        display_info = pygame.display.Info()
        self.max_width = int(display_info.current_w * 0.70)
        self.max_height = int(display_info.current_h * 0.78)

        initial_width = min(MENU_WIDTH, self.max_width)
        initial_height = min(MENU_HEIGHT, self.max_height)

        self.screen = pygame.display.set_mode((initial_width, initial_height))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = StateFactory.create(self, "menu")

    def resize_window(self, width: int, height: int):
        width = min(width, self.max_width)
        height = min(height, self.max_height)
        self.screen = pygame.display.set_mode((width, height))

    def change_state(self, state_name: str, **kwargs):
        self.state = StateFactory.create(self, state_name, **kwargs)

    def quit(self):
        self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.state.handle_event(event)

            self.state.update()
            self.state.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()