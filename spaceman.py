import pygame

class Spaceman:

    def __init__(self, runner):
        self.screen = runner.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/spaceman.png').convert_alpha()
        self.rect = self.image.get_rect()   

    def center(self):
        self.rect.midleft = self.screen_rect.midleft
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)