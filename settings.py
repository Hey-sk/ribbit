class Settings:

    def __init__(self):
        #game tiles
        self.col_spaces = 16
        self.row_spaces = 21
        
        #frog settings
        self.movement_speed = 1.5
        self.frog_size = 50

        #screen settings
        self.screen_width = self.frog_size * self.row_spaces
        self.screen_height = self.frog_size * self.col_spaces
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (40, 40, 40)
        