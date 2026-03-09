import pygame

from settings import DARK_GRAY, LIGHT_GRAY, WHITE


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def get_font_sizes(screen):
    height = screen.get_height()

    title_size = clamp(int(height * 0.07), 28, 56)
    text_size = clamp(int(height * 0.038), 16, 30)
    small_size = clamp(int(height * 0.028), 14, 24)

    return title_size, text_size, small_size


def draw_text(screen, text, font, color, center):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=center)
    screen.blit(rendered, rect)
    return rect


class Button:
    def __init__(self, rel_x, rel_y, rel_w, rel_h, text, font):
        """
        rel_x, rel_y, rel_w, rel_h — относительные значения от 0 до 1
        """
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_w = rel_w
        self.rel_h = rel_h
        self.text = text
        self.font = font

    def get_rect(self, screen):
        width = screen.get_width()
        height = screen.get_height()

        w = int(width * self.rel_w)
        h = int(height * self.rel_h)
        x = int(width * self.rel_x - w / 2)
        y = int(height * self.rel_y - h / 2)

        return pygame.Rect(x, y, w, h)

    def draw(self, screen):
        rect = self.get_rect(screen)
        mouse_pos = pygame.mouse.get_pos()
        hovered = rect.collidepoint(mouse_pos)

        bg = LIGHT_GRAY if hovered else DARK_GRAY
        pygame.draw.rect(screen, bg, rect, border_radius=12)
        pygame.draw.rect(screen, WHITE, rect, width=2, border_radius=12)

        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, screen, pos):
        return self.get_rect(screen).collidepoint(pos)