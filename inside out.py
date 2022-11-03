import random
import pygame
import sys
from pygame.locals import *

#버튼 그리기
def draw_btns(BUTTONS):
    for button,letter in BUTTONS:
        btn_text = btn_font.render(letter, True, BLACK)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, BLACK, button, 2)
        screen.blit(btn_text, btn_text_rect)
#화면 작성
def display_guess():
    display_word = ''

    for letter in WORD:
        if letter in GUESSED:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    text = letter_font.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))

#화면 설정
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("InSiDe OuT")

game_over = False

#색 정의하기
WHITE = (255,255,255)
BLACK = (0,0,0)

# 이미지 불러오기
IMAGES = []
hangman_satus = 0

for i in range(8):
    image = pygame.image.load(f"image/hangman{i}.png")
    IMAGES.append(image)

#타이틀 이미지 띄우기
# 게임 화면 이미지 로딩 및 크기 설정
titlescreen = pygame.image.load("TITLE.png")
titlescreen = pygame.transform.scale(titlescreen, (800, 500))
titleopen = True
while titleopen:
    # 이벤트 처리 (space 키를 눌러 설명 보기)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                titleopen = False
    # 스크린의 원하는 좌표에 이미지 복사하기
    screen.blit(titlescreen, [0, 0])
    # 작업한 스크린의 내용을 갱신하기
    pygame.display.flip()

#세계관 이미지 띄우기
# 게임 화면 이미지 로딩 및 크기 설정
worldscreen = pygame.image.load("world.png.")
worldscreen = pygame.transform.scale(worldscreen, (800, 500))
worldopen = True
while worldopen:
    # 이벤트 처리 (space 키를 눌러 설명 보기)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                worldopen = False
    # 스크린의 원하는 좌표에 이미지 복사하기
    screen.blit(worldscreen, [0, 0])
    # 작업한 스크린의 내용을 갱신하기
    pygame.display.flip()

#설명 이미지 띄우기
#게임 설명 이미지 로딩 및 크기 설정
explanescreen = pygame.image.load("explane.jpg")
explanescreen = pygame.transform.scale(explanescreen, (800, 500))
explaneopen = True
while explaneopen:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                explaneopen = False
    # 스크린의 원하는 좌표에 이미지 복사하기
    screen.blit(explanescreen, [0, 0])
    # 작업한 스크린의 내용을 갱신하기
    pygame.display.flip()

#버튼 설정하기
ROWS = 2
COLS = 13
GAP = 20
SIZE = 40
BOXES = []

for row in range(ROWS):
    for col in range(COLS):
        x = ((GAP * col) + GAP) + (SIZE * col)
        y = ((GAP * row) + GAP) + (SIZE * row) + 330
        box = pygame.Rect(x,y,SIZE,SIZE)
        BOXES.append(box)

A = 65
BUTTONS = []

for ind, box in enumerate(BOXES):
    letter = chr(A+ind)
    button = ([box, letter])
    BUTTONS.append(button)

#폰트 지정
btn_font = pygame.font.SysFont('Arial', 30)
letter_font = pygame.font.SysFont('Arial', 60)
game_font = pygame.font.SysFont('Jokerman', 20)

#무작위 감정 WORD DATABASE
WORD=['SAD', 'UPSET', 'AFRAID', 'EXITED', 'AMAZED']
WORD = random.choice(WORD)
GUESSED = []

#제목 글씨, 폰트 설정
title = "INSIDE OUT!"
title_text = game_font.render(title, True, BLACK)
title_text_rect = title_text.get_rect(topright=(780,10))

#게임 실행 코드
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            clicked_pos = event.pos

            for button, letter in BUTTONS:
                if button.collidepoint(clicked_pos):
                    GUESSED.append(letter)

                    if letter not in WORD:
                        hangman_satus += 1

                    if hangman_satus == 8:
                        game_over = True

                    BUTTONS.remove([button, letter])

    BBGG=pygame.display.set_mode((800,500))
    BAGR=pygame.image.load("BACKGROUND.jpg")   #<< 사진배경
    BBGG.blit(BAGR, (0, 0))
    screen.blit(IMAGES[hangman_satus], (40, 10))
    screen.blit(title_text, title_text_rect)
    draw_btns(BUTTONS)
    display_guess()

    won = True

    for letter in WORD:
        if letter not in GUESSED:
            won = False
    if won:
        game_over = True
        WIN=pygame.display.set_mode((800,500))
        WINSCREEN=pygame.image.load("ENDING.jpg.")
        WIN.blit(WINSCREEN,(0,0))

    pygame.display.update()

    if game_over:
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()