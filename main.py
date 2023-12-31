import random

class Girl:
    def __init__(self):
        self.moods = ["閒聊", "無聊", "認真"]
        self.current_mood = random.choice(self.moods)
        self.displeasure = 0
        self.excitement = 0

    def chat(self, choice):
        if choice == self.current_mood:
            # 玩家選擇的聊天項目跟妹子的心情一樣
            result = random.choices(["高興", "厭煩", "無感"], weights=[70, 10, 20])[0]
        else:
            # 玩家選擇的聊天項目跟妹子的心情不同
            result = random.choices(["高興", "厭煩", "無感"], weights=[10, 70, 20])[0]

        if result == "高興":
            self.excitement += 1
            return "妹子感到高興了！"
        elif result == "厭煩":
            self.displeasure += 1
            return "妹子感到厭煩了。"
        else:
            return "妹子無感。"

    def leave_check(self):
        if self.displeasure > 5:
            return "妹子因為反感太多而離開了。"
        elif self.excitement > 5:
            return "妹子很興奮，問你是否要加入本子。"
        return None

class Player:
    def __init__(self):
        self.mana = 100

    def cast_summon_girl(self):
        if self.mana >= 10:
            self.mana -= 10
            return Girl()
        else:
            return None

    def get_mana(self):
        return self.mana

def main():
    player = Player()
    girl = None
    while True:
        print(f"\n當前咒力：{player.get_mana()}")
        if not girl:
            print("1. 招喚妹子術")
        else:
            print("2. 與妹子閒聊")
            print("3. 與妹子認真聊天")
        print("4. 結束遊戲")

        choice = input("請選擇你的行動：")
        if choice == '1' and not girl:
            girl = player.cast_summon_girl()
            if girl:
                print("你成功招喚了一位妹子！")
            else:
                print("咒力不足！")
        elif choice in ['2', '3'] and girl:
            mood = "閒聊" if choice == '2' else "認真"
            print(girl.chat(mood))
            leave_message = girl.leave_check()
            if leave_message:
                print(leave_message)
                girl = None
        elif choice == '4':
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
