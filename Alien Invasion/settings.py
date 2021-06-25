
class Settings():
    '''
    A class to store all settings for Alien Invasion. '''

    def __init__(self):
        '''
        Initialize the game's settings.
        '''
        # Screen settings
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(33,182,168)
        #ship setting
        self.ship_speed_factor=1.5
        self.ship_limit =2
        #bullet settings
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(127,84,23)
        self.bullets_allowed =5
        #Alien settings
        self.alien_speed_factor =1
        self.fleet_drop_speed=10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction=1
