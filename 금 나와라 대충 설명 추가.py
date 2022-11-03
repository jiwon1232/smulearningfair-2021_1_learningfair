import pygame

import random

pygame.init()

screen_width = 749
screen_height = 588

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Gold")

background = pygame.image.load("C:/Users/82105/OneDrive/바탕 화면/새 폴더/게임/background1.jpg")

player = pygame.image.load("C:/Users/82105/OneDrive/바탕 화면/새 폴더/게임/miner.png")
player = pygame.transform.scale(player, (70,109))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_posX = 0
player_posY = 0

hole = pygame.image.load("C:/Users/82105/OneDrive/바탕 화면/새 폴더/게임/hole.png")
hole = pygame.transform.scale(hole, (120,40))
hole_size = hole.get_rect().size
hole_width = hole_size[0]
hole_height = hole_size[1]
hole_posX = random.randrange(1,670)
hole_posY = random.randrange(294, 549)

hole1 = pygame.image.load("C:/Users/82105/OneDrive/바탕 화면/새 폴더/게임/hole.png")
hole1 = pygame.transform.scale(hole1, (120,40))
hole1_size = hole1.get_rect().size
hole1_width = hole1_size[0]
hole1_height = hole1_size[1]
hole1_posX = random.randrange(1,670)
hole1_posY = random.randrange(294, 549)

hole2 = pygame.image.load("C:/Users/82105/OneDrive/바탕 화면/새 폴더/게임/hole.png")
hole2 = pygame.transform.scale(hole2, (120,40))
hole2_size = hole2.get_rect().size
hole2_width = hole2_size[0]
hole2_height = hole2_size[1]
hole2_posX = random.randrange(1,670)
hole2_posY = random.randrange(294, 549)

goal = pygame.image.load("C:/Users/82105/OneDrive/바탕 화면/새 폴더/게임/hole.png")
goal = pygame.transform.scale(goal, (120,40))
goal_size = goal.get_rect().size
goal_width = goal_size[0]
goal_height = goal_size[1]
goal_posX = random.randrange(315,670)
goal_posY = random.randrange(294, 549)

font_gameover = pygame.font.SysFont(None, 80)
font_gameclear = pygame.font.SysFont(None, 80)
text_gameover = font_gameover.render("Game Over", True, (255,0,0))
text_gameclear = font_gameclear.render("Game Clear", True, (255,212,0))

text_gameover_size = text_gameover.get_rect().size
text_gameover_width = text_gameover_size[0]
text_gameover_height = text_gameover_size[1]
text_gameover_posX = screen_width/2 - text_gameover_width/2
text_gameover_posY = screen_height/2 - text_gameover_height/2

text_gameclear_size = text_gameclear.get_rect().size
text_gameclear_width = text_gameclear_size[0]
text_gameclear_height = text_gameclear_size[1]
text_gameclear_posX = screen_width/2 - text_gameclear_width/2
text_gameclear_posY = screen_height/2 - text_gameclear_height/2


to_x = 0
to_y = 0



running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창닫기 버튼 누르면 꺼지게 하는 코드
            running = False

        #광부 움직이게 하는 코드 
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_LEFT:
                to_x -= 0.05
            elif event.key == pygame.K_RIGHT:
                to_x += 0.05
            elif event.key == pygame.K_DOWN:
                to_y += 0.05
            elif event.key == pygame.K_UP:
                to_y -= 0.05

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    player_posX += to_x
    player_posY += to_y

    #구덩이, 광부  화면 밖으로 못 나가게 하기
    if player_posX < 0:
        player_posX = 0

    elif player_posX > screen_width - player_width:
        player_posX = screen_width - player_width

    if player_posY < 0:
        player_posY = 0

    elif player_posY > screen_height - player_height:
        player_posY = screen_height - player_height

    if hole_posX < 0:
        hole_posX = 0

    elif hole_posX > screen_width - hole_width:
        hole_posX = screen_width - hole_width

    if hole_posY < 0:
        hole_posY = 0

    elif hole_posY > screen_height - hole_height:
        hole_posY = screen_height - hole_height

    if hole1_posX < 0:
        hole1_posX = 0

    elif hole1_posX > screen_width - hole1_width:
        hole1_posX = screen_width - hole1_width

    if hole1_posY < 0:
        hole1_posY = 0

    elif hole1_posY > screen_height - hole1_height:
        hole1_posY = screen_height - hole1_height

    if hole2_posX < 0:
        hole2_posX = 0

    elif hole2_posX > screen_width - hole2_width:
        hole2_posX = screen_width - hole2_width

    if hole2_posY < 0:
        hole2_posY = 0

    elif hole2_posY > screen_height - hole2_height:
        hole2_posY = screen_height - hole2_height

    if goal_posX < 0:
        goal_posX = 0

    elif goal_posX > screen_width - goal_width:
        goal_posX = screen_width - goal_width

    if goal_posY < 0:
        goal_posY = 0

    elif goal_posY > screen_height - goal_height:
        goal_posY = screen_height - goal_height

    #구덩이, 광부 충돌하는 걸 알 수 있게 rect생성
    player_rect = player.get_rect()
    player_rect.left = player_posX
    player_rect.top = player_posY

    hole_rect = hole.get_rect()
    hole_rect.left = hole_posX
    hole_rect.top = hole_posY

    hole1_rect = hole1.get_rect()
    hole1_rect.left = hole1_posX
    hole1_rect.top = hole1_posY

    hole2_rect = hole2.get_rect()
    hole2_rect.left = hole2_posX
    hole2_rect.top = hole2_posY

    goal_rect = goal.get_rect()
    goal_rect.left = goal_posX
    goal_rect.top = goal_posY


    #구덩이끼리 겹치면 구덩이 위치 다시 정하기         
    if hole_rect.colliderect(hole1_rect):
        hole1_posX = random.randrange(1,670)
        hole1_posY = random.randrange(294, 549)

    if hole1_rect.colliderect(hole2_rect):
        hole2_posX = random.randrange(1,670)
        hole2_posY = random.randrange(294, 549)

    if hole2_rect.colliderect(hole_rect):
        hole_posX = random.randrange(1,670)
        hole_posY = random.randrange(294, 549) 
        
    if goal_rect.colliderect(hole_rect):
        goal_posX = random.randrange(315,670)
        goal_posY = random.randrange(294, 549) 

    if goal_rect.colliderect(hole1_rect):
        goal_posX = random.randrange(315,670)
        goal_posY = random.randrange(294, 549)

    if goal_rect.colliderect(hole2_rect):
        goal_posX = random.randrange(315,670)
        goal_posY = random.randrange(294, 549)

    #폭탄구덩이에 닿으면 Game Over 띄우기
    if player_rect.colliderect(hole_rect):
        screen.blit(text_gameover, (text_gameover_posX, text_gameover_posY))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    #금구덩이에 닿으면 Game Clear 띄우기
    if player_rect.colliderect(goal_rect):
        screen.blit(text_gameclear, (text_gameclear_posX, text_gameclear_posY))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    screen.blit(background, (0, 0)) 
    screen.blit(hole, (hole_posX, hole_posY))
    screen.blit(hole1, (hole1_posX, hole1_posY))
    screen.blit(hole2, (hole2_posX, hole2_posY))
    screen.blit(goal, (goal_posX, goal_posY))
    screen.blit(player, (player_posX, player_posY))
    pygame.display.update() # 게임화면을 지속적으로 그리기

pygame.quit()
