import pygame

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

        elif event.type == pygame.MOUSEMOTION:
            pass  

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            lmbpressed = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if thickness < 200:
                    thickness += 5
            if event.key == pygame.K_DOWN:
                if thickness > 5:
                    thickness -= 5
            if event.key == pygame.K_0:
                screen.fill(white)
    
   
    for box in color_boxes:
        pygame.draw.rect(screen, box[4], box[:4])  

  
    if selected_box_index is not None:
        pygame.draw.rect(screen, white, color_boxes[selected_box_index][:4], width=2)  

    if lmbpressed:
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, selected_color, (pos[0], pos[1], thickness, thickness))

    pygame.display.flip()
