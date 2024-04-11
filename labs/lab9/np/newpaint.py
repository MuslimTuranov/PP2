import pygame
import math

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

colors = [red, green, blue, yellow, black]  
selected_color = red  
thickness = 5

height = 700
width = 700
color_box_size = 50  
color_box_margin = 10 
color_box_y_start = height - color_box_size - color_box_margin  
color_boxes = []

for i, color in enumerate(colors):
    x = color_box_margin + (color_box_size + color_box_margin) * i
    y = color_box_y_start
    color_boxes.append((x, y, color_box_size, color_box_size, color)) 

screen = pygame.display.set_mode((height, width))
screen.fill(white)
pygame.display.set_caption("Paint")

lmbpressed = False
selected_box_index = None  
drawing_mode = None  
triangle_points = []  
square_start = None  
circle_center = None  
circle_radius = 0  

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            lmbpressed = True
            pos = pygame.mouse.get_pos()

            for i, box in enumerate(color_boxes):
                if box[0] < pos[0] < box[0] + box[2] and box[1] < pos[1] < box[1] + box[3]:
                    selected_color = box[4]  
                    selected_box_index = i
                    break

            if drawing_mode == "triangle":
                triangle_points.append(pos)  

            elif drawing_mode == "square":
                square_start = pos  

            elif drawing_mode == "circle":
                circle_center = pos  
                circle_radius = 0  

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            lmbpressed = False

            if drawing_mode == "triangle" and len(triangle_points) == 3:
                pygame.draw.polygon(screen, selected_color, triangle_points)
                triangle_points = []  

            elif drawing_mode == "square" and square_start:
                end_pos = pygame.mouse.get_pos()
                width = end_pos[0] - square_start[0]
                height = end_pos[1] - square_start[1]
                square_rect = pygame.Rect(square_start[0], square_start[1], width, height)
                pygame.draw.rect(screen, selected_color, square_rect)
                square_start = None

            elif drawing_mode == "circle" and circle_center:
                pygame.draw.circle(screen, selected_color, circle_center, circle_radius)
                circle_center = None
                circle_radius = 0

        elif event.type == pygame.MOUSEMOTION:
            if drawing_mode == "circle" and circle_center:
                mouse_pos = pygame.mouse.get_pos()
                circle_radius = int(math.hypot(mouse_pos[0] - circle_center[0], mouse_pos[1] - circle_center[1]))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if thickness < 200:
                    thickness += 5
            if event.key == pygame.K_DOWN:
                if thickness > 5:
                    thickness -= 5
            if event.key == pygame.K_0:
                screen.fill(white)
            if event.key == pygame.K_t:  
                drawing_mode = "triangle"
            elif event.key == pygame.K_s:  
                drawing_mode = "square"
            elif event.key == pygame.K_c:  
                drawing_mode = "circle"

    for box in color_boxes:
        pygame.draw.rect(screen, box[4], box[:4])  

    if selected_box_index is not None:
        pygame.draw.rect(screen, white, color_boxes[selected_box_index][:4], width=2)  

    if drawing_mode == "triangle" and len(triangle_points) == 2:
        pygame.draw.line(screen, selected_color, triangle_points[0], triangle_points[1], thickness)

    if drawing_mode == "square" and square_start:
        end_pos = pygame.mouse.get_pos()
        width = end_pos[0] - square_start[0]
        height = end_pos[1] - square_start[1]
        square_rect = pygame.Rect(square_start[0], square_start[1], width, height)
        pygame.draw.rect(screen, selected_color, square_rect, thickness)

    if drawing_mode == "circle" and circle_center:
        pygame.draw.circle(screen, selected_color, circle_center, circle_radius, thickness)

    pygame.display.flip()
