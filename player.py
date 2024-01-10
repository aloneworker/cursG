from girl import Girl
from FolderScanner import *
import random
class Player:
    """
    玩家類，用於表示遊戲中的玩家。

    屬性:
        mana (int): 玩家的咒力值。
        book (list): 存儲本子中的妹子。
    """

    def __init__(self):
        self.mana = 100
        self.book = []
        self.精汁 = random.randint(5, 25)  # 玩家精汁的初始值
        self.S技 = random.randint(1, 3)    # 玩家S技的初始值 

    def cast_summon_girl(self):
        """
        使用咒力招喚妹子。

        返回:
            Girl: 新招喚的妹子，或者None（如果咒力不足）。
        """
        if self.mana >= 10:
            self.mana -= 10
            return Girl()
        else:
            return None

    def add_girl_to_book(self, girl):
        """
        將妹子加入到本子中。

        參數:
            girl (Girl): 要加入本子的妹子。
        """
        self.book.append(girl)

    def cast_book_spell(self):
        """
        使用本子術查看本子中的妹子，並提供與她們互動的選項。
    
        返回:
            bool: 本子術是否成功執行。
        """
        if self.mana >= 3 and self.book:
            self.mana -= 3
            print("本子中的妹子：")
            for index, girl in enumerate(self.book):
                features_str = ', '.join(girl.features) if girl.features else "無特徵"
                relationship_stage = girl.get_relationship_stage()  # 使用 get_relationship_stage 方法
                print(f"{index + 1}. [{relationship_stage}] {girl.name} - 特徵：{features_str}")
    
            girl_index = int(input("選擇要互動的妹子編號：")) - 1
            if 0 <= girl_index < len(self.book):
                selected_girl = self.book[girl_index]
                self.interact_with_girl(selected_girl)
            else:
                print("無效的選擇！")
            return True
        else:
            print("咒力不足或本子中沒有妹子！")
            return False

    def cast_wife_spell(self):
        """
        使用喚妻咒術查看並互動妻子。

        返回:
            bool: 咒術是否成功執行。
        """
        if self.mana >= 3:
            self.mana -= 3
            wives = [girl for girl in self.book if girl.get_relationship_stage() == "夫妻"]
            if wives:
                print("你的妻子：")
                for index, wife in enumerate(wives):
                    action = wife.action  # 妻子當前的行動
                    print(f"{index + 1}. {wife.name} - 目前行動：{action}")

                wife_index = int(input("選擇要互動的妻子編號：")) - 1
                if 0 <= wife_index < len(wives):
                    selected_wife = wives[wife_index]
                    self.interact_with_wife(selected_wife)
                else:
                    print("無效的選擇！")
                return True
            else:
                print("你沒有妻子！")
                return False
        else:
            print("咒力不足！")
            return False
    
    def interact_with_wife(self, wife):
        """
        與妻子互動。

        參數:
            wife (Girl): 要互動的妻子對象。
        """
        print(f"\n與{wife.name}互動：")
        print("1. 聊天")
        print("2. S")

        choice = input("選擇你的行動（輸入數字）：")

        if choice == '1':
            self.chat_with_girl(wife)
        elif choice == '2':
            # 執行S遊戲
            self.play_s_game(wife)
        else:
            print("無效的選擇！")
    def play_s_game(self,girl):
        s_game = SGame()
        selected_file = s_game.play_s_game(girl)
        """
        執行S遊戲。

        參數:
            girl (Girl): 參與S遊戲的妹子對象。
        """
        while True:
            if self.精汁 <= 0:
                print("無法進行S操作，精汁不足！")
                break

            print("S：", selected_file)

            # 有(1/S技)的機會觸發「射了」
            if random.randint(1, self.S技) == 1:
                if girl.decide_internal_finish(self.name):
                    girl.子宮.append(self.name)
                    print(random.choice(答應的話語))
                    print("射了！/n 射進子宮內！！！精汁減少，當前精汁值：", self.精汁)
                else:
                    print(random.choice(婉拒的話語))
                    print("射了！..精汁減少，當前精汁值：", self.精汁)
    
                self.精汁 -= 5  # 精汁減少5點
            

            # 檢查是否結束S操作
            choice = input("插？(enter or 1:out): ")
            if choice == '1':
                break
    
    def interact_with_girl(self, girl):
        """
        與本子中的妹子互動。

        參數:
            girl (Girl): 要互動的妹子對象。
        """
        print(f"\n與{girl.name}互動：")
        print("1. 聊天 (消耗5點咒力)")

        if girl.get_relationship_stage() != "陌生":
            print("2. 約會 (消耗20點咒力)")

        if girl.get_relationship_stage() == "朋友" and girl.relationship >= 4:
            print("3. 告白 (消耗30點咒力)")

        # 新增求婚選項
        if girl.get_relationship_stage() == "情侶" and girl.relationship >= 4:
            print("4. 求婚 (消耗50點咒力)")

        choice = input("選擇你的行動（輸入數字）：")

        if choice == '1':
            self.chat_with_girl(girl)
        elif choice == '2' and girl.get_relationship_stage() != "陌生":
            self.date_with_girl(girl)
        elif choice == '3' and girl.get_relationship_stage() == "朋友" and girl.relationship >= 4:
            self.confess_to_girl(girl)
        elif choice == '4' and girl.get_relationship_stage() == "情侶" and girl.relationship >= 4:
            self.propose_to_girl(girl)
    

    def chat_with_girl(self, girl):
        """
        與妹子聊天。

        參數:
            girl (Girl): 要聊天的妹子對象。
        """
        if self.mana >= 5:
            self.mana -= 5
            mood_choice = input("選擇聊天話題 (1. 閒聊 2. 認真)：")
            mood = "閒聊" if mood_choice == '1' else "認真"
            chat_result, leave = girl.chat(mood)
            print(chat_result)
            relationship_message = girl.update_relationship()
            if relationship_message:
                print(relationship_message)
        else:
            print("咒力不足！")

    def date_with_girl(self, girl):
        """
        與妹子約會。

        參數:
            girl (Girl): 要約會的妹子對象。
        """
        if self.mana >= 20:
            self.mana -= 20
            girl.relationship += 2  # 增加關係值
            # 有1/10的機會觸發去旅館
            if random.randint(1, 2) == 1:
                print(f"{girl.name}問你是否要去旅館。")
                choice = input("是否花費50咒力去旅館？(1/n): ")
                if choice.lower() == '1':
                    if self.mana >= 50:
                        self.mana -= 50
                        print("你選擇了去旅館。")
                        self.play_s_game(girl)
                    else:
                        print("咒力不足，無法去旅館！")
                else:
                    print("你選擇了不去旅館。")
            print(f"你和{girl.name}進行了愉快的約會，你們的關係更進一步了。")
            relationship_message = girl.update_relationship()
            if relationship_message:
                print(relationship_message)
        else:
            print("咒力不足！")


    def hotel_with_girl(self, girl):
        """
        與妹子去旅館。

        參數:
            girl (Girl): 要去旅館的妹子對象。
        """
        if self.mana >= 20:
            self.mana -= 20
            # 在這裡添加去旅館的後續事件和影響
                    # 加入1/5的機率進行S操作
         
            s_game = SGame()
            selected_file = s_game.play_s_game(girl.name)
            print("發生的S遊戲結果：", selected_file)
        else:
            print("咒力不足！")


    
    def open_backend(self):
        """
        打開後台功能，提供各種後台操作選項。
        """
        print("後台已打開，請選擇操作：")
        print("1. 增加一位妻子")
        print("2. 增加一位情人")
        print("3. 增加一位朋友")
        print("4. 查看本子中的妹子詳細信息")
        print("5. 咒力增加到999")

        choice = input("請選擇操作（輸入數字）：")

        if choice in ['1', '2', '3']:
            girl_name = input("輸入妹子的名字：")
            if choice == '1':
                self.add_girl(girl_name, "夫妻")
            elif choice == '2':
                self.add_girl(girl_name, "情侶")
            elif choice == '3':
                self.add_girl(girl_name, "朋友")
        elif choice == '4':
            self.show_girls_info()
        elif choice == '5':
            self.mana = 999
            print("咒力增加到999！")
        else:
            print("無效的選擇！")

    def add_girl(self, name, relationship_stage):
        """
        增加一位妹子到玩家的本子中。

        參數:
            name (str): 妹子的名字。
            relationship_stage (str): 與妹子的關係階段。
        """
        new_girl = Girl(name)
        new_girl.relationship_stage = relationship_stage
        self.book.append(new_girl)
        print(f"{name}（{relationship_stage}）已被添加到您的本子中。")
    def show_girls_info(self):
        """
        顯示本子中妹子的詳細信息。
        """
        if self.book:
            print("本子中的妹子詳細信息：")
            for girl in self.book:
                print(f"名稱：{girl.name}, 關係階段：{girl.relationship_stage}")
        else:
            print("本子中沒有妹子！")

    def confess_to_girl(self, girl):
        """
        嘗試向妹子告白。

        參數:
            girl (Girl): 玩家將要告白的妹子。
        """
        if self.mana >= 20:
            self.mana -= 20
            if random.randint(1, 3) == 1:
                print(f"你向{girl.name}告白了，但不幸地被拒絕了。")
            else:
                girl.relationship_stage = "情侶"
                girl.relationship = 0  # 清除關係值
                print(f"你向{girl.name}告白，她欣然接受了！現在你們是情侶了。")
               
        else:
            print("咒力不足，無法告白！")
    def propose_to_girl(self, girl):
        """
        向妹子求婚。

        參數:
            girl (Girl): 玩家將要求婚的妹子。
        """
        if self.mana >= 50:
            self.mana -= 50
            # 在這裡添加求婚成功的後續事件和影響
            print(f"你向{girl.name}求婚，她欣然接受了！現在你們是夫妻了。")
            girl.relationship_stage = "夫妻"
            girl.relationship = 0  # 重置關係值
        else:
            print("咒力不足，無法求婚！")

    
    def get_mana(self):
        """
        獲取玩家當前的咒力值。

        返回:
            int: 當前咒力值。
        """
        return self.mana
