import pygame
import math
import random

screen_width = 800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=40
collition_distance=27

pygame.init()

screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

bg=pygame.image.load("bg2/bg.png")
pygame.display.set_icon(pygame.image.load("bg2/UFO.png"))


player_img=pygame.image.load("bg2/Player.png")
playerX=player_start_x
playerY=player_start_y
player_X_Change=0


enemy_img=pygame.image.load("bg2/Enemy.png")
enemyX=[]
enemyY=[]
enemy_X_Change=[]
enemy_Y_Change=[]
no_of_enemies=10


for i in range(no_of_enemies):
    enemy_img.append(pygame.image.load("bg2/Enemy.png"))
    enemyX.append(random.randint(0, screen_width-64))
    enemyY.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_X_Change.append(enemy_speed_x)
    enemy_Y_Change.append(enemy_speed_y)

bullet_img=pygame.image.load("bg2/Bullet.png")
bulletX=0
bulletY=player_start_y
bullet_X_Change=0
bullet_Y_Change=-bullet_speed_y
bullet_state="ready"


score=0
font=pygame.font.Font("freesansbold.ttf", 32)
textX=10
textY=10

over_font=pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score_text=font.render("Score: "+str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))
