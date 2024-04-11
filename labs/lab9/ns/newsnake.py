import pygame
import random
import sys
import time

pygame.init()

speed = 15

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

height = 800
width = 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Snake")

fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50]]


food_types = ['normal', 'special', 'disappearing']
food_weights = [0.6, 0.3, 0.1]  
direction = 'RIGHT'
change_to = direction

score_value = 0

disappearing_food_timer = 5  

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score_value), True, color)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    screen.blit(score_surface, score_rect)

def game_over():
    game_over_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font.render('Your Score is : ' + str(score_value), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (height / 2, width / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

def spawn_food():
    food_type = random.choices(food_types, weights=food_weights)[0] 
    
    if food_type == 'normal':
        return [random.randrange(1, (height // 10)) * 10, random.randrange(1, (width // 10)) * 10], blue, False
    elif food_type == 'special':
        return [random.randrange(1, (height // 10)) * 10, random.randrange(1, (width // 10)) * 10], green, False
    elif food_type == 'disappearing':
        return [random.randrange(1, (height // 10)) * 10, random.randrange(1, (width // 10)) * 10], red, True
def draw_food(food_position, color):
    pygame.draw.rect(screen, color, pygame.Rect(food_position[0], food_position[1], 10, 10))

def check_food_collision(snake_position, food_position, food_type, disappearing_food_timer):
    global score_value
    
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        if food_type == 'disappearing':
            score_value += 20  
        else:
            score_value += 10
        
        return True
    
    return False

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    food_spawned = False
    
    if not food_spawned:
        food_position, food_color, is_disappearing = spawn_food()
        food_spawned = True
        if is_disappearing:
            food_disappear_time = time.time() + disappearing_food_timer

    food_collided = check_food_collision(snake_position, food_position, food_types, food_disappear_time if is_disappearing else None)
    if food_collided:
        food_spawned = False

    if is_disappearing and time.time() > food_disappear_time:
        food_spawned = False

    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    draw_food(food_position, food_color)

    if snake_position[0] < 0 or snake_position[0] > height - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > width - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(speed)
