import random

def load_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

class Girl:
    def __init__(self, name="", features=[]):
        self.name = name
        self.features = features
        self.moods = ["閒聊", "無聊", "認真"]
        self.current_mood = random.choice(self.moods)
        self.displeasure = 0
        self.excitement = 0
        self.relationship = 0  # 新增：玩家和妹子的關係

    def chat(self, choice):
        if choice == self.current_mood:
            result = random.choices(["高興", "厭煩", "無感"], weights=[50, 30, 20])[0]
        else:
            result = random.choices(["高興", "厭煩", "無感"], weights=[30, 50, 20])[0]

        if result == "高興":
            self.excitement += 1
            if self.excitement > 3:  # 當高興超過3次，關係增加
                self.relationship += 1
                return "妹子感到高興了！關係增加，妹子離開了。", True
            return "妹子感到高興了！", False
        elif result == "厭煩":
            self.displeasure += 1
            if self.displeasure > 5:  # 當厭煩超過5次，妹子離開
                return "妹子感到厭煩了。妹子離開了。", True
            return "妹子感到厭煩了。", False
        else:
            return "妹子無感。", False

    def leave_check(self):
        if self.displeasure > 5:
            return "妹子因為反感太多而離開了。"
        elif self.excitement > 5:
            return "妹子很興奮，問你是否要加入本子。"
        return None

class Player:
    def __init__(self):
        self.mana = 100
        self.book = []  # 存儲本子中的妹子

    def cast_summon_girl(self):
        if self.mana >= 10:
            self.mana -= 10
            return Girl()
        else:
            return None

    def add_girl_to_book(self, girl):
        self.book.append(girl)

    def cast_book_spell(self):
        if self.mana >= 3 and self.book:
            self.mana -= 3
            print("本子中的妹子：")
            for index, girl in enumerate(self.book):
                print(f"{index + 1}. {girl.name}")
            return True
        else:
            print("咒力不足或本子中沒有妹子！")
            return False

    def get_mana(self):
        return self.mana

def main():
    player = Player()
    girl = None
    girl_names = load_names("girl_names.txt")
    possible_features = ["巨乳", "翹臀", "長腿", "正妹", "蛇腰"]
    
    while True:
        print(f"\n當前咒力：{player.get_mana()}")
        if not girl:
            print("1. 招喚妹子術")
            if player.book:
                print("2. 本子術")
        else:
            print("3. 與妹子閒聊")
            print("4. 與妹子認真聊天")
        print("5. 結束遊戲")

        choice = input("請選擇你的行動：")
        if choice == '1' and not girl:
            girl = player.cast_summon_girl()
            if girl:
                print("你成功招喚了一位妹子！")
            else:
                print("咒力不足！")
        elif choice == '2' and not girl:
            if player.cast_book_spell():
                select = int(input("選擇要聊天的妹子編號：")) - 1
                if 0 <= select < len(player.book):
                    girl = player.book[select]
                    print(f"你選擇了與{girl.name}聊天！")
                else:
                    print("無效的選擇！")
        elif choice in ['3', '4'] and girl:
            mood = "閒聊" if choice == '3' else "認真"
            chat_result, leave = girl.chat(mood)
            print(chat_result)
            if leave:
                girl = None
        elif choice == '5':
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
