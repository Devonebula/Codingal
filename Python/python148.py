import pygame

screen_width, screen_height= 600, 600
move_speed=5

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
    def move(self, x_change, y_change):
        self.rect.x=max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y=max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)
    
    
allsprite=pygame.sprite.Group()
sp1=sprite(pygame.Color("red"), 60, 60)
allsprite.add(sp1)

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                sp1.move(0, -move_speed)
            if event.key==pygame.K_DOWN:
                sp1.move(0, move_speed)
            if event.key==pygame.K_LEFT:
                sp1.move(-move_speed, 0)
            if event.key==pygame.K_RIGHT:
                sp1.move(move_speed, 0)
    screen.fill((0,0,0))
    allsprite.draw(screen)
    pygame.display.flip()

pygame.quit()