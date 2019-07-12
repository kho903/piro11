
import random


class User:
    def __init__(self):
        self.name = input('캐릭터 이름을 입력하세요: ')
        self.item = 0  # 장비의 능력치 (공격력에 추가됨)
        self.attack = 100  # 캐릭터의 기본 공격력 100(레벨 올라도 같음)
        self.level = 1  # 몬스터와의 전투 결과에 따라 상승
        self.hp = self.level * 100  # 캐릭터의 체력 (레벨에 따라 오름)
        self.cash = 0  # 충전 전 캐시 (당연히 0)
        self.armor = 0 # 방어력 수치 기본:0

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

    def armor_strengthen(self, cash):  # 강화 성공률은 기본 0.3+ 사용하는 캐시 (1~100)%만큼
        if self.cash >= cash:
            self.cash -= cash
            if random.random() < 0.3 + cash / 100:
                self.armor += 10
                if self.armor>90:  #방어력 최대 90으로 고정
                    self.armor=90
                    print("더 이상 강화 하실 수 없습니다. "
                          "(강화를 실행하셔도 더 이상 방어력이 오르지 않습니다.)")
                print("강화에 성공하였습니다.",
                    "캐릭터의 방어력: ", self.armor,
                    "남은 캐쉬: ", self.cash)
            else:
                print("강화에 실패하였습니다.", "남은 캐쉬: ", self.cash)

        else:
            print('캐시가 부족합니다!')

    def cash_charge(self, amount):
        self.cash += amount



    # def shop(self):
    #     Armor_Item={"천갑옷":2,"쇠사슬조끼":4,"덤불조끼":6,"파수꾼의 갑옷":8,
    #            "망자의 갑옷":10,"란두인의 예언":12,"태양불꽃망토":14}
    #     ArL=Armor_Item.keys()
    #     ARP1=list(range(1,8))
    #     ARP=list(map(lambda x: x*100,ARP1))
    #     Attack_Item={"롱소드":5,"도란의검":10,"곡괭이":15,"콜필드의 전투망치":20,
    #                  "톱날단검":25, "탐식의 망치":30, "비에프대검":35}
    #     AtL=Attack_Item.keys()
    #     ATP1=list(range(1,8))
    #     ATP=list(map(lambda x: x*100,ATP1))
    #     print("상점에 오신 것을 환영합니다.")
    #     print("1. 방어구 2. 무기")
    #     sel=int(input())
    #     if sel==1:
    #         print("구매하실 무기를 선택하세요")
    #         ar=int(input())
    #         if ar==1:
    #             if self.cash >= ARP[0]:
    #                 self.armor +=Armor_Item[ArL[0]]
    #                 self.cash -=ARP[0]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==2:
    #             if self.cash >= ARP[1]:
    #                 self.armor +=Armor_Item[ArL[1]]
    #                 self.cash -=ARP[1]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==3:
    #             if self.cash >= ARP[2]:
    #                 self.armor +=Armor_Item[ArL[2]]
    #                 self.cash -=ARP[2]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==4:
    #             if self.cash >= ARP[3]:
    #                 self.armor +=Armor_Item[ArL[3]]
    #                 self.cash -=ARP[3]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==5:
    #             if self.cash >= ARP[4]:
    #                 self.armor +=Armor_Item[ArL[4]]
    #                 self.cash -=ARP[4]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==6:
    #             if self.cash >= ARP[5]:
    #                 self.armor +=Armor_Item[ArL[5]]
    #                 self.cash -=ARP[5]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==7:
    #             if self.cash >= ARP[6]:
    #                 self.armor +=Armor_Item[ArL[6]]
    #                 self.cash -=ARP[6]
    #             else:
    #                 print("금액이 부족합니다.")
    #     if sel==2:
    #         if ar==1:
    #             if self.cash>=ATP[0]:
    #                 self.armor +=Attack_Item[AtL[0]]
    #                 self.cash -=ATP[0]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==2:
    #             if self.cash >= ATP[1]:
    #                 self.armor +=Attack_Item[AtL[1]]
    #                 self.cash -=ATP[1]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==3:
    #             if self.cash >= ATP[2]:
    #                 self.armor +=Attack_Item[AtL[2]]
    #                 self.cash -=ATP[2]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==4:
    #             if self.cash >= ATP[3]:
    #                 self.armor +=Attack_Item[AtL[3]]
    #                 self.cash -=ATP[3]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==5:
    #             if self.cash >= ATP[4]:
    #                 self.armor +=Attack_Item[AtL[4]]
    #                 self.cash -=ATP[4]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==6:
    #             if self.cash >= ATP[5]:
    #                 self.armor +=Attack_Item[AtL[5]]
    #                 self.cash -=ATP[5]
    #             else:
    #                 print("금액이 부족합니다.")
    #         if ar==7:
    #             if self.cash >= ATP[6]:
    #                 self.armor +=Attack_Item[AtL[6]]
    #                 self.cash -=ATP[6]
    #             else:
    #                 print("금액이 부족합니다.")


