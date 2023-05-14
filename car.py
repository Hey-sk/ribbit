import pygame
from settings import Settings
from pygame.sprite import Sprite

class Car(Sprite):

    def __init__(self, ribbit, x_pos, y_pos, speed, fwd):
        super().__init__()
        self.screen = ribbit.screen
        self.settings = Settings()
        self.back_image = pygame.image.load('images/car.png').convert_alpha()
        self.fwd_image = pygame.transform.flip(self.back_image, True, False)
        self.image = self.fwd_image if fwd == True else self.back_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.topleft = (x_pos, y_pos)
        self.speed = float(speed)
        self.fwd = fwd
    
    def update(self):
        movement_direction = 1 if self.fwd == True else -1
        if self.rect.left > self.settings.screen_width:
            self.rect.x = 0
        if self.rect.right < 0:
            self.rect.x = self.settings.screen_width
        self.rect.x += self.speed * movement_direction

    def blit(self):
        self.screen.blit(self.image, self.rect)