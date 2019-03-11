class Settings:
    # store settings

    def __init__(self):
        # initialize game settings
        # screen settings
        self.screen_width = 800
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.pacspd = 2
        self.rect_size = 15
        self.pac_size = self.rect_size * 5