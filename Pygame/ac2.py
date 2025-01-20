import pygame
pygame.init()
screen=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adding images to the game")
background=pygame.transform.scale(
    pygame.image.load("background.png").convert(), (500, 500)
)
pygame.display.set_caption("Adding images to the game")

background=pygame.transform.scale(
    pygame.image.load("background.png").convert(), (500, 500)
)

penguin=pygame.transform.scale(
    pygame.image.load("penguin.png").convert(), (200, 200)
)

penguin_rect=penguin.get_rect(center=(500//2, 500//2 -30))
text=pygame.font.Font(None, 36).render("Hello Keshav", True, pygame.Color("black"))
text_rect=text.get_rect(center=(500//2, 500//2 + 110))

def game_loop():
    clock= pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        screen.blit(background, (0, 0))
        screen.blit(penguin, penguin_rect)
        screen.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
game_loop()