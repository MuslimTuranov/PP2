import pygame
import sys

pygame.init()

height = 800
width = 800

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Kanye West, TY Dolla Sign ft. Rich Kid, Playboi Carti - Carnival")
pygame.mixer.init()
carnival_path = r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\2.py\Carnival.wav"
kanye_path = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\2.py\kanyebear.jpg")
music_list = [carnival_path]
pygame.mixer.music.load(music_list[0])
pygame.mixer.music.play(-1)
kanye = pygame.transform.scale(kanye_path, (500,500))
screen.blit(kanye, (150, 150))

black = (0, 0, 0)

run = True
index = 0
pl = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pl = not pl
                if pl:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                pos = pygame.mixer.music.get_pos() / 1000  
                pygame.mixer.music.set_pos(pos + 10)  
            elif event.key == pygame.K_LEFT:
                pos = pygame.mixer.music.get_pos() / 1000  
                pygame.mixer.music.set_pos(pos - 10)   
                
                
    pygame.display.flip()