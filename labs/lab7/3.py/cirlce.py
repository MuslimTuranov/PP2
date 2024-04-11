import pygame 
import sys

pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)

width = 800
height = 800

radius = 25

speed = 20

screen = pygame.display.set_mode((height, width))

ball_x = 400
ball_y = 400

pygame.display.set_caption("Red Ball")

while True:
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), radius)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y < 610:
                    ball_y -= speed
            if event.key == pygame.K_DOWN:
                if ball_y > -10:
                    ball_y += speed
            if event.key == pygame.K_LEFT:
                if ball_x < 610:
                    ball_x -= speed
            if event.key == pygame.K_RIGHT:
                if ball_x > -10:
                    ball_x += speed
    