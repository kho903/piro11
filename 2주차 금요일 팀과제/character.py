import random


class User:
    def __init__(self):
        self.name = input('캐릭터 이름을 입력하세요: ')
        self.item = 0  # 장비의 능력치 (공격력에 추가됨)
        self.attack = 100  # 캐릭터의 기본 공격력 100(레벨 올라도 같음)
        self.level = 1  # 몬스터와의 전투 결과에 따라 상승
        self.hp = self.level * 100  # 캐릭터의 체력 (레벨에 따라 오름)

    def item_strengthen(self):  # 강화 성공률은 50%로
        if random.random() > 0.5:
            self.item += 10
        self.attack += self.item
