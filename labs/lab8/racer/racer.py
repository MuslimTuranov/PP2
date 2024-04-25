import pygame, sys, random, time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

FPS = 60
FramePerSec = pygame.time.Clock()

width = 600
height = 400

speed = 5
score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab8\racer\AnimatedStreet.png")

screen = pygame.display.set_mode((height, width))
screen.fill(white)
pygame.display.set_caption("Racist")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab8\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

      def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab8\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < width:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
      
p1 = Player()
e1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
      
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              speed += 0.5      
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, black)
    screen.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
        

    if pygame.sprite.spritecollideany(p1, enemies):
          pygame.mixer.Sound(r"C:\Users\musli\Documents\pp2\PP2\labs\lab8\racer\crash.wav").play()
          time.sleep(1)
                   
          screen.fill(red)
          screen.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
