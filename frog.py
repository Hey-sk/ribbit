import pygame

from settings import Settings


class Frog:

    def __init__(self, ribbit):
        self.screen = ribbit.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(200, 100, 50, 50)
        self.settings = Settings()
              
        self.movement_speed = 10

    def center(self):
        self.rect.center = self.screen_rect.center

    def update(self):
        speed = self.settings.movement_speed
        if dir == 'up':
            self.rect.y -= speed
        if dir == 'down':
            self.rect.y += speed
        if dir == 'left' and self.rect.left > self.screen_rect.left:
            self.rect.x -= speed
        if dir == 'right' and self.rect.right < self.screen_rect.right:
            self.rect.x += speed

    def blitme(self):
        pygame.draw.rect(self.screen, 'green', self.rect)