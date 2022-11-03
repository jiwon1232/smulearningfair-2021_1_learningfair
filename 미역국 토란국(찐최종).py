print(" [경고]\n 이 게임을 플레이에 앞서..")
import time
time.sleep(1)
print(" 꼭! 전체화면으로 플레이 해주시기 바랍니다!!!")
import time
time.sleep(3)
print(" \n \n \n \n \n")
import time
time.sleep(1)
print(" [시스템] \n 게임의 난이도 설정입니다.")
import time
time.sleep(1)
print(" 게임의 난이도는 게임 이벤트의 빈도와 강도를 뜻하며") 
import time
time.sleep(1)
print(" 난이도는 무작위로 설정됩니다.")
import random
Len5 = 1
List5 = random.sample(range(3), Len5)
secret5 = ''
for i in range(Len5):
    secret5 += str(List5[i])
if secret5 == "0":
    import time
    time.sleep(1)
    print(" 랜덤 중..")
    import time
    time.sleep(3)
    print(" 이번 게임의 난이도는 하입니다.")
if secret5 == "1":
    import time
    time.sleep(1)
    print ("랜덤 중..")
    import time
    time.sleep(3)
    print(" [시스템]\n 이번 게임의 난이도는 중입니다.")
if secret5 == "2":
    import time
    time.sleep(1)
    print ("랜덤 중..")
    import time
    time.sleep(3)
    print(" [시스템]\n 이번 게임의 난이도는 상입니다.")
import time
time.sleep(1)
print(" \n \n \n \n \n")
import time
time.sleep(1)
print("미역국 vs 토란국 \n")
import time
time.sleep(1)
사회자= str("상명대")
print(사회자+": 안녕하세요.")
import time
time.sleep(1)
print(사회자+": 저는 이 게임의 사회자 "+사회자+"입니다.")
import time
time.sleep(1)
username = str(input("\n 당신의 닉네임을 알려주세요: "))
if username == "알고리즘과게임콘텐츠":
    print("\n \n [이스터에그]")
    import time
    time.sleep(1)
    print(" made by 간호학과")
    import time
    time.sleep(1)
    print(" 202220854 김주환")
    import time
    time.sleep(1)
    print(" 202220870 안원민")
    import time
    time.sleep(1)
    print(" 202220891 정민석")
    import time
    time.sleep(1)
    print(" 202220892 정의찬")
import time
time.sleep(0.75)
print("\n \n"+사회자+": "+username+"님 반가워요.")
import time
time.sleep(1)
print(사회자+": 먼저 "+username+"님이 이끌어갈 국가를 선택하셔야 합니다.")
import time
time.sleep(1)
print(사회자+": 국가 종류에는 미역국과 토란국이 있습니다.")
import time
time.sleep(1)
print(사회자+": 미역국은 막대한 부자들이 많아 부유한 자본이 바탕인 국가 입니다.")
import time
time.sleep(1)
print(사회자+": 하지만 군사를 늘리면 반발이 심한 점을 유의하십시오.")
import time
time.sleep(1)
print(사회자+": 토란국은 막대한 군사력을 바탕으로 하고 있습니다.")
import time
time.sleep(1)
print(사회자+": 세금을 징수해도 많은 돈을 못 모으지만 한 번에 군사력이 많이 증가하게 됩니다.")
import time
time.sleep(3)
while True:
    n1 = str(input("\n"+사회자+": 국가를 선택해주세요. \n 1. 미역국 \n 2. 토란국 \n \n"))
    if n1 != "미역국" and n1 != "토란국" and n1 != "1" and n1 != "2":
        print(사회자+": 그건 어떤 국가야? 미래에서 왔어??")
    if n1 == "미역국" or n1 == "1":
        print(사회자+": 미역국을 선택하셨군요.")
        break
    if n1 == "토란국" or n1 == "2":
        print(사회자+": 토란국을 선택하셨군요.")
        break
import time
time.sleep(1)
print(사회자+": 훌륭한 선택이십니다. \n")
import time
time.sleep(1)
if n1 == "미역국" or n1 == "1":
    print(" [시스템]\n "+username+"님 당신은 미역국의 지도자입니다.")
    import time
    time.sleep(1)
    print(" 여러 가지 게임 요소를 활용하여 상대국인 토란국을 정복해봅시다.")
if n1 == "토란국" or n1 == "2":
    print(" [시스템]\n "+username+"님 당신은 토란국의 지도자입니다.")
    import time
    time.sleep(1)
    print(" 여러 가지 게임 요소를 활용하여 상대국인 미역국을 정복해봅시다.")
import time
time.sleep(1)
print("--------------------------------------------------------------------------------\n")
import time
time.sleep(1)
while True:
    print(" [시스템]\n 게임의 룰에 대한 설명입니다.")
    import time
    time.sleep(1)
    n0 = str(input(" 룰의 설명을 듣겠습니까?. \n  1. 룰의 설명 듣기. \n  2. 룰의 설명 건너뛰기. \n \n "))
    if n0 != "룰의 설명 듣기." and n0 != "룰의 설명 건너뛰기." and n0 != "1" and n0 != "2":
        print(" [시스템]\n 다시 선택해 주세요")
    if n0 == "룰의 설명을 건너 뜁니다." or n0 == "2":
        print(" [시스템]\n 룰의 설명을 건너 뜁니다.\n \n \n")
        import time
        time.sleep(1)
        break
    if n0 == "룰의 설명 듣기." or n0 == "1":
        print("비서: 이 국가를 이끌어 가기 전에 몇가지 설명을 해줄게요.")
        import time
        time.sleep(1)
        if n1 == "미역국" or n1 == "1":
            print("비서: 토란국은 우리 미역국 빼고 모든 국가를 정복 했어요.")
        if n1 == "토란국" or n1 == "2":
            print("비서: 미역국은 우리 토란국 빼고 모든 국가를 정복 했어요.")
        import time
        time.sleep(1)
        print("비서: 이젠 우리 국가만을 남기고 있는 상황이에요.")
        import time
        time.sleep(1)
        print("비서: 이런 혼란 속에서 "+username+"님이 지도자가 되셨구요.")
        import time
        time.sleep(1)
        print("비서: 걱정 마세요. 저가 도와 드릴게요.")
        import time
        time.sleep(1)
        print("비서: 국가 운영에 있어 필요한 3가지를 알려드릴게요")
        import time
        time.sleep(1)
        print("비서: 먼저 세금 징수가 있습니다.")
        import time
        time.sleep(1)
        print("비서: 세금을 징수하여 국가의 예산을 늘릴 수 있습니다.")
        import time
        time.sleep(1)
        print("비서: 하지만 과다한 세금 징수는 오히려 민심이 떨어져 반란이 일어날 수 있습니다.")
        import time
        time.sleep(1)
        if n1 == "미역국" or n1 == "1":
            print("비서: 우리 미역국같은 경우 세금을 징수하면 한 번에 많은 국가 예산을 늘릴 수가 있어요.")
            import time
            time.sleep(1)
        print("비서: 두 번째로는 사회복지 시설 건축이 있습니다.")
        import time
        time.sleep(1)
        print("비서: 사회복지 시설을 건축함으로서 세금 징수로 인한 민심을 회복할 수 있습니다.")
        import time
        time.sleep(1)
        print("비서: 마지막으로는 군사력을 증강 시킬 수 있습니다.")
        import time
        time.sleep(1)
        print("비서: 군사력은 인구수에 비례해서 증가합니다.")
        import time
        time.sleep(1)
        print("비서: 인구수 관리에 유의하세요.")
        import time
        time.sleep(1)
        print("비서: 국가 예산을 사용하여 군사력을 늘려 강대한 국가를 만들 수 있습니다.")
        import time
        time.sleep(1)
        print("비서: 하지만 군사력을 과하게 늘리면 국민들이 힘들어해 민심이 줄어들 수 있습니다.")
        import time
        time.sleep(1)
        if n1 == "미역국" or n1 == "1":
            print("비서: 민심과 상대국을 조심하며, 토란국을 무찔러 봅시다.\n \n")
        if n1 == "토란국" or n1 == "2":
            print("비서: 민심과 상대국을 조심하며, 미역국을 무찔러 봅시다.\n \n")
        import time
        time.sleep(3)
        break
    
