import pygame

class Ship():
    def __init__(self,ai_setting,screen):
        #Initialize the ship and set its starting position.
        self.screen=screen
        self.ai_setting= ai_setting

        #load the ship image and get its rect.
        self.image=pygame.image.load('F:\projects\projectSanghrah\Alien Invasion\images\ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new ship at the bottom  center of the screen.
        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom= self.screen_rect.bottom

        #store decimal value for the centerx
        self.center=float(self.rect.centerx)

        #Moving flag
        self.moving_right= False
        self.moving_left= False

    def update(self):
        '''Updat the ship's position based on the movement flag '''
        #update ships center value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left >0:
           self.center -=self.ai_setting.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx=self.center

    def blitme(self):
        #Draw the ship at its current location.
        self.screen.blit(self.image,self.rect)
