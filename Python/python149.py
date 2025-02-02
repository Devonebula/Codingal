import pygame
import random

# colors

red=pygame.Color('red')
green=pygame.Color('green')
blue=pygame.Color('blue')
yellow=pygame.Color('yellow')
white=pygame.Color('white')
black=pygame.Color('black')


pygame.init()
screen_width, screen_height= 600, 600

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image= pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x= (screen_width- width)// 2
        self.rect.y= (screen_height- height)// 2
        pygame.draw.rect(screen, color, pygame.Rect(self.rect.x, self.rect.y, width, height))
    def color_change(self):
        self.image.fill(random.choice([red, green, blue, yellow, white]))
        
sp1=sprite((255, 0 ,0) , 100, 100)
allsprite=pygame.sprite.Group()
allsprite.add(sp1)

clock=pygame.time.Clock()



done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    allsprite.update()
    screen.fill((0, 0 ,0))
    allsprite.draw(screen)
    sp1.color_change()
    pygame.display.flip()   
    
    clock.tick(10)

pygame.quit()
