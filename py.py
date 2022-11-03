import pygame,sys
from pygame.locals import *
pygame.init()
print('                                  ')
sound = pygame.mixer.Sound ('배경음.mp3')
pygame.mixer.music.set_volume(0.1)
sound.play(loops=-1)
print('                                  ')
name = input('[먼저 이름을 입력해줘!] :')
print('                                  ')
print('[', name,'!!]')
print('                                  ')
print('[고마워! 즐거운 게임 되길 바랄게 ^&^]')
print('                                  ')
w1 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
while w1 != "응" :
    print("[응이라구 적어달랬지! ㅡㅡ ]")
    print('                                  ')
    w1 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
print('                                  ')

if w1 == "응":
    print('                                  ')
 
else:
    print ("[하기 싫어?ㅠㅠ]")
    
print('*')
print('*')
print('*')
print('*')
print('*')
print('                                  ')
sound = pygame.mixer.Sound ( 'alarm.mp3' )
sound.play()


print(name, '일어나! 아빠 지금 나갈거니까 아침 알아서 챙겨 먹어!!')
print('                                  ')
print('하아아아암~','(기지개를 켜며)')
print('                                  ')
print('*')
print('*')
print('*')
print('*')
print('                                  ')
print('(오늘은 집에 아무도 없다. 나 혼자 차려 먹어야 하는데 뭐 먹지....)')
print('                                  ')
print('(냉장고를 열며)')
print('                                  ')
print('어?! 케이크다')
print('                                  ')
print('살 찌는건 싫지만 배는 채워야 되니까...')
print('                                  ')
print('케이크 두조각이 570kcal니까 딱 한조각만 먹자..!')
print('                                  ')
print('(케이크를 꺼낸다)')
print('                                  ')

#rpc
print('[',name, '다이어트 중인데 케이크 먹고싶지?]')
print('                                  ')
print('[첫끼니까 특별히 허락해주는 거야!!]')
print('                                  ')
print('[대신 퀴즈를 풀어서 280kcal에서 300kcal까지만 먹어야 해!!!]')
print('                                  ')
print('[만약 절제에 성공하면 오늘 저녁은 특식이고,')
print('                                  ')
print('실패한다면 굶기야 ㅡㅡ ]')
print('                                  ')
print('[자, 이제 먹으러 가볼까?]')
print('                                  ')
print('[다이어트 파이팅~~]')
print('                                  ')
w2 = input ("[다 읽었으면 응이라고 대답해줘!] : ")
while w2 != "응" :
    print("[응이라구 적어달랬지! ㅡㅡ ]")
    print('                                  ')
    w2 = input ("[다 읽었으면 응이라고 대답해줘!] : ")
print('                                  ')

if w2 == "응":
    print('                                  ')
 
else:
    print ("[하기 싫어?ㅠㅠ]")
print('*')
print('*')
print('*')
print('*')
print('*')
print('                                  ')

#다시 돌아와서

print('                                  ')
print('[',name,'처음은 맞춤법 퀴즈야!]')
print('                                  ')
print('[다음 문장이 맞는 문장인지 맞다 혹은 아니다로 대답해줘.]')
correct=0
print('                                  ')
q1= input ("<문제1: 학생으로써 본분을 지키기 바랍니다.> : ")

while q1 != "맞다" and q1 != "아니다":
    print("[맞다 또는 아니다만 쓰라니까ㅡㅡ. ]")
    q1 = input ("학생으로써 본분을 지키기 바랍니다. : ")
print('                                  ')
if q1 == "아니다":
    print("[정답! 이 문제는 25kcal였어!] ")
    correct += 25
  
else:
    print ("[틀렸어ㅡㅡ]")
   
print('                                  ')
score = correct * 1

print('                                  ')
print("[다음 문제로 넘어갈겡.]")
print('                                  ')
q2= input ("<문제2: 제가 원하는 사람은 당신뿐이에요.> : ")

while q2 != "맞다" and q2 != "아니다":
    print("[맞다 또는 아니다만 쓰라니까ㅡㅡ ]")
    q2 = input ("제가 원하는 사람은 당신뿐이에요. : ")

if q2 == "맞다":
    print("[정답! 이 문제는 40 kcal였어!]")
    correct += 40
   
else:
    print ("[땡!]")
    
print('                                  ')
score = correct * 1

print('                                  ')
print("[다음 문제로 넘어갈겡.]")
print('                                  ')
q3= input ("<문제3: 그렇게 살다가는 언젠가 댓가를 치르고 말 거야.> : ")

