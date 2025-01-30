import pygame
pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill((0, 0 ,0))

pygame.display.set_caption("My First game screen")

red=(255, 0, 0)

rect_width = 100
rect_height = 80
x = (400 - rect_width) // 2
y = (400 - rect_height) // 2

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, red, pygame.Rect(x, y, rect_width, rect_height))
    pygame.draw.circle(screen, (255,255,255), (200,200), 90, 3)
    pygame.display.flip()
