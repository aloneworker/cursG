from girl import Girl
from player import Player
import random

def load_names(filename):
    """
    從給定的文件中加載名字。

    參數:
        filename (str): 包含名字的文件名。

    返回:
        list: 包含名字的列表。
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def main():
    """
    遊戲的主函數，負責處理遊戲循環和玩家互動。
    """
    player = Player()
    girl_names = load_names("girl_names.txt")
    possible_features = ["巨乳", "翹臀", "長腿", "正妹", "蛇腰"]
    
    while True:
        print(f"\n當前咒力：{player.get_mana()}")
        if player.mana < 3 and not player.book:
            print("咒力不足，且本子中沒有妹子！")
            break

        print("1. 招喚妹子術")
        if player.book:
            print("2. 本子術")
        print("3. 結束遊戲")

        choice = input("請選擇你的行動：")
        if choice == '1':
            girl = player.cast_summon_girl()
            if girl:
                name = random.choice(girl_names)
                features = random.sample(possible_features, random.randint(0, 3))
                girl.name = name
                girl.features = features
                print(f"你成功招喚了{girl.name}！她的特徵是：{', '.join(features)}")
                player.add_girl_to_book(girl)
            else:
                print("咒力不足！")
        elif choice == '2' and player.book:
            player.cast_book_spell()
        elif choice == '3':
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
