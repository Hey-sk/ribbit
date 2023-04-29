import sys
import pygame

from settings import Settings
from spaceman import Spaceman

class Runner:
    def __init__(self):
        self.title = pygame.display.set_caption('spaceman runner')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.spaceman = Spaceman(self)

    def run_game(self):
        self.spaceman.center()
        while self.is_running == True:
            
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)
            self.spaceman.blitme()

            pygame.display.flip()
            
            for event in pygame.event.get():
                self._check_events(event)
                
    def _check_events(self, event):
        if event.type == pygame.QUIT:
            sys.exit()



if __name__ == '__main__':
    runner = Runner()
    runner.run_game()
