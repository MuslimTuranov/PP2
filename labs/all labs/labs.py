import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Определение размеров экрана и блока
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
block_size = 20

# Шрифт и размер текста
font_style = pygame.font.SysFont(None, 50)

# Функция вывода сообщения на экран
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Основная функция змейки
def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты змейки и скорость движения
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    # Начальные координаты яблока
    foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size

    # Главный игровой цикл
    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Вы проиграли! Нажмите C-новая игра или Q-выход", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Отслеживание действий пользователя
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Проверка на выход за границы экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Изменение координат змейки
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Рисование змейки на экране
        for segment in snake_List:
            pygame.draw.rect(dis, black, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        # Переключение яблока, если змейка его съела
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size
            Length_of_snake += 1

        pygame.display.update()

        # Скорость змейки
        pygame.time.Clock().tick(10)

    pygame.quit()
    quit()

gameLoop()