if secret5 == "0":
    예산 = 10000
    인구수 = 100000
    인구수2 = 100000
    군사력 = 100
    군사력2 = 100
    민심 = 100
    상대국군사력 = 2000
    이벤트 = 404
    print("국가의 정보입니다.\n 예산: 10000\n 인구수: 100000\n 군사력: 100\n 민심: 100\n 상대국군사력: 2000\n")
    import time
    time.sleep(1)
    print(" [경고]\n "+사회자+": 이제부터는 선택지가 나옵니다.")
    import time
    time.sleep(1)
    print(" "+사회자+": 상황에 맞게 적절한 선택지를 선택하여 플레이를 하시기 바랍니다.\n")
    import time
    time.sleep(1)
    print("이제 지도자로서 국가를 운영해 주세요.")
    import time
    time.sleep(3)
    while True:
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        import time
        time.sleep(2)
        if 이벤트 == int("777"):
            import random
            Len = 1
            List = random.sample(range(18), Len)
            secret = ''
            for i in range(Len):
                secret += str(List[i])
            if secret == "1":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국의 군대가 기습을 했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 토란국의 군대가 무고한 우리의 백성들을 죽였습니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 감소합니다.\n")
                    인구수 = 인구수 - 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                    if 인구수 <= 0:
                        인구수 = 0
                        print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                        import time
                        time.sleep(2)
                        print(" 더 이상 국가를 운영할 수 없습니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Lose")
                        break
                    if 인구수 <= 40000:
                        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
                        import time
                        time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국의 군대가 기습을 했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 미역국의 군대가 무고한 우리의 백성들을 죽였습니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 감소합니다.\n")
                    인구수 = 인구수 - 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                    if 인구수 <= 0:
                        print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                        import time
                        time.sleep(2)
                        print(" 더 이상 국가를 운영할 수 없습니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Lose")
                        break
                    if 인구수 <= 40000:
                        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
                        import time
                        time.sleep(2)
            if secret == "4":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국 지도자에 대한 불만을 가진 자들이 귀화하였습니다!\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 증가합니다.\n")
                    인구수 = 인구수 + 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(+10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국 지도자에 대한 불만을 가진 자들이 귀화하였습니다!\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 증가합니다.\n")
                    인구수 = 인구수 + 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(+10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
            if secret == "7":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국으로 보낸 정찰병이 정보를 입수했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 토란국의 군사력이 증가했다고 합니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 상대국군사력이 100 증가합니다.\n")
                    상대국군사력 = 상대국군사력 + 100
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"(+100)\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국으로 보낸 정찰병이 정보를 입수했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 미역국의 군사력이 증가했다고 합니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 상대국군사력이 100 증가합니다.\n")
                    상대국군사력 = 상대국군사력 + 100
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"(+100)\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
        if n1 == "미역국" or n1 == "1":
            이벤트 = 777
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5 + 50000)+")\n 2. 사회복지 시설 건축(사용 예산: "+str(인구수 * 0.5)+")\n 3. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 4. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "토란국" or n1 == "2":
            이벤트 = 777
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5)+")\n 2. 사회복지 시설 건축(사용 예산: "+str(인구수 * 0.5)+")\n 3. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 4. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "미역국" or n1 == "1":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5 + 50000
                민심 = 민심 - 10
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심)+"(-10)")
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                if 민심 < 20:
                    print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                    import time
                    time.sleep(2)
                    print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                    import time
                    time.sleep(2)
                    print("비서: 어떻게 하실껀가요??\n")
                    import time
                    time.sleep(2)
                    n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                    if n3 == "1":
                        print(username+": 죄송합니다. 정말 죄송합니다..")
                        import time
                        time.sleep(2)
                        if n1 == "미역국" or n1 == "1":
                            print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        if n1 == "토란국" or n1 == "2":
                            print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Die")
                        break
                    if n3 == "2":
                        print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                        n5 = str("play")
                        import time
                        time.sleep(2)
                        break
                if 민심 < 50:
                    print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "미역국" or n1 == "1":
            if n2 == "2":
                if 예산 < 인구수 * 0.5:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 0.5:
                    민심 = 민심 + 20
                    if 민심 >= 300:
                        민심 = 300
                        print("\n비서: 민심이 최고치로 올랐습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 모든 국민이 "+username+"님을 숭배하고 찬양하기 시작했습니다.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님은 이제 이 나라의 신과 같은 존재가 됩니다.")
                        import time
                        time.sleep(2)
                        print("비서: 더이상 민심이 떨어지지 않습니다.\n")
                        n5 = str("God")
                        break
                    print("\n비서: 알겠습니다. 일꾼들에게 사회복지 시설을 건축하라 시키겠습니다.")
                    예산 = 예산 - 인구수 * 0.5
                    if 민심 >= 250:
                        print("비서: 민심의 최대치는 300입니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심)+"(+20)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "미역국" or n1 == "1":
            if n2 == "3":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.002
                    민심 = 민심 - 15
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.002)+")")
                    print("민심: "+str(민심)+"(-15)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.002
                    import time
                    time.sleep(2)
                    if 민심 < 20:
                        print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 어떻게 하실껀가요??\n")
                        import time
                        time.sleep(2)
                        n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                        if n3 == "1":
                            print(username+": 죄송합니다. 정말 죄송합니다..")
                            import time
                            time.sleep(2)
                            if n1 == "미역국" or n1 == "1":
                                print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            if n1 == "토란국" or n1 == "2":
                                print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            print(" 당신의 패배입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n YOU LOSE  ")
                            n5 = str("Die")
                            break
                        if n3 == "2":
                            print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                            n5 = str("play")
                            import time
                            time.sleep(2)
                            break
                    if 민심 < 50:
                        print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                        import time
                        time.sleep(2)
                        continue
            if n2 == "4":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                        if 군사력 > 상대국군사력:
                            print("[시스템]\n "+username+"은(는) 드디어 토란국을 정복했다.")
                            import time
                            time.sleep(2)
                            print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                            import time
                            time.sleep(2)
                            print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                            import time
                            time.sleep(2)
                            print(" 당신의 승리입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            n5 = str("You Victory")
                            print("\n \n \n \n \n You Victory  ")
                            break
        if n1 == "토란국" or n1 == "2":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5
                민심 = 민심 - 10
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심)+"(-10)")
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                if 민심 < 20:
                    print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                    import time
                    time.sleep(2)
                    print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                    import time
                    time.sleep(2)
                    print("비서: 어떻게 하실껀가요??\n")
                    import time
                    time.sleep(2)
                    n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                    if n3 == "1":
                        print(username+": 죄송합니다. 정말 죄송합니다..")
                        import time
                        time.sleep(2)
                        if n1 == "미역국" or n1 == "1":
                            print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        if n1 == "토란국" or n1 == "2":
                            print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Die")
                        break
                    if n3 == "2":
                        print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                        n5 = str("play")
                        import time
                        time.sleep(2)
                        break
                if 민심 < 50:
                    print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "토란국" or n1 == "2":
            if n2 == "2":
                if 예산 < 인구수 * 0.5:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 0.5:
                    민심 = 민심 + 20
                    if 민심 >= 300:
                        민심 = 300
                        print("\n비서: 민심이 최고치로 올랐습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 모든 국민이 "+username+"님을 숭배하고 찬양하기 시작했습니다.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님은 이제 이 나라의 신과 같은 존재가 됩니다.")
                        import time
                        time.sleep(2)
                        print("비서: 더이상 민심이 떨어지지 않습니다.\n")
                        n5 = str("God")
                        break
                    print("\n비서: 알겠습니다. 일꾼들에게 사회복지 시설을 건축하라 시키겠습니다.")
                    예산 = 예산 - 인구수 * 0.5
                    if 민심 >= 250:
                        print("비서: 민심의 최대치는 300입니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심)+"(+20)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "토란국" or n1 == "2":
            if n2 == "3":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.0033
                    민심 = 민심 - 10
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.0033)+")")
                    print("민심: "+str(민심)+"(-10)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.0033
                    import time
                    time.sleep(2)
                    if 민심 < 20:
                        print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 어떻게 하실껀가요??\n")
                        import time
                        time.sleep(2)
                        n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                        if n3 == "1":
                            print(username+": 죄송합니다. 정말 죄송합니다..")
                            import time
                            time.sleep(2)
                            if n1 == "미역국" or n1 == "1":
                                print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            if n1 == "토란국" or n1 == "2":
                                print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            print(" 당신의 패배입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n YOU LOSE  ")
                            n5 = str("Die")
                            break
                        if n3 == "2":
                            print(username+": 나의 군사력을 동원해 반란자들을 처단하라!! ")
                            n5 = str("play")
                            import time
                            time.sleep(2)
                            break
                    if 민심 < 50:
                        print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                        import time
                        time.sleep(2)
                        continue
            if n2 == "4":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                    if 군사력 > 상대국군사력:
                        print("[시스템]\n "+username+"은(는) 드디어 미역국을 정복했다.")
                        print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                        import time
                        time.sleep(2)
                        print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                        import time
                        time.sleep(2)
                        print(" 당신의 승리입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        n5 = str("You Victory")
                        print("\n \n \n \n \n You Victory  ")
                        break
                    
if secret5 == "1":
    예산 = 5000
    인구수 = 100000
    인구수2 = 100000
    군사력 = 100
    군사력2 = 100
    민심 = 100
    상대국군사력 = 2000
    이벤트 = 404
    print("국가의 정보입니다.\n 예산: 5000\n 인구수: 100000\n 군사력: 100\n 민심: 100\n 상대국군사력: 2000\n")
    import time
    time.sleep(1)
    print(" [경고]\n "+사회자+": 이제부터는 선택지가 나옵니다.")
    import time
    time.sleep(1)
    print(" "+사회자+": 상황에 맞게 적절한 선택지를 선택하여 플레이를 하시기 바랍니다.\n")
    import time
    time.sleep(1)
    print("이제 지도자로서 국가를 운영해 주세요.")
    import time
    time.sleep(3)
    while True:
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        import time
        time.sleep(2)
        if 이벤트 == int("777"):
            import random
            Len = 1
            List = random.sample(range(12), Len)
            secret = ''
            for i in range(Len):
                secret += str(List[i])
            if secret == "1":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국의 군대가 기습을 했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 토란국의 군대가 무고한 우리의 백성들을 죽였습니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 15000 감소합니다.\n")
                    인구수 = 인구수 - 15000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-15000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                    if 인구수 <= 0:
                        인구수 = 0
                        print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                        import time
                        time.sleep(2)
                        print(" 더 이상 국가를 운영할 수 없습니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Lose")
                        break
                    if 인구수 <= 40000:
                        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
                        import time
                        time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국의 군대가 기습을 했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 미역국의 군대가 무고한 우리의 백성들을 죽였습니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 15000 감소합니다.\n")
                    인구수 = 인구수 - 15000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-15000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                    if 인구수 <= 0:
                        print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                        import time
                        time.sleep(2)
                        print(" 더 이상 국가를 운영할 수 없습니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Lose")
                        break
                    if 인구수 <= 40000:
                        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
                        import time
                        time.sleep(2)
            if secret == "4":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국 지도자에 대한 불만을 가진 자들이 귀화하였습니다!\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 증가합니다.\n")
                    인구수 = 인구수 + 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(+10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국 지도자에 대한 불만을 가진 자들이 귀화하였습니다!\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 증가합니다.\n")
                    인구수 = 인구수 + 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(+10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
            if secret == "7":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국으로 보낸 정찰병이 정보를 입수했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 토란국의 군사력이 증가했다고 합니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 상대국군사력이 200 증가합니다.\n")
                    상대국군사력 = 상대국군사력 + 200
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"(+200)\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국으로 보낸 정찰병이 정보를 입수했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 미역국의 군사력이 증가했다고 합니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 상대국군사력이 200 증가합니다.\n")
                    상대국군사력 = 상대국군사력 + 200
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"(+200)\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
        if n1 == "미역국" or n1 == "1":
            이벤트 = 777
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5 + 50000)+")\n 2. 사회복지 시설 건축(사용 예산: "+str(인구수 * 0.5)+")\n 3. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 4. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "토란국" or n1 == "2":
            이벤트 = 777
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5)+")\n 2. 사회복지 시설 건축(사용 예산: "+str(인구수 * 0.5)+")\n 3. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 4. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "미역국" or n1 == "1":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5 + 50000
                민심 = 민심 - 10
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심)+"(-10)")
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                if 민심 < 20:
                    print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                    import time
                    time.sleep(2)
                    print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                    import time
                    time.sleep(2)
                    print("비서: 어떻게 하실껀가요??\n")
                    import time
                    time.sleep(2)
                    n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                    if n3 == "1":
                        print(username+": 죄송합니다. 정말 죄송합니다..")
                        import time
                        time.sleep(2)
                        if n1 == "미역국" or n1 == "1":
                            print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        if n1 == "토란국" or n1 == "2":
                            print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Die")
                        break
                    if n3 == "2":
                        print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                        n5 = str("play")
                        import time
                        time.sleep(2)
                        break
                if 민심 < 50:
                    print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "미역국" or n1 == "1":
            if n2 == "2":
                if 예산 < 인구수 * 0.5:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 0.5:
                    민심 = 민심 + 20
                    if 민심 >= 300:
                        민심 = 300
                        print("\n비서: 민심이 최고치로 올랐습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 모든 국민이 "+username+"님을 숭배하고 찬양하기 시작했습니다.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님은 이제 이 나라의 신과 같은 존재가 됩니다.")
                        import time
                        time.sleep(2)
                        print("비서: 더이상 민심이 떨어지지 않습니다.\n")
                        n5 = str("God")
                        break
                    print("\n비서: 알겠습니다. 일꾼들에게 사회복지 시설을 건축하라 시키겠습니다.")
                    예산 = 예산 - 인구수 * 0.5
                    if 민심 >= 250:
                        print("비서: 민심의 최대치는 300입니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심)+"(+20)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "미역국" or n1 == "1":
            if n2 == "3":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.002
                    민심 = 민심 - 15
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.002)+")")
                    print("민심: "+str(민심)+"(-15)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.002
                    import time
                    time.sleep(2)
                    if 민심 < 20:
                        print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 어떻게 하실껀가요??\n")
                        import time
                        time.sleep(2)
                        n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                        if n3 == "1":
                            print(username+": 죄송합니다. 정말 죄송합니다..")
                            import time
                            time.sleep(2)
                            if n1 == "미역국" or n1 == "1":
                                print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            if n1 == "토란국" or n1 == "2":
                                print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            print(" 당신의 패배입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n YOU LOSE  ")
                            n5 = str("Die")
                            break
                        if n3 == "2":
                            print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                            n5 = str("play")
                            import time
                            time.sleep(2)
                            break
                    if 민심 < 50:
                        print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                        import time
                        time.sleep(2)
                        continue
            if n2 == "4":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                        if 군사력 > 상대국군사력:
                            print("[시스템]\n "+username+"은(는) 드디어 토란국을 정복했다.")
                            import time
                            time.sleep(2)
                            print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                            import time
                            time.sleep(2)
                            print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                            import time
                            time.sleep(2)
                            print(" 당신의 승리입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            n5 = str("You Victory")
                            print("\n \n \n \n \n You Victory  ")
                            break
        if n1 == "토란국" or n1 == "2":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5
                민심 = 민심 - 10
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심)+"(-10)")
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                if 민심 < 20:
                    print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                    import time
                    time.sleep(2)
                    print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                    import time
                    time.sleep(2)
                    print("비서: 어떻게 하실껀가요??\n")
                    import time
                    time.sleep(2)
                    n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                    if n3 == "1":
                        print(username+": 죄송합니다. 정말 죄송합니다..")
                        import time
                        time.sleep(2)
                        if n1 == "미역국" or n1 == "1":
                            print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        if n1 == "토란국" or n1 == "2":
                            print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Die")
                        break
                    if n3 == "2":
                        print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                        n5 = str("play")
                        import time
                        time.sleep(2)
                        break
                if 민심 < 50:
                    print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "토란국" or n1 == "2":
            if n2 == "2":
                if 예산 < 인구수 * 0.5:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 0.5:
                    민심 = 민심 + 20
                    if 민심 >= 300:
                        민심 = 300
                        print("\n비서: 민심이 최고치로 올랐습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 모든 국민이 "+username+"님을 숭배하고 찬양하기 시작했습니다.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님은 이제 이 나라의 신과 같은 존재가 됩니다.")
                        import time
                        time.sleep(2)
                        print("비서: 더이상 민심이 떨어지지 않습니다.\n")
                        n5 = str("God")
                        break
                    print("\n비서: 알겠습니다. 일꾼들에게 사회복지 시설을 건축하라 시키겠습니다.")
                    예산 = 예산 - 인구수 * 0.5
                    if 민심 >= 250:
                        print("비서: 민심의 최대치는 300입니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심)+"(+20)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "토란국" or n1 == "2":
            if n2 == "3":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.0033
                    민심 = 민심 - 10
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.0033)+")")
                    print("민심: "+str(민심)+"(-10)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.0033
                    import time
                    time.sleep(2)
                    if 민심 < 20:
                        print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 어떻게 하실껀가요??\n")
                        import time
                        time.sleep(2)
                        n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                        if n3 == "1":
                            print(username+": 죄송합니다. 정말 죄송합니다..")
                            import time
                            time.sleep(2)
                            if n1 == "미역국" or n1 == "1":
                                print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            if n1 == "토란국" or n1 == "2":
                                print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            print(" 당신의 패배입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n YOU LOSE  ")
                            n5 = str("Die")
                            break
                        if n3 == "2":
                            print(username+": 나의 군사력을 동원해 반란자들을 처단하라!! ")
                            n5 = str("play")
                            import time
                            time.sleep(2)
                            break
                    if 민심 < 50:
                        print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                        import time
                        time.sleep(2)
                        continue
            if n2 == "4":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                    if 군사력 > 상대국군사력:
                        print("[시스템]\n "+username+"은(는) 드디어 미역국을 정복했다.")
                        print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                        import time
                        time.sleep(2)
                        print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                        import time
                        time.sleep(2)
                        print(" 당신의 승리입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        n5 = str("You Victory")
                        print("\n \n \n \n \n You Victory  ")
                        break

if secret5 == "2":
    예산 = 5000
    인구수 = 100000
    인구수2 = 100000
    군사력 = 100
    군사력2 = 100
    민심 = 100
    상대국군사력 = 2000
    이벤트 = 404
    print("국가의 정보입니다.\n 예산: 5000\n 인구수: 100000\n 군사력: 100\n 민심: 100\n 상대국군사력: 2000\n")
    import time
    time.sleep(1)
    print(" [경고]\n "+사회자+": 이제부터는 선택지가 나옵니다.")
    import time
    time.sleep(1)
    print(" "+사회자+": 상황에 맞게 적절한 선택지를 선택하여 플레이를 하시기 바랍니다.\n")
    import time
    time.sleep(1)
    print("이제 지도자로서 국가를 운영해 주세요.")
    import time
    time.sleep(3)
    while True:
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        import time
        time.sleep(2)
        if 이벤트 == int("777"):
            import random
            Len = 1
            List = random.sample(range(9), Len)
            secret = ''
            for i in range(Len):
                secret += str(List[i])
            if secret == "1":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국의 군대가 기습을 했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 토란국의 군대가 무고한 우리의 백성들을 죽였습니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 20000 감소합니다.\n")
                    인구수 = 인구수 - 20000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-20000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                    if 인구수 <= 0:
                        인구수 = 0
                        print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                        import time
                        time.sleep(2)
                        print(" 더 이상 국가를 운영할 수 없습니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Lose")
                        break
                    if 인구수 <= 40000:
                        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
                        import time
                        time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국의 군대가 기습을 했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 미역국의 군대가 무고한 우리의 백성들을 죽였습니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 20000 감소합니다.\n")
                    인구수 = 인구수 - 20000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-20000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                    if 인구수 <= 0:
                        print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                        import time
                        time.sleep(2)
                        print(" 더 이상 국가를 운영할 수 없습니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Lose")
                        break
                    if 인구수 <= 40000:
                        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
                        import time
                        time.sleep(2)
            if secret == "4":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국 지도자에 대한 불만을 가진 자들이 귀화하였습니다!\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 증가합니다.\n")
                    인구수 = 인구수 + 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(+10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국 지도자에 대한 불만을 가진 자들이 귀화하였습니다!\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 인구수가 10000 증가합니다.\n")
                    인구수 = 인구수 + 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(+10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
            if secret == "7":
                if n1 == "미역국" or n1 == "1":
                    print("비서: 토란국으로 보낸 정찰병이 정보를 입수했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 토란국의 군사력이 증가했다고 합니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 상대국군사력이 300 증가합니다.\n")
                    상대국군사력 = 상대국군사력 + 300
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"(+300)\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
                if n1 == "토란국" or n1 == "2":
                    print("비서: 미역국으로 보낸 정찰병이 정보를 입수했습니다!")
                    import time
                    time.sleep(2)
                    print("비서: 미역국의 군사력이 증가했다고 합니다.\n")
                    import time
                    time.sleep(2)
                    print(" [시스템]\n 상대국군사력이 300 증가합니다.\n")
                    상대국군사력 = 상대국군사력 + 300
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"(+300)\n \n \n \n \n")
                    import time
                    time.sleep(2)
                    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    import time
                    time.sleep(2)
        if n1 == "미역국" or n1 == "1":
            이벤트 = 777
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5 + 50000)+")\n 2. 사회복지 시설 건축(사용 예산: "+str(인구수 * 0.5)+")\n 3. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 4. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "토란국" or n1 == "2":
            이벤트 = 777
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5)+")\n 2. 사회복지 시설 건축(사용 예산: "+str(인구수 * 0.5)+")\n 3. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 4. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "미역국" or n1 == "1":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5 + 50000
                민심 = 민심 - 10
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심)+"(-10)")
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                if 민심 < 20:
                    print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                    import time
                    time.sleep(2)
                    print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                    import time
                    time.sleep(2)
                    print("비서: 어떻게 하실껀가요??\n")
                    import time
                    time.sleep(2)
                    n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                    if n3 == "1":
                        print(username+": 죄송합니다. 정말 죄송합니다..")
                        import time
                        time.sleep(2)
                        if n1 == "미역국" or n1 == "1":
                            print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        if n1 == "토란국" or n1 == "2":
                            print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Die")
                        break
                    if n3 == "2":
                        print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                        n5 = str("play")
                        import time
                        time.sleep(2)
                        break
                if 민심 < 50:
                    print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "미역국" or n1 == "1":
            if n2 == "2":
                if 예산 < 인구수 * 0.5:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 0.5:
                    민심 = 민심 + 20
                    if 민심 >= 300:
                        민심 = 300
                        print("\n비서: 민심이 최고치로 올랐습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 모든 국민이 "+username+"님을 숭배하고 찬양하기 시작했습니다.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님은 이제 이 나라의 신과 같은 존재가 됩니다.")
                        import time
                        time.sleep(2)
                        print("비서: 더이상 민심이 떨어지지 않습니다.\n")
                        n5 = str("God")
                        break
                    print("\n비서: 알겠습니다. 일꾼들에게 사회복지 시설을 건축하라 시키겠습니다.")
                    예산 = 예산 - 인구수 * 0.5
                    if 민심 >= 250:
                        print("비서: 민심의 최대치는 300입니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심)+"(+20)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "미역국" or n1 == "1":
            if n2 == "3":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.002
                    민심 = 민심 - 15
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.002)+")")
                    print("민심: "+str(민심)+"(-15)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.002
                    import time
                    time.sleep(2)
                    if 민심 < 20:
                        print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 어떻게 하실껀가요??\n")
                        import time
                        time.sleep(2)
                        n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                        if n3 == "1":
                            print(username+": 죄송합니다. 정말 죄송합니다..")
                            import time
                            time.sleep(2)
                            if n1 == "미역국" or n1 == "1":
                                print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            if n1 == "토란국" or n1 == "2":
                                print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            print(" 당신의 패배입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n YOU LOSE  ")
                            n5 = str("Die")
                            break
                        if n3 == "2":
                            print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                            n5 = str("play")
                            import time
                            time.sleep(2)
                            break
                    if 민심 < 50:
                        print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                        import time
                        time.sleep(2)
                        continue
            if n2 == "4":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                        if 군사력 > 상대국군사력:
                            print("[시스템]\n "+username+"은(는) 드디어 토란국을 정복했다.")
                            import time
                            time.sleep(2)
                            print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                            import time
                            time.sleep(2)
                            print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                            import time
                            time.sleep(2)
                            print(" 당신의 승리입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            n5 = str("You Victory")
                            print("\n \n \n \n \n You Victory  ")
                            break
        if n1 == "토란국" or n1 == "2":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5
                민심 = 민심 - 10
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심)+"(-10)")
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                if 민심 < 20:
                    print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                    import time
                    time.sleep(2)
                    print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                    import time
                    time.sleep(2)
                    print("비서: 어떻게 하실껀가요??\n")
                    import time
                    time.sleep(2)
                    n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                    if n3 == "1":
                        print(username+": 죄송합니다. 정말 죄송합니다..")
                        import time
                        time.sleep(2)
                        if n1 == "미역국" or n1 == "1":
                            print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        if n1 == "토란국" or n1 == "2":
                            print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                            import time
                            time.sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n YOU LOSE  ")
                        n5 = str("Die")
                        break
                    if n3 == "2":
                        print(username+": 나의 군사력을 동원해 반란자들을 처단하라!!")
                        n5 = str("play")
                        import time
                        time.sleep(2)
                        break
                if 민심 < 50:
                    print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "토란국" or n1 == "2":
            if n2 == "2":
                if 예산 < 인구수 * 0.5:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 0.5:
                    민심 = 민심 + 20
                    if 민심 >= 300:
                        민심 = 300
                        print("\n비서: 민심이 최고치로 올랐습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 모든 국민이 "+username+"님을 숭배하고 찬양하기 시작했습니다.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님은 이제 이 나라의 신과 같은 존재가 됩니다.")
                        import time
                        time.sleep(2)
                        print("비서: 더이상 민심이 떨어지지 않습니다.\n")
                        n5 = str("God")
                        break
                    print("\n비서: 알겠습니다. 일꾼들에게 사회복지 시설을 건축하라 시키겠습니다.")
                    예산 = 예산 - 인구수 * 0.5
                    if 민심 >= 250:
                        print("비서: 민심의 최대치는 300입니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심)+"(+20)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
        if n1 == "토란국" or n1 == "2":
            if n2 == "3":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.0033
                    민심 = 민심 - 10
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.0033)+")")
                    print("민심: "+str(민심)+"(-10)")
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.0033
                    import time
                    time.sleep(2)
                    if 민심 < 20:
                        print("국민1: "+username+", 너 때문에 우리가 못살겠다.\n국민2: 이렇게는 안되겠어. 지도자를 끌어내자.")
                        import time
                        time.sleep(2)
                        print("비서: "+username+"님.. 바닥난 민심으로 반란군이 생겼습니다.")
                        import time
                        time.sleep(2)
                        print("비서: 어떻게 하실껀가요??\n")
                        import time
                        time.sleep(2)
                        n3 = str(input(" 1. 사죄하며 지도자자리에서 내려온다.\n 2. 독재자가 된다. 최후의 발악\n \n선택해 주세요: "))
                        if n3 == "1":
                            print(username+": 죄송합니다. 정말 죄송합니다..")
                            import time
                            time.sleep(2)
                            if n1 == "미역국" or n1 == "1":
                                print(" [시스템]\n "+username+"님 당신은 미역국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            if n1 == "토란국" or n1 == "2":
                                print(" [시스템]\n "+username+"님 당신은 토란국의 지도자 자리에서 내려오셨습니다.")
                                import time
                                time.sleep(2)
                            print(" 당신의 패배입니다.")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n YOU LOSE  ")
                            n5 = str("Die")
                            break
                        if n3 == "2":
                            print(username+": 나의 군사력을 동원해 반란자들을 처단하라!! ")
                            n5 = str("play")
                            import time
                            time.sleep(2)
                            break
                    if 민심 < 50:
                        print("비서: 민심이 50 이하로 떨어졌습니다! 만일 민심이 20 이하로 떨어지게 되면 국민들이 반란을 일으킬 수 있습니다! 조심해주세요!!\n \n")
                        import time
                        time.sleep(2)
                        continue
            if n2 == "4":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                    if 군사력 > 상대국군사력:
                        print("[시스템]\n "+username+"은(는) 드디어 미역국을 정복했다.")
                        print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                        import time
                        time.sleep(2)
                        print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                        import time
                        time.sleep(2)
                        print(" 당신의 승리입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        n5 = str("You Victory")
                        print("\n \n \n \n \n You Victory  ")
                        break

if n5 == "play":
    if n3 == "2":
        print("\n \n \n \n \n 며칠 후..")
        import time
        time.sleep(2)
        print(" 군사력을 동원해 반란군의 진압에 성공하였다...")
        import time
        time.sleep(2)
        print(" 하지만..")
        import time
        time.sleep(2)
        if n1 == "미역국" or n1 == "1":
            print(" 미역국의 독재자가 된 "+username+"은..")
        if n1 == "토란국" or n1 == "2":
            print(" 토란국의 독재자가 된 "+username+"은..")
        import time
        time.sleep(2)
        print(" 아무도 그를 믿어주지 못하였다.")
        import time
        time.sleep(2)
        print(" 점점 혼자가 되어가는데..\n \n \n \n \n")
        import time
        time.sleep(2)
        print(" [시스템]\n 이제부터 인구수가 매턴마다 10000명씩 감소하게 됩니다.")
        import time
        time.sleep(2)
        print(" 만약 인구수가 0명이 될 시 국가의 운영이 불가능하므로 게임을 종료시킵니다.\n \n")
        import time
        time.sleep(2)
        인구수 = 인구수 - 10000
        인구수2 = 인구수2 - 10000
        민심 = 0
        print("예산: "+str(예산))
        print("인구수: "+str(인구수))
        print("군사력: "+str(군사력))
        print("민심: "+str(민심))
        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
        import time
        time.sleep(2)
    if n3 == "2":
        while True:
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            import time
            time.sleep(2)
            if 인구수 <= 0:
                print(" [시스템]\n 인구수가 0명에 도달하였습니다.")
                import time
                time.sleep(2)
                print(" 더 이상 국가를 운영할 수 없습니다.")
                import time
                time.sleep(2)
                print(" 게임을 종료합니다.")
                import time
                time.sleep(2)
                print("\n \n \n \n \n YOU LOSE  ")
                break
            if n1 == "미역국" or n1 == "1":
                n4 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5 + 50000)+")\n 2. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 3. 상대국 공격\n \n선택해 주세요: "))
            if n1 == "토란국" or n1 == "2":
                n4 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5)+")\n 2. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 3. 상대국 공격\n \n선택해 주세요: "))
            if n1 == "미역국" or n1 == "1":
                if n4 == "1":
                    print(" [시스템]\n 세금 징수.\n")
                    예산 = 예산 + 인구수 * 1.5 + 50000
                    인구수 = 인구수 - 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    인구수2 = 인구수2 - 10000
                    import time
                    time.sleep(2)
                    continue
                if n4 == "2":
                    if 예산 < 인구수 * 2:
                        print("\n [시스템]\n 예산 부족.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력))
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        import time
                        time.sleep(2)
                        continue
                    if 예산 > 인구수 * 2:
                        print("\n [시스템]\n 군사력 증강.")
                        예산 = 예산 - 인구수 * 2.0
                        군사력 = 군사력 + 인구수 * 0.002
                        인구수 = 인구수 - 10000
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수)+"(-10000)")
                        print("군사력: "+str(군사력)+"(+"+str(군사력2 * 0.002)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 =  군사력2 + 인구수 * 0.002
                        import time
                        time.sleep(2)
                        continue
            if n4 == "3":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        인구수 = 인구수 - 10000
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수)+"(-10000)")
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        continue
                    if 군사력 > 상대국군사력:
                        print("[시스템]\n "+username+"은(는) 드디어 미역국은 토란국을 정복했다.")
                        print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었다.")
                        import time
                        time.sleep(2)
                        print(" 하지만..")
                        import time
                        time.sleep(2)
                        print(" "+username+"의 곁에는 아무도 없었다..")
                        import time
                        time.sleep(2)
                        print(" 과연 이것이 승리일까?..")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        print("\n \n \n \n \n The End  ")
                        break
            if n1 == "토란국" or n1 == "2":
                if n4 == "1":
                    print("\n [시스템]\n 세금 징수.")
                    예산 = 예산 + 인구수 * 1.5
                    인구수 = 인구수 - 10000
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수)+"(-10000)")
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    인구수2 = 인구수2 - 10000
                    import time
                    time.sleep(2)
                    continue
                if n4 == "2":
                    if 예산 < 인구수 * 2:
                        print("\n [시스템]\n 예산 부족.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력))
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        import time
                        time.sleep(2)
                        continue
                    if 예산 > 인구수 * 2:
                        print("\n [시스템]\n 군사력 증강.")
                        예산 = 예산 - 인구수 * 2.0
                        군사력 = 군사력 + 인구수 * 0.0033
                        인구수 = 인구수 - 10000
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수)+"(-10000)")
                        print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.0033)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - 인구수 * 0.0033
                        import time
                        time.sleep(2)
                        continue
                if n4 == "3":
                    if 군사력 <= 100:
                        print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력))
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        import time
                        time.sleep(2)
                        continue
                    if 군사력 > 100:
                        if 군사력 < 상대국군사력:
                            상대국군사력 = 상대국군사력 - 군사력
                            군사력 = 군사력 - (군사력 - 100)
                            인구수 = 인구수 - 10000
                            print("\n비서: "+username+"님 공격에 실패했습니다.")
                            print("예산: "+str(예산))
                            print("인구수: "+str(인구수)+"(-10000)")
                            print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                            print("민심: "+str(민심))
                            print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                            군사력2 = 군사력2 - (군사력2 - 100)
                            import time
                            time.sleep(2)
                            continue
                        if 군사력 > 상대국군사력:
                            print("[시스템]\n "+username+"은(는) 드디어 토란국은 미역국을 정복했다.")
                            print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었다.")
                            import time
                            time.sleep(2)
                            print(" 하지만..")
                            import time
                            time.sleep(2)
                            print(" "+username+"의 곁에는 아무도 없었다..")
                            import time
                            time.sleep(2)
                            print(" 과연 이것이 승리일까?..")
                            import time
                            time.sleep(2)
                            print(" 게임을 종료합니다.")
                            import time
                            time.sleep(2)
                            print("\n \n \n \n \n The End  ")
                            break
                        
