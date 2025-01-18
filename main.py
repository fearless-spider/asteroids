# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
import sys

from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()

        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
