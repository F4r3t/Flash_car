from states.start_menu import StartMenuState
from states.game_state import GameState
from states.game_over_state import GameOverState


STATE_MAP = {
    "menu": StartMenuState,
    "game": GameState,
    "game_over": GameOverState,
}


class StateFactory:
    @staticmethod
    def create(game, state_name: str, **kwargs):
        state_cls = STATE_MAP.get(state_name)
        if state_cls is None:
            raise ValueError(f"Unknown state name: {state_name}")
        return state_cls(game, **kwargs)