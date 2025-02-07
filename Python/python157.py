import pygame 
import random
import math

pygame.init()

screen_width=500
screen_height=500

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0, 0, 0))
pygame.display.set_caption("My First Game")

rect_width=60
rect_height=60
rectX=(screen_width- rect_width)//2
rectY=((screen_height-rect_height)//2) + 190

done=False
for i in range(7):
    pygame.draw.circle(screen, (255,255,255), ((random.randint(20, 250)) , (random.randint(20, 250))), 15)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0,125,225), pygame.Rect(rectX, rectY, rect_width, rect_height))
    pygame.display.flip()

pygame.quit()
