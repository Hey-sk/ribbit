import pygame
from pygame.sprite import Sprite

class Border(Sprite):
    def __init__(self, ribbit, len, wid):
        super().__init__()
        self.screen = ribbit.screen
        self.image = pygame.Surface((len, wid))
        self.image.fill((30, 30, 30))
        self.rect = self.image.get_rect()