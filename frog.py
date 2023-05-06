import pygame

from settings import Settings


class Frog:

    def __init__(self, ribbit):
        #get screen dimensions
        self.screen = ribbit.screen
        self.screen_rect = self.screen.get_rect()

        #get settings
        self.settings = Settings()
        self.size = self.settings.frog_size
        self.starting_x_pos = (self.settings.screen_width - self.size) / 2
        self.starting_y_pos = self.settings.screen_height - (self.size * 2)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('green')
        
        self.rect = self.image.get_rect()
        self.is_on_log = False
        self.log_speed_modifier = self.settings.log_speed_modifier
        
         
    def update(self):
        if self.is_on_log:
            self.rect.x -= 1


    def center(self):
        self.rect.left = int(self.settings.row_spaces/2) * self.size
        self.rect.bottom = self.screen_rect.bottom - self.size

    def blitme(self):
        self.screen.blit(self.image, self.rect)