while q3 != "맞다" and q3 != "아니다":
    print("[맞다 또는 아니다만 쓰라니까ㅡㅡ]")
    q3 = input ("그렇게 살다가는 언젠가 댓가를 치르고 말 거야 . : ")

if q3 == "아니다":
    print("[정답! 이 문제는 45kcal였어!]")
    correct += 45
    
else:
    print ("[틀렸어ㅡㅡ]")
    
print('                                  ')
score = correct * 1

print('                                  ')
print("[다음 문제로 넘어갈겡.]")

print('                                  ')
q4= input ("<문제4: 우리 제안에 대해 어떻게 판단할런지 예측이 안된다.> : ")

while q4 != "맞다" and q4 != "아니다":
    print("[맞다 또는 아니다만 쓰라니까ㅡㅡ]")
    q4 = input ("우리 제안에 대해 어떻게 판단할런지 예측이 안된다 . : ")

if q4 == "아니다":
    print("[정답! 이 문제는 52kcal였어!]")
    correct += 62
   
else:
    print ("[땡!]")
    
print('                                  ')
score = correct * 1

print('                                  ')
w3 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
while w3 != "응" :
    print("[응이라구 적어달랬지! ㅡㅡ ]")
    print('                                  ')
    w3 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
print('                                  ')

if w3 == "응":
    print('                                  ')
 
else:
    print ("[하기 싫어?ㅠㅠ]")
print('*')
print('*')
print('*')
print('*')
print('*')
print('                                  ')

#넌센스
sound = pygame.mixer.Sound ( '다음 게임.mp3' )
sound.play()

print('                                  ')
print('[이번엔 넌센스 퀴즈를 줄게!]')
print('                                  ')
print('[정답을 적어줭.]')

print('                                  ')
q5= input("<문제5: 신이 화가 나면?>: ")

if q5 == "신발끈":
    print("[정답! 이 문제는 30kcal였어!]")
    correct += 30

else :
    print("[틀렸어! 정답은 신발끈이야.]")
    
print('                                  ')
score = correct * 1


print('                                  ')
print("[다음 문제로 넘어갈게.]")

print('                                  ')
q6= input("<문제6: 돼지가 방구를 끼면?>: ")

if q6 == "돈가스" or q6 == "돈까스":
    print("[정답! 이 문제는 30kcal였어!]")
    correct += 30

else :
    print("[땡~ 정답은 돈가스/돈까스였어.]")
    
print('                                  ')
score = correct * 1


print('                                  ')
print("[다음 문제야.]")
print('                                  ')
q7= input("<문제7: 바람이 귀엽게 부는 지역은?> : ")

if q7 == "분당" :
    print("[맞췄어! 이 문제는 50kcal였어!]")
    correct += 50

else :
    print("[아쉬워 ㅠㅠ. 정답은 분당이야...]")
   
print('                                  ')
score = correct * 1


print('                                  ')
print("[다음 문제 줄게.]")
print('                                  ')
q8= input("<문제8: 사람의 몸무게가 가장 많이 나갈 때는?> : ")

if q8 == "철들때" or q8 == "철들 때" or q8 == "철 들 때" :
    print("[정답!! 이 문제는 62kcal였어!]")
    correct += 62

else :
    print("[땡~~ 정답은 철들 때야!]")
   
print('                                  ')
score = correct * 1

print('                                  ')
w4 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
while w4 != "응" :
    print("[응이라구 적어달랬지! ㅡㅡ ]")
    print('                                  ')
    w4 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
print('                                  ')

if w4 == "응":
    print('                                  ')
 
else:
    print ("[하기 싫어?ㅠㅠ]")
print('*')
print('*')
print('*')
print('*')
print('*')
print('                                  ')

#구구단
sound = pygame.mixer.Sound ( '다음 게임.mp3' )
sound.play()

print('                                  ')
print('[구구단을 외자~ 이번엔 구구단 문제야!]')
print('                                  ')
print('[정답을 적어줘.]')
print('                                  ')
q9= input('<문제9: 69 X 4 = ?> : ')

if q9 == '276' :
    print('[정답!정답! 이 문제는 30kcal였어!]')
    correct += 30

else :
    print('[아쉽다 ㅠㅠ]')
   
print('                                  ')
score = correct*1

print('                                  ')

q10= input('<문제8: 48 X 6 = ?> : ')

