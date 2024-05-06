import sys

import pygame

from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class game:


    def __init__(self):
        pygame.init()

        # screen display size

        pygame.display.set_caption('Echoes of the Nameless City')
        self.screen = pygame.display.set_mode((640,480))

        # frames per second

        self.clock = pygame.time.Clock()

        self.img_pos = [160, 260]        # image position attribute
        self.movement = [False, False]   # Movement variable

        self.assets = {
            'player': load_image('entities/player.png')
        }

        # Physics

        self.collision_area = pygame.Rect(50,50,300,50)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):

        # Exit funciton

        while True:
            self.screen.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

game().run()