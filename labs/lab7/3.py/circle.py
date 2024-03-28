import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
BALL_SIZE = BALL_RADIUS * 2
BALL_SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2

while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - BALL_SPEED >= 0:
                    ball_y -= BALL_SPEED
            elif event.key == pygame.K_DOWN:
                if ball_y + BALL_SPEED <= SCREEN_HEIGHT - BALL_SIZE:
                    ball_y += BALL_SPEED
            elif event.key == pygame.K_LEFT:
                if ball_x - BALL_SPEED >= 0:
                    ball_x -= BALL_SPEED
            elif event.key == pygame.K_RIGHT:
                if ball_x + BALL_SPEED <= SCREEN_WIDTH - BALL_SIZE:
                    ball_x += BALL_SPEED
