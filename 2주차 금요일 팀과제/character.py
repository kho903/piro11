import random


class User:
    def __init__(self):
        self.name = input('캐릭터 이름을 입력하세요: ')
        self.item = 0  # 장비의 능력치 (공격력에 추가됨)
        self.attack = 100  # 캐릭터의 기본 공격력 100(레벨 올라도 같음)
        self.level = 1  # 몬스터와의 전투 결과에 따라 상승
        self.hp = self.level * 100  # 캐릭터의 체력 (레벨에 따라 오름)
        self.cash = 0  # 충전 전 캐시 (당연히 0)

    def item_strengthen(self, cash):  # 강화 성공률은 기본 0.3+ 사용하는 캐시 (1~100)%만큼
        if self.cash >= cash:
            self.cash -= cash
            if random.random() < 0.3 + cash / 100:
                self.item += 10
                self.attack = 100 + self.item
                print("강화에 성공하였습니다.",
                      "장비의 능력치: ",self.item,
                      "장비의 공격력: ",self.attack,
                      "남은 캐쉬: ",self.cash)
            else:
                print("강화에 실패하였습니다.","남은 캐쉬: ",self.cash)

        else:
            print('캐시가 부족합니다!')

    def cash_charge(self, amount):
        self.cash += amount
