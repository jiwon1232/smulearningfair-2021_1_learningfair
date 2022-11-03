import pygame
import random
import os

###information
#
#   pygame 관련 코드들은 pygame 공식 documentation과 pygame를 다룬 많은 블로그들에서 참고했음
#   
#
#   말의 위치에 따라서 x좌표와 y좌표를 맞추는 것이 어려웠음
#   주사위가 굴러가는 장면을 구현하는데 어려웠음
#   -> alarm 변수를 따로 만들어서 변수에 맞춰, 주사위가 천천히 굴러가게 구현함
#   그림들은 뱀사다리게임 판만 인터넷에서 찾았고, 나머지는 그림 툴로 직접 그렸음
#   효과음들은 인터넷에서 찾았음
#   
#   게임 화면으로는 전달하지 못할 정보(도움말, 시도 횟수 등)를 python 콘솔에 출력하였음
#   추후 추가 개발을 위해서 많은 제어 변수들을 만들었음
#   계속 플레이하며 익숙하지 않은 pygame코드들의 많은 버그들을 고쳤음
#

###init
pygame.init()

###setup
#current_path = os.path.dirname(__file__)
#image_path = os.path.join(current_path, "images")
#image = pygame.image.load(os.path.join(image_path, "image.png"))
screen_width = 720
screen_height = 540
SCREEN = pygame.display. set_mode([screen_width,screen_height])
pygame.display.set_caption("snake_dice_game")
clock = pygame.time.Clock()
playing = True
alarm = [-1,-1,-1,-1,-1]

red = pygame.color.Color('#FF0000')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

myFont = pygame.font.SysFont('arial', 30, True, False)
text_ending = myFont.render("clear! ", True, black)

sfx_good = pygame.mixer.Sound("se_extend.wav")
sfx_bad = pygame.mixer.Sound("se_pldead00.wav")
sfx_clear = pygame.mixer.Sound("se_pause.wav")

###object
map = pygame.image.load("map.jpg")
map = pygame.transform.scale(map, (screen_height, screen_height))
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (screen_height/10, screen_height/10))
dice1 = pygame.image.load("dice1.png")
dice2 = pygame.image.load("dice2.png")
dice3 = pygame.image.load("dice3.png")
dice4 = pygame.image.load("dice4.png")
dice5 = pygame.image.load("dice5.png")
dice6 = pygame.image.load("dice6.png")


#player_rect = player.get_rect()

#player_rect.centerx = screen_width / 2
#player_rect.centery = screen_height / 2

###function
def dice():
    return random.randrange(1, 7)

def snake_or_ladder():
    global player_count
    p  = player_count
    mp = 0
    ret = 0
    
    if (p == 1):
        mp = 38
        ret = 1
    elif (p == 4):
        mp = 14
        ret = 1
    elif (p == 9):
        mp = 31
        ret = 1
    elif (p == 17):#s
        mp = 7
        ret = 2
    elif (p == 21):
        mp = 42
        ret = 1
    elif (p == 28):
        mp = 84
        ret = 1
    elif (p == 51):
        mp = 67
        ret = 1
    elif (p == 54):#s
        mp = 34
        ret = 2
    elif (p == 62):#s
        mp = 19
        ret = 2
    elif (p == 64):#s
        mp = 60
        ret = 2
    elif (p == 71):
        mp = 91
        ret = 1
    elif (p == 80): 
        mp = 100
        ret = 1
    elif (p == 87):#s
        mp = 24
        ret = 2
    elif (p == 93):#s
        mp = 73
        ret = 2
    elif (p == 95):#s
        mp = 75
        ret = 2
    elif (p == 98):#s
        mp = 79
        ret = 2

    if (ret == 1):
        print("{} LADDER! goto {}".format(p, mp))
        sfx_good.set_volume(0.05)
        sfx_good.play()
        player_count = mp
    elif (ret == 2):
        print("{} SNAKE!!! goto {}".format(p, mp))
        sfx_bad.set_volume(0.03)
        sfx_bad.play()
        player_count = mp
    else:
        player_count = p    

###var
room = "room_main"

player_count = 0
player_x = screen_width-100
player_y = (screen_height/20)*18
dice_index = 1
dice_x = screen_width-128-32
dice_y = screen_height-128-32
try_count = 0
dice_roll = 10
freeze = 0

###start
print("----------------------------------------------------------")
print("")
print("Snake dice game")
print("press \'space\' to roll the dice.")
print("사다리를 만나면 앞으로 나아가고,")
print("뱀을 만나면 뒤로 돌아갑니다.")
print("")
print("----------------------------------------------------------")

while playing:
    ###console test
    
    #print()
    
    ###pygame_steps_before
    for i in range(0,5):
        if (alarm[i] > -1):
            alarm[i] -= 1
    
    ###pygame_draw
    SCREEN.fill(white)
    
    if (room == "room_main"):
        SCREEN.blit(map, [0, 0])
        SCREEN.blit(player, [player_x,player_y])
        if (dice_index == 1):
            SCREEN.blit(dice1, [dice_x, dice_y])
        elif (dice_index == 2):
            SCREEN.blit(dice2, [dice_x, dice_y])
        elif (dice_index == 3):
            SCREEN.blit(dice3, [dice_x, dice_y])
        elif (dice_index == 4):
            SCREEN.blit(dice4, [dice_x, dice_y])
        elif (dice_index == 5):
            SCREEN.blit(dice5, [dice_x, dice_y])
        elif (dice_index == 6):
            SCREEN.blit(dice6, [dice_x, dice_y])
    elif (room == "room_end"):
        SCREEN.blit(text_ending, [200, 300])
        
    pygame.display.flip()
    
    ###pygame_steps
        
    
    if (player_count > 0):
        if ((player_count-1) // 10 % 2 == 0):
            player_x = ((player_count-1)%10)*(screen_height/10)
        else:
            player_x = (9-(player_count-1)%10)*(screen_height/10)
        player_y = ((screen_height/20)*18)-(((player_count-1)%100//10)*(screen_height/10))
    else:
        player_x = screen_width-100
        player_y = 100

    if (player_count > 100 and room == "room_main"):
        room = "room_end"
        sfx_clear.set_volume(0.05)
        sfx_clear.play()
        freeze = 1
        print("----------------------------------------------------------")
        print("")
        print("clear!")
        print("총 시도 횟수 : {}회. ".format(try_count))
        print("")
        print("----------------------------------------------------------")
        
    
    ###pygame_alarms

    if (alarm[0] == 0):
        dice_index = dice()
        dice_roll -= 1
        if (dice_roll > 0):
            alarm[0] = 2
        elif (dice_roll == 0):
            dice_roll = 10
            freeze = 0
            alarm[1] = 1

    if (alarm[1] == 1): 
        a = dice()
        dice_index = a
        player_count += a

        snake_or_ladder()
        try_count += 1

        print("{}회. ".format(try_count),end=" ")
        print("주사위 값 : {},".format(a),end=" ")
        print("현재 위치 : {}".format(player_count))
    
    ###pygame_keycheck
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and freeze == 0:
            if event.key == pygame.K_SPACE:

                if (dice_roll > 0):
                    freeze = 1
                    alarm[0] = 10
                    print("주사위 굴리는 중...")
                
        if event.type == pygame.QUIT:
            playing = False

    ###pygame_steps_after

    clock.tick(60)



pygame.quit()
