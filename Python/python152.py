import pygame
from pygame import mixer

pygame.init()
mixer.init()



bg=pygame.transform.scale(pygame.image.load("bg/bg.jpg"), (500,500))

screen=pygame.display.set_mode((500,500))
mixer.music.load('song.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        pygame.display.flip()

pygame.quit()