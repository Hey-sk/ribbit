class Settings:

    def __init__(self):
        #game tiles
        self.col_spaces = 15
        self.row_spaces = 13
        
        #frog settings
        self.frog_size = 50

        #screen settings
        self.screen_width = self.frog_size * self.row_spaces
        self.screen_height = self.frog_size * self.col_spaces
    
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (40, 40, 40)

        