import sys
import pygame

from settings import Settings
from frog import Frog
from goal import Goal
from log import Log
from water import Water

class Ribbit:
    def __init__(self):
        self.title = pygame.display.set_caption('Ribbit')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.is_running = True
        self.frog = Frog(self)
        self.water = Water(self)
        self.goal = Goal(self, 0, 0)
        self.log = Log(self)
        self.all_goals = pygame.sprite.Group()
        self.all_logs = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        

    def run_game(self):
        self.frog.center()
        self._create_goals()

        while self.is_running == True:
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)
            self.water.blit()
            self.frog.blitme()
            self.all_logs.update()
            self.all_logs.draw(self.screen)
            self.all_goals.update()
            self.all_goals.draw(self.screen)
            pygame.display.flip()
            self._create_logs()
            self._check_events()
            self._check_goal_reached()
            self._check_frog_killed()
                
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)             

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
        if event.key == pygame.K_g:
            for goal in self.all_goals.sprites():
                print(goal.rect)
            
    
    def _create_logs(self):
        self.all_logs.add(self.log)

    def _create_goals(self):
        x = 100
        for i in range(5):
            this_goal = Goal(self, x, 50)
            self.all_goals.add(this_goal)
            x += 100
        
    def _check_goal_reached(self):
        for goal in self.all_goals:
            collision = goal.rect.colliderect(self.frog.rect)
            if collision:
                goal.is_empty = False
                self.frog.center()
    
    def _check_frog_killed(self):
        collision = self.frog.rect.colliderect(self.water.rect)
        if collision:
            self._kill_frog()
    
    def _kill_frog(self):
        print('the frog has died')
        self.frog.center()

if __name__ == '__main__':
    ribbit = Ribbit()
    ribbit.run_game()
