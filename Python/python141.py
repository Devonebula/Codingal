import pygame
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Color changing sprite")

colors={
    "red":pygame.Color('red'),
    "green":pygame.Color('green'),
    "blu":pygame.Color('blue'),
    "yellow":pygame.Color('yellow'),
    "white":pygame.Color('white')
}

current_color=colors['white']

x,y=30,30
sprite_width, sprite_height=60,60
clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
        pass