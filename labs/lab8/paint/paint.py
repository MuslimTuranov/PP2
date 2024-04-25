import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

color = black

height = 800
width = 800

thickness = 5

screen = pygame.display.set_mode((height, width))
screen.fill(white)
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

lmbpressed = False

curX = 0
curY = 0
prevX = 0
prevY = 0

done = False

while not done:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            lmbpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        elif event.type == pygame.MOUSEMOTION:
            print(event.pos)
            if lmbpressed:
                curX = event.pos[0]
                curY = event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            lmbpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.rect(screen, color, (prevX, prevY, curX - prevX, curY - prevY), thickness)
        
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                if thickness < 200:
                    thickness += 5
            if event.key == pygame.K_DOWN:
                if thickness > 5:
                    thickness -= 5
            if event.key == pygame.K_1:
                color = red
            if event.key == pygame.K_2:
                color = blue
            if event.key == pygame.K_3:
                color = green
            if event.key == pygame.K_4:
                color = yellow
            if event.key == pygame.K_5:
                color = black
            if event.key == pygame.K_0:
                screen.fill(white)
        
    pygame.display.flip()