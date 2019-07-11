import random

name=input("캐릭터의 이름을 입력하세요:")
gla=random.randint(6,9)
wlfur=random.randint(6,9)
print("캐릭터 이름: %s"%name)
print(f'캐릭터 정보: 힘({gla}) 지력({wlfur})')
if gla>wlfur:
    print("캐릭터 직업: 전사")
elif gla==wlfur:
    print("캐릭터 직업: 궁수")
elif gla<wlfur:
    print("캐릭터 직업: 법사")
