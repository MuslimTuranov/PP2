import pygame, random, sys, time

pygame.init()

speed = 15

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

height = 600
width = 600

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Kevin Durant cimulator")

fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50]]

fruit_position = [random.randrange(1, (height // 10)) * 10, random.randrange(1, (width // 10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def showscore(choice, color, font, size) :
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


def game_over() :
    game_over_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (height / 2, width / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

while True :

    for event in pygame.event.get() :
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
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] :
        score += 10
        fruit_spawn = False
    else :
        snake_body.pop()

    if not fruit_spawn :
        fruit_position = [random.randrange(1, (height // 10)) * 10, random.randrange(1, (width // 10)) * 10]

    fruit_spawn = True
    screen.fill(black)

    for pos in snake_body :
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > height - 10 :
        game_over()
    if snake_position[1] < 0 or snake_position[1] > width - 10 :
        game_over()

    for block in snake_body[1 :] :
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    showscore(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(speed)