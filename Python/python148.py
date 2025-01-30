import pygame

screen_width, screen_height= 600, 600

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image= pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        