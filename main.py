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
            print("3. 與妹子閒聊 (消耗5咒力)")
            print("4. 與妹子約會 (消耗15咒力)")
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
                select = int(input("選擇要互動的妹子編號：")) - 1
                if 0 <= select < len(player.book):
                    girl = player.book[select]
                    print(f"你選擇了{girl.name}。")
                else:
                    print("無效的選擇！")
        elif choice in ['3', '4'] and girl:
            if choice == '3' and player.mana >= 5:
                player.mana -= 5
                mood = "閒聊"
            elif choice == '4' and player.mana >= 15:
                player.mana -= 15
                mood = "約會"
            else:
                print("咒力不足！")
                continue

            chat_result, leave = girl.chat(mood)
            print(chat_result)
            if leave:
                girl = None
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
