import pygame
from pygame.sprite import Sprite

class Goal(Sprite):

    def __init__(self, ribbit):
        super().__init__()
        self.screen = ribbit.screen
        self.image = pygame.Surface((50, 50))
        
        self.rect = self.image.get_rect()
        self.is_empty = True

    def place(self):
        self.rect.left = 50
        self.rect.top = 50

    def blit(self):
        if self.is_empty:
            self.image.fill('black')
        else:
            self.image.fill('gold')

        self.screen.blit(self.image, self.rect)