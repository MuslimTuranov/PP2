import pygame 
import datetime

pygame.init()

clock = pygame.time.Clock()

mick = pygame.transform.scale(pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\1.py\output.png"), (800, 600))
min_hand = pygame.transform.scale(pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\1.py\rightie.jpg"), (800, 600))
sec_hand = pygame.transform.scale(pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\1.py\leftie.jpg"), (50, 600))

def rot_center(surf, image, angle, x, y):
    image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center=image.get_rect(center=(x, y)).center)
    surf.blit(image, rect)
    
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(mick, (0, 0))

    t = datetime.datetime.now()
    sec_angle = -t.second * 6
    min_angle = -t.minute * 6
    
    rot_center(screen, sec_hand, sec_angle, 400, 300)
    rot_center(screen, min_hand, min_angle + sec_angle / 60, 400, 300)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
