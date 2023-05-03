import pygame
from pygame.sprite import Sprite

class Goal(Sprite):

    def __init__(self, ribbit, x, y):
        super().__init__()
        self.screen = ribbit.screen
        self.image = pygame.Surface((50, 50))
        
        self.rect = self.image.get_rect()
        self.is_empty = True
        self.rect.topleft = (x, y)

    def update(self):
        if self.is_empty:
            self.image.fill('blue')
        else:
            self.image.fill('gold')