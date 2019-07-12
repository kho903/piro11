import random
import character
class monster:
    def __init__(self,lv):
        a=['커피를 마시는 ','외로움을 타는 ','문서 작성을 잘하는 ','정신을 집중한 ','여행 계획을 세우는 ','인터넷 검색 중인 ']
        i = random.randint(0,len(a))
        b=['신입 사원','3년차 대리','만년 과장','꼰대 부장님','대머리 상무 이사','낙하산 임원']
        j = random.randint(0,len(b))
        self.name = a[i]+b[j]
        self.level=lv
        self.hp=self.level * 100
        self.attack=100
        print('{0} {1} - {2}레벨- 이/가 출몰했다..!'.format(a[i],b[j],self.level))

