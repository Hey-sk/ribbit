import pygame
from pygame.sprite import Sprite
from settings import Settings

class Log(Sprite):

    def __init__(self, ribbit, y_pos = 250):
        super().__init__()
        self.screen = ribbit.screen
        self.screen_rect = ribbit.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.Surface((100, 50))
        self.image.fill((94, 83, 47))
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.right
        self.rect.y = y_pos
        
        

    def update(self):
        if self.rect.right > 0:
            if self.rect.y == 250:
                self.rect.x -= 1
            else:
                self.rect.x -= 2
        else:
            self.rect.x = self.screen_rect.right
