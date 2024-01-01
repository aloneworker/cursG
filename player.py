from girl import Girl

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
                relationship_stage = girl.update_relationship()
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
    def interact_with_girl(self, girl):
        """
        與本子中的妹子互動。

        參數:
            girl (Girl): 要互動的妹子對象。
        """
        print(f"與{girl.name}互動：")
        print("1. 聊天 (消耗5點咒力)")
        if girl.relationship > 1:  # 如果是朋友或情侶
            print("2. 約會 (消耗20點咒力)")

        choice = input("選擇你的行動：")
        if choice == '1':
            if self.mana >= 5:
                self.mana -= 5
                mood = input("選擇聊天話題 (閒聊/認真)：")
                chat_result, leave = girl.chat(mood)
                print(chat_result)
            else:
                print("咒力不足！")
        elif choice == '2' and girl.relationship > 1:
            if self.mana >= 20:
                self.mana -= 20
                girl.relationship += 2  # 增加關係值
                print(f"你和{girl.name}進行了愉快的約會，你們的關係更進一步了。")
            else:
                print("咒力不足！")


    def get_mana(self):
        """
        獲取玩家當前的咒力值。

        返回:
            int: 當前咒力值。
        """
        return self.mana
