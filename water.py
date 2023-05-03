import pygame

from settings import Settings
class Water:

    def __init__(self, ribbit):
        self.screen = ribbit.screen
        self.settings = Settings()
        self.image = pygame.Surface((self.settings.screen_width, 200))
        self.image.fill('navy')
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 100)

    def blit(self):
        self.screen.blit(self.image, self.rect)