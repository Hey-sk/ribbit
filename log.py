import pygame
from pygame.sprite import Sprite

class Log(Sprite):

    def __init__(self, ribbit):
        super().__init__()
        self.screen = ribbit.screen
        self.screen_rect = ribbit.screen.get_rect()

        self.image = pygame.Surface((100, 50))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.right
        self.rect.y = 100
        

    def update(self):
        if self.rect.right > 0:
            self.rect.x -= 1
        else:
            self.rect.x = self.screen_rect.right
    
    def blit(self):
        self.screen.blit(self.image, self.rect)
