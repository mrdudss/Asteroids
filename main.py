import sys
print(sys.path)

import pygame
from constants import *
from circleshape import *
from player import *
from Asteroids import *
from asteroidfield import *
from shot import Shot
# cd /root/repo/Asteroids
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    fps = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        for rocks in asteroids:
            for bullet in shots:
                if rocks.collision(bullet):
                    rocks.split()
                    bullet.kill()
            if player.collision(rocks):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = fps.tick(60)/1000
    

main()