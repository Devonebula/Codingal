import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))
pygame.display.set_caption("My First Game Screen")

rect_width, rect_height = 60, 60
rect_x = (400 - rect_width) // 2
rect_y = (400 - rect_height) // 2


font=pygame.font.SysFont("Times New Roman", 32)

text=font.render("Hello World", True, (0, 0, 255))
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(rect_x, rect_y, rect_width, rect_height))
screen.blit(text, (rect_x, rect_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

