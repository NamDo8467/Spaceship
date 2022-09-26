import pygame

from src.Spaceship import Spaceship
from src.Wall import Wall


pygame.init()

TITLE = "GAME"
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
SPACESHIP_X = 0
SPACESHIP_Y = 420
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
background = pygame.image.load("images\\spaceBackground.jpg").convert()

running = True

spaceShip = Spaceship()

wall = Wall()

bullets = []


def draw_window_and_object():
    screen.blit(background, (0, 0))

    screen.blit(spaceShip.spaceShipObject, (spaceShip.X, spaceShip.Y))

    for layer in wall.queue:
        for brick in layer.getAllBricks():
            if brick is not None:
                pygame.draw.rect(screen, brick.color, pygame.Rect(brick.x, brick.y, brick.width, brick.height), 0, 3)

    wall.addLayerOfBricks()


def handle_bullets_fire():
    if len(bullets) == 0:
        return
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
        for layer in wall.queue:
            for brick in layer.getAllBricks():
                if brick is not None:
                    if bullet.colliderect(pygame.Rect(brick.x, brick.y, brick.width, brick.height)):
                        bullets.remove(bullet)
                        layer.removeBrick(brick.x, brick.y)
        bullet.y -= 3
        if bullet.y < 0:
            bullets.remove(bullet)


def handle_movement(keys):
    if keys[pygame.K_RIGHT] and spaceShip.X < SCREEN_WIDTH - 50:
        spaceShip.X += 20
    if keys[pygame.K_LEFT] and spaceShip.X > 0:
        spaceShip.X -= 10


clock = pygame.time.Clock()


while running:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_COMMA:
                bullet = spaceShip.fire()
                bullets.append(bullet)

    keys_pressed = pygame.key.get_pressed()
    handle_movement(keys_pressed)
    draw_window_and_object()
    handle_bullets_fire()

    pygame.display.update()


pygame.quit()