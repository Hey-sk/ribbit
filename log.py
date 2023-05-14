import pygame
from pygame.sprite import Sprite
from settings import Settings

class Log(Sprite):

    def __init__(self, speed_modifier = 3, dir = 'fwd'):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.image.load('images/log.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.screen_width
    
        self.speed_modifier = float(speed_modifier)
        self.dir = dir
        
    def update(self):
        if self.dir == 'fwd':
            if self.rect.left < self.settings.screen_width:
                self.rect.x += 1 * self.speed_modifier
            else:
                self.rect.x = -50
        else:
            if self.rect.right > 0:
                self.rect.x -= 1 * self.speed_modifier
            else:
                self.rect.x = self.settings.screen_width