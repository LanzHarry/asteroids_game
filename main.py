import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for ast_elt in asteroids:
            if ast_elt.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot_elt in shots:
                if ast_elt.collides_with(shot_elt):
                    log_event("asteroid_shot")
                    shot_elt.kill()
                    ast_elt.split()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60)/1000



if __name__ == "__main__":
    main()
