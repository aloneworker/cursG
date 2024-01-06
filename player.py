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
            s_game = SGame(self.base_path)
            selected_file = s_game.play_s_game(wife.name)
            print("S遊戲結果：", selected_file)
        else:
            print("無效的選擇！")

    
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
         
            s_game = SGame(self.base_path)
            selected_file = s_game.play_s_game(girl.name)
            print("發生的S遊戲結果：", selected_file)
        else:
            print("咒力不足！")


    
    def open_backend(self):
        """
        打開後台功能，顯示本子中所有妹子的詳細信息，並將咒力增加到999。
        """
        self.mana = 999
        print("後台已打開，咒力增加到999！")
        print("本子中的妹子詳細信息：")
        for girl in self.book:
            print(f"名稱：{girl.name}")
            print(f"與玩家的感情階段：{girl.get_relationship_stage()}")
            male_friends_info = ", ".join([f"{name}: S值 {s_value}" for name, s_value in girl.male_friends.items()])
            print(f"認識的男子：{male_friends_info if male_friends_info else '無'}")
            print(f"行動：{girl.action}")
            print(f"身體特徵：{', '.join(girl.features) if girl.features else '無特徵'}")
            print(f"不滿程度：{girl.displeasure}")
            print(f"興奮程度：{girl.excitement}")
            print("-" * 30)  # 分隔線

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
