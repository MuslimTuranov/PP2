import pygame as pg

CarnivalPath = r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\2.py\Carnival.wav"

pg.init()

sc = pg.display.set_mode((480, 360))
pg.display.set_caption("wav")
clock = pg.time.Clock()
pg.mixer.init()
musicList = [CarnivalPath]
pg.mixer.music.load(musicList[0])
pg.mixer.music.play(-1)
kanyebear = pg.image.load(r"C:\Users\musli\Documents\pp2\PP2\labs\lab7\2.py\kanyebear.jpg")


sc.blit(kanyebear, (0, 0))
flPlay = True
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
                flPlay = not flPlay
            elif event.key == pg.K_RIGHT:
                index = (index + 1) % len(musicList)
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index = (index - 1) % len(musicList)
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()

    pg.display.flip()
    clock.tick(60)
