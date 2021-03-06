import pygame

from main import window_height, display_surf, WHITE


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, w, h):
        self.x = x
        self.w = w
        self.h = h
        self.y = int(window_height / 2 - self.h / 2)
        # Creates Rectangle for paddle.
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    # Draws the paddle
    def draw(self):
        # Stops paddle moving too low
        if self.rect.bottom > window_height - self.w:
            self.rect.bottom = window_height - self.w
        # Stops paddle moving too high
        elif self.rect.top < self.w:
            self.rect.top = self.w
        # Draws paddle
        pygame.draw.rect(display_surf, WHITE, self.rect)

    # Moves the paddle
    def move(self, pos):
        self.rect.y = pos[1]