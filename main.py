import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfields import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    asteroid_field = AsteroidField()
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:    
            object.update(dt) 
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("game over")
                sys.exit()

        screen.fill("black")

        for object in drawable:    
            object.draw(screen)

        pygame.display.flip()

        #Framerate 
        dt = clock.tick(60) / 1000

        

if __name__ == "__main__":
    main()