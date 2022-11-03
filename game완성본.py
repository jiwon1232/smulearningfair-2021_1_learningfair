import os
print ('제로게임을 시작합니다')
def rule ():
    print('')
    print('[규칙설명]')
    print('1. 플레이어와 봇은 0,1,2,3,4 중 숫자를 차례대로 말합니다')
    print('2. 그 후 각자 0,1,2 중 숫자를 정합니다')
    print('3. 두번째로 정한 서로의 숫자 합을 구합니다')
    print('4. 첫번째 숫자와 숫자합이 일치한 플레이어가 승리합니다')
    print('')

def play() :
 import random

 while True:
  try :
   number1 = int(input('0부터 4 사이의 숫자를 입력하세요 : '))
   if number1 >= 5 or number1 < 0 :
    print('범위 밖  숫자입니다.')
    continue  
   else :
       print('')
       print('당신의 첫번째 숫자는', number1, '입니다.')       
   break
  except ValueError :
      print('입력값이 숫자가 아닙니다.')

 botnumber1 = random.randrange(0 , 5)
 while botnumber1 != number1 :
     random.randrange(0 , 5)
     break
    
 print('')

 while True:
  number2 = int(input('0부터 2사이의 숫자를 입력하세요 : '))
  if number2 >2 or number2 < 0 :
   print('범위 밖 숫자입니다.')
   continue
  if number2 <= 2 and number2 >= 0 :
      print('')
      print('당신의 두번째 숫자는', number2, '입니다')
      break

 botnumber2 = random.randrange(0 , 3)
 print('봇의 두번째 숫자는', botnumber2, '입니다')


 an = int(number2 + botnumber2)
 print('두 숫자의 합은' , an, '입니다')
 print('')
 print('당신의 첫번째 숫자는', number1, '이었습니다.')
 print('봇의 첫번째 숫자는', botnumber1, '이었습니다.')
 print('')

 if an == number1 and an != botnumber1 :
     print('당신의 승리입니다.')
 elif an != number1 and an == botnumber1 :
     print('당신의 패배입니다.')
 elif an != number1 and an != botnumber1 :
     print('둘 모두 맞추지 못했습니다.'
           '무승부입니다.')
 elif an == number1 and an == botnumber1 :
     print('둘 모두 맞추었습니다.'
           '무승부입니다.')
 print('')
def end() :    
 print('다시 시작하시겠습니까?')
 print('')
 while True :
  x = str(input('설명을 다시 보려면 rule을 입력하세요.\n'
               '다시 시작하려면 y를 눌러주세요.\n'
               '게임을 종료하려면 n을 눌러주세요.\n :'))
  if x == str('y') :
      print('다시 시작합니다.')
      play()
  elif x == str('n') :
      print('플레이 해 주셔서 감사합니다.')
      print('창을 닫으시려면 아무 버튼이나 누르십시오...')
      input()
      break
  elif x == str('rule') :
     rule()
     end()
  else :
      continue

rule()
play()
end()



