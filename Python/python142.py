import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My First Game Screen") 

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip