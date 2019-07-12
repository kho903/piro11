import monster
import character
import random

def battle(character):
    mon1 = monster.monster(character.level)

    while True:
        print("유저의 체력: ", character.hp, " 몬스터의 체력:", mon1.hp)
        print(" 1. 바위 \n 2. 보 \n 3. 가위 \n")
        choice = int(input("선택하세요: "))
        while choice > 3 or choice < 1:
            choice = int(input("선택범위가 아닙니다....: "))
        if choice == 1:
            choice_name = '바위'
        elif choice == 2:
            choice_name = '보'
        else:
            choice_name = '가위'
        print("유저의 선택: " + choice_name)
        comp_choice = random.randint(1, 3)
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)
        if comp_choice == 1:
            comp_choice_name = '바위'
        elif comp_choice == 2:
            comp_choice_name = '보'
        else:
            comp_choice_name = '가위'
        print("몬스터의 선택은: " + comp_choice_name)
        print(choice_name + " V/s " + comp_choice_name)
        if ((choice == 1 and comp_choice == 2) or
                (choice == 2 and comp_choice == 1)):
            print("보 wins => ", end="")
            result = "보"
        elif ((choice == 1 and comp_choice == 3) or
              (choice == 3 and comp_choice == 1)):
            print("바위 wins =>", end="")
            result = "바위"
        else:
            print("가위 wins =>", end="")
            result = "가위"
        if result == choice_name:
            print("<== 유저 wins ==>")
            mon1.hp -=character.attack
        else:
            print("<== 몬스터 wins ==>")
            character.hp -= mon1.attack
            character.hp += character.armor
        if character.hp<=0:
            print("패배하였습니다.")
            break
        if mon1.hp<=0:
            print("승리하였습니다.")
            character.level +=1
            character.hp = character.level*100
            break

