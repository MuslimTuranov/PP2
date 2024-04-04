import pygame
import time
import random

pygame.init()

width = 600
height = 600
pygame.display.set_caption("kd")
screen = pygame.display.set_mode((height, width))

speed = 15

clock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

snake_pos = [300, 300]

snake_body = [[100, 50], [90, 50]]

apple_position = [random.randrange(1, (height // 10)) * 10, random.randrange(1, (width // 10)) * 10]

apple_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

fruit_time = 5

def show_score(choice, color, font, size) :
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    screen.blit(score_surface, score_rect)


def game_over() :
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render('GAME OVER', True, red)
    score_surface = my_font.render('Your Score is : ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()
    score_rect = score_surface.get_rect()

    game_over_rect.midtop = (height / 2, width / 4)
    score_rect.midtop = (height / 2, game_over_rect.bottom + 20)

    screen.blit(game_over_surface, game_over_rect)
    screen.blit(score_surface, score_rect)
    pygame.display.flip()
    
    pygame.clock(5)
    
    pygame.quit()

while True :

    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'


    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'

    if direction == 'UP' :
        snake_pos[1] -= 10
    if direction == 'DOWN' :
        snake_pos[1] += 10
    if direction == 'LEFT' :
        snake_pos[0] -= 10
    if direction == 'RIGHT' :
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == apple_position[0] and snake_pos[1] == apple_position[1] :
        score += 10
        apple_spawn = False
    else :
        snake_body.pop()

    if not apple_spawn :
        apple_position = [random.randrange(1, (height // 10)) * 10,random.randrange(1, (width // 10)) * 10]
    apple_spawn = True
    screen.fill(black)

    for pos in snake_body :
        pygame.draw.rect(screen, green,pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, red, pygame.Rect(apple_position[0], apple_position[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > height - 10 :
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > width - 10 :
        game_over()


    for block in snake_body[1 :] :
        if snake_pos[0] == block[0] and snake_pos[1] == block[1] :
            game_over()

    show_score(1, white, 'times new roman', 20)

    pygame.display.update()

    clock.tick(speed)
