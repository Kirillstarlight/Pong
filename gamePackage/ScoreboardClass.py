import pygame

from main import window_width, display_surf, WHITE


class Scoreboard():
    def __init__(self, score=0, x=window_width - 150, y=25, font_size=20):
        self.score = score
        self.x = x
        self.y = y
        self.font = pygame.font.Font('freesansbold.ttf', font_size)

    # Displays the current score on the screen
    def display(self, score):
        self.score = score
        result_surf = self.font.render('Score = %s' % (self.score), True, WHITE)
        rect = result_surf.get_rect()
        rect.topleft = (self.x, self.y)
        display_surf.blit(result_surf, rect)