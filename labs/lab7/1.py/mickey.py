import pygame
import sys
import time

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

clock_image = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\1.py\output.png")
minute_hand_image = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\1.py\rightie.jpg")
second_hand_image = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\1.py\leftie.jpg")

clock_image = pygame.transform.scale(clock_image, (screen_width, screen_height))

def draw_clock(minute_angle, second_angle):
    screen.blit(clock_image, (0, 0))

    rotated_minute_hand = pygame.transform.rotate(minute_hand_image, minute_angle)
    minute_hand_rect = rotated_minute_hand.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(rotated_minute_hand, minute_hand_rect)

    rotated_second_hand = pygame.transform.rotate(second_hand_image, second_angle)
    second_hand_rect = rotated_second_hand.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(rotated_second_hand, second_hand_rect)

def get_hand_angles():
    current_time = time.localtime()
    minute_angle = -(current_time.tm_min * 6)  
    second_angle = -(current_time.tm_sec * 6)  
    return minute_angle, second_angle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  
    minute_angle, second_angle = get_hand_angles()
    draw_clock(minute_angle, second_angle)
    pygame.display.flip()
    pygame.time.delay(1000) 
