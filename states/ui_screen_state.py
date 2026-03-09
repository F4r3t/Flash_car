from states.base_state import BaseState


class UIScreenState(BaseState):
    BG_COLOR = (60, 60, 60)

    def fill_background(self, screen):
        screen.fill(self.BG_COLOR)