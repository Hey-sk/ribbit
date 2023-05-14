import sys
import pygame

from settings import Settings
from frog import Frog
from goal import Goal
from log import Log
from water import Water
from border import Border
from car import Car

class Ribbit:
    def __init__(self):
        self.title = pygame.display.set_caption('Ribbit- Frogger Clone')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_size))
        self.is_running = True
        self.frog = Frog(self)
        self.water = Water(self)

        self.all_goals = pygame.sprite.Group()
        self.all_logs = pygame.sprite.Group()
        self.all_borders = pygame.sprite.Group()
        self.all_cars = pygame.sprite.Group()

        self._create_goals()
        self._create_logs()
        self._create_cars()
        
        self.clock = pygame.time.Clock()
        

    def run_game(self):
        self.frog.center()
        while self.is_running == True:
            self.screen.fill(self.settings.BG_COL)       
            
            #render assets
            self.water.blit()
            self.all_logs.draw(self.screen)
            self.all_cars.draw(self.screen)
            self._create_borders()
            self.all_goals.draw(self.screen)
            self.frog.blitme()
            
            #update assets
            self.frog.update()
            self.all_logs.update()
            self.all_goals.update()
            self.all_cars.update()

            #check for events and conditions
            self._check_events()
            self._check_goal_reached()
            self._check_on_log()
            self._check_hazard_collide()
            pygame.display.flip()
            self.clock.tick(60)
                
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
            if self.frog.rect.y < 550:
                self.frog.rect.y += self.frog.size
        if event.key == pygame.K_LEFT:
            self.frog.rect.x -= self.frog.size
        if event.key == pygame.K_RIGHT:
            self.frog.rect.x += self.frog.size
        if event.key == pygame.K_ESCAPE:
            sys.exit()
    
    def _create_log(self, x_pos, y_pos, speed_modifier = 1, dir = 'fwd'):
        new_log = Log(speed_modifier, dir)
        new_log.rect.x = x_pos
        new_log.rect.y = y_pos
        self.all_logs.add(new_log)
    
    def _create_logs(self):
        x_pos = self.settings.screen_width
        y_pos = 50
        log_gap = 200
        speed_modifier = 2.5
        for i in range(4):
            y_pos += 50
            if y_pos % 100:
                dir = 'fwd'
                for i in range(1):
                    self._create_log(x_pos + (log_gap * i), y_pos, (speed_modifier / 2), dir)
            else:
                dir = 'back'
                for i in range(1):
                    self._create_log(x_pos + (log_gap * i), y_pos, speed_modifier, dir)
  
    def _create_car(self, x_pos, y_pos, speed, fwd):
        new_car = Car(self, x_pos, y_pos, speed, fwd)
        self.all_cars.add(new_car)
    
    def _create_cars(self):
        x_pos = 0
        y_pos = 350
        speed = 2
        
        for i in range(2):
            for i in range(2):
                x_pos = x_pos + 350
                self._create_car(x_pos, y_pos, speed, True)
            y_pos += 50
            speed += 1
        
        speed = 2
        
        for i in range(2):
            for i in range(2):
                x_pos = x_pos - 350
                self._create_car(x_pos, y_pos, speed, False)
            y_pos += 50
            speed += 1

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
        goal_reached = pygame.sprite.spritecollide(self.frog, self.all_goals, True)
        
        if goal_reached:
            if len(self.all_goals) == 0:
                print('you win!')
            else:
                print('goal_reached')
                self.frog.center()

    def _check_hazard_collide(self):        
        self._fell_in_water()
        self._check_touched_edges()
        self._check_hit_by_car()
    
    def _fell_in_water(self):
        water_touched_frog = self.water.rect.colliderect(self.frog.rect)
        if water_touched_frog and not self.frog.is_on_log:
            self.frog.center()

    def _check_hit_by_car(self):
        cars_hit_frog = pygame.sprite.spritecollide(self.frog, self.all_cars, False )
        if any(cars_hit_frog):
            self.frog.center()
            
    def _check_touched_edges(self):
        touched_edge = pygame.sprite.spritecollide(self.frog, self.all_borders, False)
        if any(touched_edge):
            self.frog.center()
        
    def _check_on_log(self):
        on_a_log = pygame.sprite.spritecollide(self.frog, self.all_logs, False)
        self.frog.is_on_log = any(on_a_log)
    
if __name__ == '__main__':
    ribbit = Ribbit()
    ribbit.run_game()
