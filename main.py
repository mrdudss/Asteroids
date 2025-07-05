import pygame
from constants import *
from circleshape import *
from player import *
# cd /root/repo/Asteroids
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    fps = pygame.time.Clock()
    dt = 0
    the_player = player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = fps.tick(60)
        player.draw(screen)
        pygame.display.flip()
    

main()