import pygame
from pygame.sprite import Sprite
from settings import Settings

class Log(Sprite):

    def __init__(self, ribbit, speed_modifier = 1):
        super().__init__()
        self.screen = ribbit.screen
        self.screen_rect = ribbit.screen.get_rect()
        self.settings = Settings()
        self.image = pygame.image.load('images/log.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.right
        self.rect.y = 250
        self.speed_modifier = speed_modifier
        
    def update(self):
        if self.rect.right > 0:
            self.rect.x -= 1 * self.speed_modifier
        else:
            self.rect.x = self.screen_rect.right