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
            print("4. 打開後台 (僅限開發者使用)")

            # 增加喚妻咒術選項
            if any(girl.get_relationship_stage() == "夫妻" for girl in player.book):
                print("5. 喚妻咒術")

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
            player.cast_book_spell()
        elif choice == '5' and any(girl.get_relationship_stage() == "夫妻" for girl in player.book) and not girl:
            player.cast_wife_spell()
        elif choice in ['3', '4'] and girl:
            mood = "閒聊" if choice == '3' else "認真"
            chat_result, leave = girl.chat(mood)
            print(chat_result)
            if leave:
                leave_message = girl.leave_check()
                if leave_message and "是否要加入本子" in leave_message:
                    print(leave_message)
                    add_choice = input("選擇 1 同意, 2 拒絕: ")
                    if add_choice == '1':
                        name = random.choice(girl_names)
                        features = random.sample(possible_features, random.randint(0, 3))
                        girl.name = name
                        girl.features = features
                        player.add_girl_to_book(girl)
                        print(f"{girl.name}加入了你的本子。她的特徵是：{', '.join(features)}")
                    girl = None
                else:
                    print(leave_message)
                    girl = None
        elif choice == '5' and girl:
            girl = None
        elif choice == '4':
            player.open_backend()
        elif choice == '3' and not girl:
            print("遊戲結束。")
            break

        elif choice =='' :
            # 更新妹子的行動
            for girl in player.book:
                girl.update_action()
                print(f"{girl.name} 當前行動: {girl.current_action}")
                friends_list = ", ".join([f"{name}: {value}" for name, value in girl.male_friends.items()])
                print(f"朋友名單: {friends_list if friends_list else '無'}")
                print(f"子宮內 {girl.子宮}")
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")


if __name__ == "__main__":
    main()
