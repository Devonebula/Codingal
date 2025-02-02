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
enemy_speed_y=20
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


enemy_img=[]
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

def game_over_text():
    over_text=over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
    

def fire_bullet(x, y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img, (x+16, y+10))
    
def collision(enemyX, enemyY, bulletX, bulletY):
    distance=math.sqrt((enemyX- bulletX)**2 + (enemyY-bulletY)**2)
    return distance < collition_distance

running=True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_X_Change=-5
            if event.key== pygame.K_RIGHT:
                player_X_Change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletX=playerX
                fire_bullet(bulletX, bulletY)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_X_Change=0
            
    playerX=player_X_Change
    playerX=max(0, min(playerX, screen_width-64))

    for i in range(no_of_enemies):
        if enemyY[i]>340:
            for j in range(no_of_enemies):
                enemyY[j]=2000
                game_over_text()
                break
        enemyX[i]+=enemy_X_Change[i]
        if enemyX[i]<=0 or enemyX[i]>=screen_width-64:
            enemy_X_Change[i]*= -1
            enemyY[i]+=enemy_Y_Change[i]

        if collision(enemyX[i], enemyY[i], bulletX, bulletY) and bullet_state=="fire":
            bulletY= player_start_y
            bullet_state="ready"
            score+=1
            enemyX[i]=random.randint(0, screen_width-64)
            enemyY[i]=random.randint(enemy_start_y_min, enemy_start_y_max)
        enemy(enemyX[i], enemyY[i], i)
    
    if bulletY<=0:
        bulletY=player_start_y
        bullet_state="ready"

    elif bullet_state=="fire":
        fire_bullet(bulletX, bulletY)
        bulletY-=bullet_Y_Change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
