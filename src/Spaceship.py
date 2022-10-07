import pygame
from src.Colors import colors
from random import randrange


class Spaceship:
    __color_list = list(colors.values())

    def __init__(self):
        self.image = pygame.image.load("images/spaceship_red.png").convert_alpha()
        self.spaceShipObject = pygame.transform.rotate(pygame.transform.scale(self.image, (50, 50)), 180)
        self.X = 0
        self.Y = 420

    def fire(self):
        color_code = self.__color_list[randrange(0, len(self.__color_list))]
        bullet = {"color": color_code, "shape": pygame.Rect(self.X + 20, self.Y - 25, 10, 10)}
        return bullet

    def detect_collision(self, bullet, wall):
        for brick in wall.queue:
            if bullet["shape"].colliderect(pygame.Rect(brick.x, brick.y, brick.width, brick.height)) \
                    and bullet["color"] == brick.color:
                return brick
