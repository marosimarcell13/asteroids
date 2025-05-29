# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Set containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    #Instantiate player and asteroid field
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #Initalize pygame
    pygame.init()

    #Set game clock
    dt = 0
    clock = pygame.time.Clock()

    #Create display with SCREEN_WIDTH and SCREEN_HEIGHT form constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Fill the screen background with black
        screen.fill("black")

        #Call updatable group
        updatable.update(dt)

        #Check for collision
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                return print("Game over!")
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    asteroid.split()
                    shot.kill()
        
        #Call drawable group
        for thing in drawable:
            thing.draw(screen)

        #Refresh screen
        pygame.display.flip()

        #Get time delta since last refresh
        dt = clock.tick(60)/1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()