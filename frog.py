import pygame

from settings import Settings

class Frog:

    def __init__(self, ribbit):
        self.screen = ribbit.screen
        self.screen_rect = self.screen.get_rect()

        self.image = [pygame.image.load('images/spaceman.png').convert_alpha()]
        self.rect = self.image[0].get_rect()
        self.settings = Settings()
        
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.is_jumping = False
        self.jump_duration = 15
        self.movement_speed = 1.5

    def center(self):
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.rect.x += 100

    def update(self):
        speed = self.settings.movement_speed
        if self.moving_up:
            self.rocket_boost()
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += speed
        if self.is_jumping:
            self.jump()
            
    def jump(self):
        if self.jump_duration >= -15:
            self.rect.y -= (self.jump_duration * abs(self.jump_duration) * .05)
            self.jump_duration -= 1
        else:
            self.jump_duration = 15
            self.is_jumping = False
    
    def rocket_boost(self):
        self.rect.y -= self.settings.movement_speed

    def blitme(self):
        self.screen.blit(self.image[0], self.rect)