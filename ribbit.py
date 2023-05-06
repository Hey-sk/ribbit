import sys
import pygame

from settings import Settings
from frog import Frog
from goal import Goal
from log import Log
from water import Water
from border import Border

class Ribbit:
    def __init__(self):
        self.title = pygame.display.set_caption('Ribbit')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.is_running = True
        self.frog = Frog(self)
        self.water = Water(self)
        self.goal = Goal(self, 0, 0)
        self.log = Log(self, 250)
        self.border = Border(self, 0, 0)
        self.all_goals = pygame.sprite.Group()
        self.all_logs = pygame.sprite.Group()
        self.all_borders = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        

    def run_game(self):
        self.frog.center()
        self._create_goals()
        while self.is_running == True:
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)
            #render assets
            self.water.blit()
            self._create_logs()
            self._create_borders()
            self.all_goals.draw(self.screen)
            self.frog.blitme()
            #update assets
            self.frog.update()
            self.all_logs.update()
            self.all_goals.update()
            #check for events and conditions
            self._check_events()
            self._check_goal_reached()
            self._check_on_log()
            self._check_frog_killed()
            pygame.display.flip()
                
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)             

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.frog.rect.y -= self.frog.size
        if event.key == pygame.K_DOWN:
            self.frog.rect.y += self.frog.size
        if event.key == pygame.K_LEFT:
            self.frog.rect.x -= self.frog.size
        if event.key == pygame.K_RIGHT:
            self.frog.rect.x += self.frog.size
        if event.key == pygame.K_ESCAPE:
            sys.exit()
    
    def _create_logs(self):
        self.all_logs.add(self.log)
        for log in self.all_logs.sprites():
            if log.rect.x == 400:
                self.all_logs.add(Log(self, 250))
                self.all_logs.add(Log(self, 150))
            if log.rect.x == 200 and log.rect.y % 100 != 0:
                self.all_logs.add(Log(self, 200))
                self.all_logs.add(Log(self, 100))
        self.all_logs.draw(self.screen)

    def _create_borders(self):
        left_border = Border(self, 50, self.settings.screen_height)
        top_border = Border(self, self.settings.screen_width, 100)
        right_border = Border(self, 50, self.settings.screen_height)
        right_border.rect.right = self.settings.screen_width
        self.all_borders.add(left_border)
        self.all_borders.add(top_border)
        self.all_borders.add(right_border)
        self.all_borders.draw(self.screen)

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
    
    def _kill_frog(self):
        self.frog.center()
    
    def _check_frog_killed(self):
        on_water = self.frog.rect.colliderect(self.water.rect)
        if on_water and not self.frog.is_on_log:
            self._kill_frog()
        for border in self.all_borders.sprites():
            touched_border = pygame.sprite.spritecollideany(self.frog, self.all_borders)
            if touched_border:
                self._kill_frog()

    def _check_on_log(self):
        for log in self.all_logs:
            on_a_log = pygame.sprite.spritecollideany(self.frog, self.all_logs)
            self.frog.is_on_log = True if on_a_log else False
    

if __name__ == '__main__':
    ribbit = Ribbit()
    ribbit.run_game()
