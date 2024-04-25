import pygame

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Толщина линии
LINE_WIDTH = 5

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Рисование фигур")

# Текущая фигура
selected_shape = "line"

# Текущий цвет
selected_color = BLACK

# Список фигур
shapes = []

# Функция рисования линии
def draw_line(screen, start_pos, end_pos, color, width):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

# Функция рисования прямоугольника
def draw_rectangle(screen, start_pos, end_pos, color, fill):
    if fill:
        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    else:
        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), LINE_WIDTH)

# Функция рисования круга
def draw_circle(screen, center_pos, radius, color, fill):
    if fill:
        pygame.draw.circle(screen, color, center_pos, radius)
    else:
        pygame.draw.circle(screen, color, center_pos, radius, LINE_WIDTH)

# Функция рисования многоугольника
def draw_polygon(screen, points, color, fill):
    if fill:
        pygame.draw.polygon(screen, color, points)
    else:
        pygame.draw.polygon(screen, color, points, LINE_WIDTH)


# Функция отслеживания нажатия мыши
def get_mouse_pos():
    mouse_pos = pygame.mouse.get_pos()
    return mouse_pos

# Функция отрисовки
def draw_everything(screen, shapes, selected_shape, selected_color):
    screen.fill(WHITE)

    for shape in shapes:
        if shape["type"] == "line":
            draw_line(screen, shape["start_pos"], shape["end_pos"], shape["color"], LINE_WIDTH)
        elif shape["type"] == "rectangle":
            draw_rectangle(screen, shape["start_pos"], shape["end_pos"], shape["color"], shape["fill"])

