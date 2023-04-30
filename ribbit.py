import sys
import pygame

from settings import Settings
from frog import Frog

class Ribbit:
    def __init__(self):
        self.title = pygame.display.set_caption('Ribbit')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.frog = Frog(self)

    def run_game(self):
        self.frog.center()
        while self.is_running == True:
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)
            self.frog.blitme()
            self.frog.update()
            pygame.display.flip()
            self._check_events()
            
            
                
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)           
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.frog.moving_up = True
        if event.key == pygame.K_RIGHT:
            self.frog.moving_right = True
        if event.key == pygame.K_LEFT:
            self.frog.moving_left = True
        if event.key == pygame.K_SPACE:
            self.frog.is_jumping = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()
                
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
              self.frog.moving_up = False
        if event.key == pygame.K_LEFT:
            self.frog.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.frog.moving_right = False


if __name__ == '__main__':
    ribbit = Ribbit()
    ribbit.run_game()