if q10 == '288' :
    print('[잘했어! 이 문제는 30kcal였어!]')
    correct += 30

else :
    print('[땡~]')
   
print('                                  ')
score = correct*1

print('                                  ')
q11= input('<문제9: 24 X 9 = ?> : ')

if q11 == '216' :
    print('[정답 ㅎㅎ 이 문제는 50kcal였어!]')
    correct += 50

else :
    print('[틀렸어...]')
   
print('                                  ')    
score = correct*1

print('                                  ')
q12= input('<문제10: 36 X 7 = ?> : ')

if q12 == '252' :
    print('[나이스~! 정답이야. 이 문제는 62kcal였어!]')
    correct += 62

else :
    print('땡~')
   
print('                                  ')    
score = correct*1

print('                                  ')
w5 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
while w5 != "응" :
    print("[응이라구 적어달랬지! ㅡㅡ ]")
    print('                                  ')
    w5 = input ("[다음으로 넘어가고 싶으면 응이라고 대답해줘!] : ")
print('                                  ')

if w5 == "응":
    print('                                  ')
 
else:
    print ("[하기 싫어?ㅠㅠ]")
print('*')
print('*')
print('*')
print('*')
print('*')
print('                                  ')

#야구게임
sound = pygame.mixer.Sound ( '다음 게임.mp3' )
sound.play()

print('                                  ')
print('[야구게임을 시작할게. 제일 많은 칼로리를 얻을 수 있으니까 신중해야 해! 행운을 빌어!_!]')
print('                                  ')
import random
secretLen = 2


secretList = random.sample(range(10), secretLen)
secret = ''
for i in range(secretLen):
    secret += str(secretList[i])
    
for chance in range(8, 0, -1):
  while True:
   guess = input(("You have %d chance(s)."% chance) + ("[두자리수를 맞춰봐.: ] "))
   if len(guess) == secretLen and guess.isdigit():
       
      break

    
  strike = 0
  ball = 0
  
  for i in range(secretLen):
    if secret[i] == guess[i]:
       strike += 1
       
    elif secret[i] in guess:
       ball+=1
       
  print(strike, ball)
  
  if strike == secretLen:
      print('[정답이야!! 이 문제는 54kcal였어!]')
      correct += 54
      break
    
  if strike > 0:
      if ball > 0:
         print("%d strike(s) and %d ball(s)\n" % (strike,ball))
      else:
         print("%d strike(s)\n" % strike)
  else:
     if ball > 0:
        print ("%d ball(s)\n" % ball)
     else:
        print ("Out\n")
else:
  print ('[기회를 다 써버렸어...]')


print('                                  ')    
score = correct*1
print('                                            ')
w6 = input ("[결과가 궁금하다면 응이라고 대답해줘.] : ")
while w6 != "응" :
    print("[응이라구 적어달랬지! ㅡㅡ ]")
    print('                                  ')
    w6 = input ("[결과가 궁금하다면  응이라고 대답해줘.] : ")
print('                                  ')
if w6 == "응":
    print('                                  ')
 
else:
    print ("[보기 싫어?ㅠㅠ]")


print('*')
print('*')
print('*')
print('*')
print('*')
print('*')
print('*')
print('*')
print('*')
print('*')
print('*')
print('                                            ')
print("[수고했어!!", name, "네가 지금까지 먹은 케이크는", score, "kcal야.]")
print('                                            ')
#결과

if score <= 300 and score >= 280:
    print('[',name,'칼로리 잘 맞춰서 먹었넹? ㅎㅎ]')
    print('                                            ')
    print('[오늘 저녁은 맛있는 거 먹을 수 있겠당!!!  ₍˄·͈༝·͈˄₎◞ ̑̑ෆ⃛ ]')
    print('                                           ')
    print('[다음에 또 만나자, ', name, '~!]')
    
elif score >= 301 and score <= 570:
    print('[',name, '칼로리 맞춰서 먹기로 했지ㅡㅡ]')
    print('                                             ')
    print('[벌로 오늘 저녁 굶기로 약속했다, 꼭 지켜 !]')
    print('                                             ')
    print('[다음에는 꼭 성공하기다, ', name, '!!]')
    
elif score <= 279:
      print('[', name, '너 너무 조금 먹었어 ㅠㅠ]')
      print( '                                           ' )
      print('[이러다가 쓰러질지도 몰라!]')
      print('                                             ')
      print('[조금 더 먹기로 약속해,', name, 'ㅠㅡㅠ]')
      

pygame.quit()
