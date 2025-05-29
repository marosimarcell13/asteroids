# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    #Instantiate player
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

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

        #Rotate player
        player.update(dt)

        #Draw player
        player.draw(screen)

        #Refresh screen
        pygame.display.flip()

        #Get time delta since last refresh
        dt = clock.tick(60)/1000       
        print(dt) 


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()