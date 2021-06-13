import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    #redraw the screen during each pass
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #make the most recently drawn screen visible
    pygame.display.flip()
    
   

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''respond to key presses '''
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            # Move the ship to the right.
            ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            ship.moving_left=True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings,screen,ship,bullets)
            


def check_keyup_events(event,ship):
    ''' respond to key releases '''
    if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    ship.moving_right=False
                elif event.key==pygame.K_LEFT:
                    ship.moving_left=False
def update_bullets(bullets):
    ''' Update position of bullets and get rid of old bullets. '''
    #Update bullet position
    bullets.update()
        #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
def fire_bullet(ai_settings,screen,ship,bullets):
    ''' fire a bullet if limit not reach yet '''
    #Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
