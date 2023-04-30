import sys
import pygame

from settings import Settings
from frog import Frog
from goal import Goal

class Ribbit:
    def __init__(self):
        self.title = pygame.display.set_caption('Ribbit')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.frog = Frog(self)
        self.goal = Goal(self)

    def run_game(self):
        self.frog.center()
        self.goal.place()
        while self.is_running == True:
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)
            self.frog.blitme()
            self.goal.blit()
            pygame.display.flip()
            self._check_events()
            self._check_goal_reached()
                
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)         
    
    def _check_goal_reached(self):
        collision = self.goal.rect.colliderect(self.frog.rect)
        if collision:
            self.goal.is_empty = False
            self.frog.center()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP and self.frog.rect.top > self.screen.get_rect().top + self.frog.size:
            self.frog.rect.y -= self.frog.size
        if event.key == pygame.K_DOWN and self.frog.rect.bottom < self.screen.get_rect().bottom - self.frog.size:
            self.frog.rect.y += self.frog.size
        if event.key == pygame.K_LEFT and self.frog.rect.left > self.screen.get_rect().left + self.frog.size:
            self.frog.rect.x -= self.frog.size
        if event.key == pygame.K_RIGHT and self.frog.rect.right < self.screen.get_rect().right - self.frog.size:
            self.frog.rect.x += self.frog.size
        if event.key == pygame.K_ESCAPE:
            sys.exit()

if __name__ == '__main__':
    ribbit = Ribbit()
    ribbit.run_game()
