import pygame,sys
import random, time

pygame.init()

global viv
viv = [[".",".","."],[".",".","."],[".",".","."]]
global a
a = 1 
font = pygame.font.SysFont('airal', 20,True,False)

frame = pygame.time.Clock()

        
def tik(x, y):
    global viv,a
    pos_x = int(x//140)
    pos_y = int(y//140)
    print(pos_y , pos_x,a,)

    #enter를 누른 위치와 플레이어의 턴을 확인후 틱택토 판에 O,X 부여
    if viv[pos_y][pos_x] == ".":
        if a%2==1:
            viv[pos_y][pos_x] = "O"
        elif a%2==0:
            viv[pos_y][pos_x] ="X"
    else:
        for i in range(0,3,1):
            print(viv[i])
        return 0
    for i in range(0,3,1):
        print(viv[i])

    #가로 방향 승리 확인
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if viv[i][j] == "O":
                count = count+1
            if count ==3:
                return 1
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if viv[i][j] == "X":
                count = count+1
            if count ==3:
                return 2
    #세로 방향 승리 확인           
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if viv[j][i] == "O":
                count = count+1
            if count ==3:
                return 1
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if viv[j][i] == "X":
                count = count+1
            if count ==3:
                return 2
    #대각선 방향 승리 확인
    if viv[0][0] == "O" and(viv[1][1] == "O" and viv[2][2]=="O"):
        return 1
    elif viv[0][2] == "O" and(viv[1][1] == "O" and viv[2][0] == "O"):
        return 1
    if viv[0][0] == "X" and(viv[1][1] == "X" and viv[2][2] == "X"):
        return 2
    elif viv[0][2] == "X" and(viv[1][1] == "X" and viv[2][0]=="X"):
        return 2

    a  = a+1
    #마지막턴일 경우 무승부 선언
    if a == 10:
        return 3
    for i in range(0,3,1):
        viv[i]
    return 4
    

screen_width = 430 #가로 크기
screen_height = 430 #세로 크기

screen = pygame.display.set_mode((screen_width, screen_height)) #화면의 크기 조정
pygame.display.set_caption('틱택토 게임(2인용)') #타이틀 바

RED = (255, 0, 0)
ORANGE = (255, 153, 51)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SEAGREEN = (60, 179, 113)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (204, 153, 255)
PINK = (255, 153, 153)

background = pygame.image.load("a.jpg")
screen_O = pygame.image.load("O.png")
screen_X = pygame.image.load("X.png")
background1 = pygame.image.load("기본화면.png")

character = pygame.image.load("click1.png")
character_size = character.get_rect().size #캐릭터 이미지 사이즈 구하기
character_width = character_size[0] #가로 크기
character_height = character_size[1] #세로 크기
character_x = (screen_width/ 2) - (character_width / 2) #화면 가로 절반의 중간에 위치. 좌우로 움직이는 변수
character_y =screen_height - character_height #이미지가 화면 세로의 가장 아래 위치

vitory1 = pygame.image.load("승리1.png")
vitory2 = pygame.image.load("승리2.png")
vitory3 = pygame.image.load("무승부.png")

x = 0
y = 0
b= 4
running = False 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = True
    
    while running:
        for event in pygame.event.get(): #이벤트의 발생 여부 확인
            if event.type == pygame.QUIT: #창 닫기 버튼 누름 여부
                running = False
            if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
                if event.key == pygame.K_LEFT: #왼쪽 방향키
                    x -= 5
                elif event.key == pygame.K_RIGHT: #오른쪽 방향키
                    x += 5
                elif event.key == pygame.K_DOWN: #아래쪽 방향키
                    y += 5
                elif event.key == pygame.K_UP: #위쪽 방향키
                    y -= 5
                elif event.key ==pygame.K_RETURN:
                    b = tik(character_x,character_y)
                    if b == 0:
                        x =  0-character_x #마우스 (0,0) 위치로 이동
                        y =  0-character_y
                    elif b == 1:
                        print(b)
                        screen.blit(vitory1,(0,0))
                        pygame.display.update()
                        time.sleep(4)  
                        running = False
                    elif b == 2:
                        print(b)
                        screen.blit(vitory2,(0,0))
                        pygame.display.update()
                        time.sleep(4)  
                        running = False
                    elif b == 3:
                        screen.blit(vitory3,(0,0))
                        pygame.display.update()
                        time.sleep(4)
                        running = False
                    elif b == 4:
                        pass


            if event.type == pygame.KEYUP: #없으면 마우스가 폭주함
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y = 0
        
        character_x += x
        character_y += y

        #마우가 나가지 못하게 함
        if character_x < 0:
            character_x = 0

        elif character_x> screen_width - character_width:
            character_x = screen_width - character_width

        if character_y < 0:
            character_y = 0

        elif character_y > screen_height - character_height:
            character_y = screen_height - character_height

        screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
        screen.blit(character, (character_x, character_y)) #배경에 캐릭터 그려주기
        for i in range(0,3,1):
            for j in range(0,3,1):
                if viv[i][j] == ".":
                    pass
                elif viv[i][j] == "O":
                    screen.blit(screen_O,(j*140,(i)*140))
                elif viv[i][j] == "X":
                    screen.blit(screen_X,(j*140,(i)*140))
        if a%2==0:
            c = 2
        else:
            c=1
        player = font.render("Player " + str(c), True, RED)
        screen.blit(player,(0,0))
        pygame.display.update()
        frame.tick(60) #60프레임 설정
    screen.blit(background1,(0,0))
    pygame.display.update()
    viv = [[".",".","."],[".",".","."],[".",".","."]]
    a= 1

    
pygame.quit()
