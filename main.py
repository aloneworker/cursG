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
        else:
            print("3. 與妹子閒聊")
            print("4. 與妹子認真聊天")
            print("5. 結束對話")

        choice = input("請選擇你的行動：")
        if choice == '1' and not girl:
            girl = player.cast_summon_girl()
            if girl:
                print("你成功招喚了一位妹子！")
            else:
                print("咒力不足！")

    elif choice == '2' and not girl and player.book:
        if player.cast_book_spell():
            girl_index = int(input("選擇要互動的妹子編號：")) - 1
            if 0 <= girl_index < len(player.book):
                girl = player.book[girl_index]
                interaction = input(f"選擇與{girl.name}的互動方式 (1. 聊天 2. 約會): ")
                if interaction == '1':
                    # 聊天邏輯
                    pass  # 這裡添加聊天相關的代碼
                elif interaction == '2':
                    # 約會邏輯
                    print(f"你和{girl.name}去了一次愉快的約會。")
                    # 這裡可以添加更詳細的約會相關代碼
                else:
                    print("無效的選擇！")
            else:
                print("無效的編號！")
        girl = None  # 確保對話結束後重置girl變量
        elif choice == '5' and girl:
            girl = None
        elif choice == '3' and not girl:
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
