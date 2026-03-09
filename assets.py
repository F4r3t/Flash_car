from pathlib import Path
import sys
import pygame


def get_base_dir() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


BASE_DIR = get_base_dir()
DATA_DIR = BASE_DIR / "data"


def load_image(*parts, convert_alpha=True):
    path = DATA_DIR / "images"
    for part in parts:
        path /= part

    image = pygame.image.load(path)
    return image.convert_alpha() if convert_alpha else image.convert()


def load_font(name: str, size: int):
    path = DATA_DIR / "fonts" / name
    return pygame.font.Font(path, size)


def gameplay_music_path(index: int):
    return DATA_DIR / "music" / "gameplay" / f"{index}.mp3"


def game_over_music_path(index: int):
    return DATA_DIR / "music" / "game_over" / f"{index}.mp3"


def nyancat_music_path():
    return DATA_DIR / "music" / "nyancat" / "nyan_theme.mp3"