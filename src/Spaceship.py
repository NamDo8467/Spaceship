import pygame


class Spaceship:
    def __init__(self):
        self.image = pygame.image.load("images/spaceship_red.png").convert_alpha()
        self.spaceShipObject = pygame.transform.rotate(pygame.transform.scale(self.image, (50,50)), 180)
        self.X = 0
        self.Y = 420

    def fire(self):
        bullet = pygame.Rect(self.X + 20, self.Y - 25, 10, 10)

        return bullet

    def detect_collision(self):
        pass


