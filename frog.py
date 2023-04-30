import pygame

from settings import Settings


class Frog:

    def __init__(self, ribbit):
        self.screen = ribbit.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = Settings()

        self.movement_speed = 10
        self.size = self.settings.frog_size

        self.starting_x_pos = (self.settings.screen_width - self.size) / 2
        self.starting_y_pos = self.settings.screen_height - (self.size * 2)
        self.rect = pygame.Rect( self.starting_x_pos, self.starting_y_pos, 50, 50)

              

    def center(self):
        self.rect.left = int(self.settings.row_spaces/2) * self.size
        self.rect.bottom = self.screen_rect.bottom - self.size

    def blitme(self):
        pygame.draw.rect(self.screen, 'green', self.rect)