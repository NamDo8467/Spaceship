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

# removed_bricks = []

brick_to_remove = None

def draw_window_and_object():
    screen.blit(background, (0, 0))

    screen.blit(spaceShip.spaceShipObject, (spaceShip.X, spaceShip.Y))

    for brick in wall.queue:
        pygame.draw.rect(screen, brick.color, pygame.Rect(brick.x, brick.y, brick.width, brick.height), 0, 3)

    wall.addLayerOfBricks()


def handle_bullets_collision():
    global wall
    global brick_to_remove

    if len(bullets) == 0:
        return
    for b in bullets:
        pygame.draw.rect(screen, b["color"], b["shape"])
        brick_to_remove = spaceShip.detect_collision(b, wall)
        if brick_to_remove:
            bullets.remove(b)
            wall.removeBrick(brick_to_remove)
        b["shape"].y -= 3
        if b["shape"].y < 0:
            bullets.remove(b)


def handle_movement(keys):
    if keys[pygame.K_RIGHT] and spaceShip.X < SCREEN_WIDTH - 50:
        spaceShip.X += 10
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
    handle_bullets_collision()

    pygame.display.update()


pygame.quit()