if n5 == "God":
    이벤트2 = 000
    print("비서: "+username+"님 정찰병의 새로운 정보가 들어왔습니다!")
    import time
    time.sleep(2)
    if n1 == "미역국" or n1 == "1":
        print("비서: "+username+"님의 막대한 권력 때문에 토란국에서 암살자가 넘어 온다는 소식입니다.\n \n \n")
    if n1 == "토란국" or n1 == "2":
        print("비서: "+username+"님의 막대한 권력 때문에 미역국에서 암살자가 넘어 온다는 소식입니다.\n \n \n")
    import time
    time.sleep(2)
    while True:
        if 이벤트2 == int("999"):
            import random
            Len2 = 2
            List2 = random.sample(range(5), Len2)
            secret2 = ''
            for i in range(Len2):
                secret2 += str(List2[i])
            if secret2 == "01" or secret2 == "02" or secret2 == "03" or secret2 == "04" or secret2 == "10" or secret2 == "20" or secret2 == "30" or secret2 == "40":
                print("비서: 지도자로서 국가 내의 다양한 행사에 참여하셔야 합니다.")
                import time
                time.sleep(2)
                print("비서: 어떤 행사에 참여할지 선택하여 주십시오.\n")
                import time
                time.sleep(2)
                print(" [경고]\n 어떤 장소에 암살자가 대기하고 있을지 모르므로 유의하여 선택하여 주십시오.")
                import time
                time.sleep(2)
                n7 = str(input(" 1. 야외 무대 연설\n 2. 병사 위로연\n 3. 방위시설 방문\n 4. 행차 행사 참여\n 5. 문화제 행사 방문\n \n비서: 선택하여 주십시오: "))
                import time
                time. sleep(2)
                import random
                Len3 = 1
                List3 = random.sample(range(5), Len3)
                secret3 = ''
                for i in range(Len3):
                    secret3 += str(List3[i])
                if secret3 == "0":
                    if n7 == "1":
                        print("\n [시스템]\n 야외 무대 연설에 가셨습니다.")
                        import time
                        time. sleep(2)
                        print(" 연설도중 야외에 배치되어 있던 저격수에 의해 살해당했습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time. sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time. sleep(2)
                        print("\n \n \n \n \n The End  ")
                        break
                    if n7 == "2":
                        print("\n [시스템]\n 병사 위로연에 갔습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "3":
                        print("\n [시스템]\n 방위시설을 방문 했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "4":
                        print("\n [시스템]\n 행차 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "5":
                        print("\n [시스템]\n 문화제 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                if secret3 == "1":
                    if n7 == "1":
                        print("\n [시스템]\n 야외 무대 연설에 가셨습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "2":
                        print("\n [시스템]\n 병사 위로연에 갔습니다.")
                        import time
                        time. sleep(2)
                        print(" 병사로 위장한 암살자에 의해 살해당했습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time. sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time. sleep(2)
                        print("\n \n \n \n \n The End  ")
                        break
                    if n7 == "3":
                        print("\n [시스템]\n 방위시설을 방문 했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "4":
                        print("\n [시스템]\n 행차 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "5":
                        print("\n [시스템]\n 문화제 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                if secret3 == "2":
                    if n7 == "1":
                        print("\n [시스템]\n 야외 무대 연설에 가셨습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "2":
                        print("\n [시스템]\n 병사 위로연에 갔습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "3":
                        print("\n [시스템]\n 방위시설을 방문 했습니다.")
                        import time
                        time. sleep(2)
                        print(" 방위시설에 암살자가 잠입해 있었습니다.")
                        import time
                        time. sleep(2)
                        print(" 그에 의해 살해당했습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time. sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time. sleep(2)
                        print("\n \n \n \n \n The End  ")
                        break
                    if n7 == "4":
                        print("\n [시스템]\n 행차 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "5":
                        print("\n [시스템]\n 문화제 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                if secret3 == "3":
                    if n7 == "1":
                        print("\n [시스템]\n 야외 무대 연설에 가셨습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "2":
                        print("\n [시스템]\n 병사 위로연에 갔습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "3":
                        print("\n [시스템]\n 방위시설을 방문 했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "4":
                        print("\n [시스템]\n 행차 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 주변 건물에서 기다리던 저격수에 의해 살해당했습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time. sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time. sleep(2)
                        print("\n \n \n \n \n The End  ")
                        break
                    if n7 == "5":
                        print("\n [시스템]\n 문화제 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                if secret3 == "4":
                    if n7 == "1":
                        print("\n [시스템]\n 야외 무대 연설에 가셨습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "2":
                        print("\n [시스템]\n 병사 위로연에 갔습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "3":
                        print("\n [시스템]\n 방위시설을 방문 했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "4":
                        print("\n [시스템]\n 행차 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 아무일도 일어나지 않았습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신은 안전합니다.\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        import time
                        time. sleep(2)
                    if n7 == "5":
                        print("\n [시스템]\n 문화제 행사에 참여했습니다.")
                        import time
                        time. sleep(2)
                        print(" 일반인으로 위장한 암살자에 의해 살해당했습니다.")
                        import time
                        time. sleep(2)
                        print(" 당신의 패배입니다.")
                        import time
                        time. sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time. sleep(2)
                        print("\n \n \n \n \n The End  ")
                        break
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        import time
        time.sleep(2)
        if n1 == "미역국" or n1 == "1":
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5 + 50000)+")\n 2. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 3. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "토란국" or n1 == "2":
            n2 = str(input(" 1. 세금징수(얻는 예산: "+str(인구수 * 1.5)+")\n 2. 군사력 증강(사용 예산: "+str(인구수 * 2)+")\n 3. 상대국 공격 \n \n선택해 주세요: "))
        if n1 == "미역국" or n1 == "1":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5 + 50000
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심))
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                이벤트2 = 999
                continue
            if n2 == "2":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    이벤트2 = 999
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.002
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.002)+")")
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.002
                    import time
                    time.sleep(2)
                    이벤트2 = 999
                    continue
            if n2 == "3":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    이벤트2 = 999
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        이벤트2 = 999
                        continue
                    if 군사력 > 상대국군사력:
                        print("[시스템]\n "+username+"은(는) 드디어 토란국을 정복했다.")
                        import time
                        time.sleep(2)
                        print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                        import time
                        time.sleep(2)
                        print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                        import time
                        time.sleep(2)
                        print(" 당신의 승리입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        n5 = str("You Victory")
                        print("\n \n \n \n \n You Victory  ")
                        break
        if n1 == "토란국" or n1 == "2":
            if n2 == "1":
                print("\n비서: 알겠습니다. 세금을 징수 하겠습니다.")
                예산 = 예산 + 인구수 * 1.5
                print("예산: "+str(예산))
                print("인구수: "+str(인구수))
                print("군사력: "+str(군사력))
                print("민심: "+str(민심))
                print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                import time
                time.sleep(2)
                이벤트2 = 999
                continue
            if n2 == "2":
                if 예산 < 인구수 * 2:
                    print("\n비서: "+username+"님 예산이 부족합니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    이벤트2 = 999
                    continue
                if 예산 > 인구수 * 2:
                    print("\n비서: 알겠습니다. 군사력 증강을 위해 증병과 군비확충을 하겠습니다.")
                    예산 = 예산 - 인구수 * 2.0
                    군사력 = 군사력 + 인구수 * 0.0033
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력)+"(+"+str(인구수 * 0.0033)+")")
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    군사력2 = 군사력2 + 인구수 * 0.0033
                    import time
                    time.sleep(2)
                    이벤트2 = 999
                    continue
            if n2 == "3":
                if 군사력 <= 100:
                    print("\n비서: "+username+"님, 충분한 군사력을 보유하셔야 공격 가실 수 있습니다.")
                    print("예산: "+str(예산))
                    print("인구수: "+str(인구수))
                    print("군사력: "+str(군사력))
                    print("민심: "+str(민심))
                    print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                    import time
                    time.sleep(2)
                    이벤트2 = 999
                    continue
                if 군사력 > 100:
                    if 군사력 < 상대국군사력:
                        상대국군사력 = 상대국군사력 - 군사력
                        군사력 = 군사력 - (군사력 - 100)
                        print("\n비서: "+username+"님 공격에 실패했습니다.")
                        print("예산: "+str(예산))
                        print("인구수: "+str(인구수))
                        print("군사력: "+str(군사력)+"(-"+str(군사력2-100)+")")
                        print("민심: "+str(민심))
                        print("상대국군사력: "+str(상대국군사력)+"\n \n \n \n")
                        군사력2 = 군사력2 - (군사력2 - 100)
                        import time
                        time.sleep(2)
                        이벤트2 = 999
                        continue
                    if 군사력 > 상대국군사력:
                        print("[시스템]\n "+username+"은(는) 드디어 미역국을 정복했다.")
                        print(" "+username+"은(는) 최초로 세상을 통일한 지도자가 되었으며..")
                        import time
                        time.sleep(2)
                        print(" "+username+"은(는) 후세에도 존경받는 지도자가 되었다.")
                        import time
                        time.sleep(2)
                        print(" 당신의 승리입니다.")
                        import time
                        time.sleep(2)
                        print(" 게임을 종료합니다.")
                        import time
                        time.sleep(2)
                        n5 = str("You Victory")
                        print("\n \n \n \n \n You Victory  ")
                        break
