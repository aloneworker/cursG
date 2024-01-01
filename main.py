from girl import Girl
from player import Player
import random

def load_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def main():
    player = Player()
    girl_names = load_names("girl_names.txt")
    possible_features = ["巨乳", "翹臀", "長腿", "正妹", "蛇腰"]
    girl = None
    
    while True:
        print(f"\n當前咒力：{player.get_mana()}")
        if not girl:
            print("1. 招喚妹子術")
            if player.book:
                print("2. 本子術")
            print("3. 結束遊戲")

        choice = input("請選擇你的行動：")
        if choice == '1' and not girl:
            girl = player.cast_summon_girl()
            if girl:
                name = random.choice(girl_names)
                features = random.sample(possible_features, random.randint(0, 3))
                girl.name = name
                girl.features = features
                print(f"你成功招喚了{girl.name}！她的特徵是：{', '.join(features)}")
            else:
                print("咒力不足！")
        elif choice == '2' and not girl and player.book:
            if player.mana >= 3:
                player.mana -= 3
                print("本子中的妹子：")
                for index, girl in enumerate(player.book):
                    print(f"{index + 1}. {girl.name} - 狀態：{girl.update_relationship()}")
                select = int(input("選擇要互動的妹子編號：")) - 1
                if 0 <= select < len(player.book):
                    girl = player.book[select]
                    interaction = input(f"選擇與{girl.name}的互動方式：1. 聊天 (5咒力) 2. 約會 (15咒力): ")
                    if interaction == '1' and player.mana >= 5:
                        player.mana -= 5
                        print(f"你選擇了與{girl.name}聊天。")
                        # 聊天邏輯
                    elif interaction == '2' and player.mana >= 15:
                        player.mana -= 15
                        print(f"你選擇了與{girl.name}約會。")
                        # 約會邏輯
                    else:
                        print("咒力不足或無效的選擇！")
                        girl = None
                else:
                    print("無效的選擇！")
            else:
                print("咒力不足！")
        elif choice == '3':
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
