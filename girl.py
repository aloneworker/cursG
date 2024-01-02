import random

class Girl:
    """
    Girl類別用於表示遊戲中的妹子角色。

    屬性:
        name (str): 妹子的名字。
        features (list): 妹子的特徵列表。
        moods (list): 可能的心情狀態。
        current_mood (str): 當前的心情狀態。
        displeasure (int): 妹子的不滿程度。
        excitement (int): 妹子的興奮程度。
        relationship (int): 與玩家的關係值。
        action (str): 妹子當前的行動。
        male_friends (list): 儲存妹子本子中的男子列表。
    """
    
    RELATIONSHIP_STAGES = ["陌生", "朋友", "情侶", "夫妻"]
    ACTIONS = ["逛街", "工作", "吃飯", "洗澡", "睡覺", "被搭訕"]
    MALE_ACTIONS = ["跟男約會", "跟男聊天"]

    def __init__(self, name="", features=[]):
        self.name = name
        self.features = features
        self.moods = ["閒聊", "無聊", "認真"]
        self.current_mood = random.choice(self.moods)
        self.displeasure = 0
        self.excitement = 0
        self.relationship = 0
        self.action = random.choice(self.ACTIONS)
        self.male_friends = []

    def update_action(self):
        """
        更新妹子的行動。根據當前行動（逛街或工作）決定是否觸發被搭訕事件。
        被搭訕時可能認識新的男子或被帶去酒吧。
        """
        if self.male_friends:
            all_actions = self.ACTIONS + self.MALE_ACTIONS
        else:
            all_actions = self.ACTIONS

        self.action = random.choice(all_actions)

        # 當妹子在逛街或工作時，可能觸發被搭訕事件
        if self.action in ["逛街", "工作"] and random.randint(1, 2) == 1:
            self.action = "被搭訕"
            flirt_random = random.randint(1, 4)
            if flirt_random == 1:  # 1/4的機率認識男子
                male_name = f"男子{len(self.male_friends) + 1}"
                self.male_friends.append(male_name)
                print(f"{self.name}在{self.action}時認識了一位新朋友：{male_name}！")
            elif flirt_random == 2:  # 1/4的機率被帶去酒吧
                self.action = "酒吧"
                print(f"{self.name}被帶去了酒吧。")

    def update_relationship(self):
        """
        根據關係值更新與玩家的關係階段，並檢查是否發生感情升級。

        返回:
            str: 描述感情變化的消息，如果沒有發生變化則返回None。
        """
        previous_stage = self.get_current_relationship_stage()
        if self.relationship > 6:
            current_stage = self.RELATIONSHIP_STAGES[3]  # 夫妻
        elif self.relationship > 4:
            current_stage = self.RELATIONSHIP_STAGES[2]  # 情侶
        elif self.relationship > 2:
            current_stage = self.RELATIONSHIP_STAGES[1]  # 朋友
        else:
            current_stage = self.RELATIONSHIP_STAGES[0]  # 陌生

        if current_stage != previous_stage:
            return f"你和{self.name}的關係升級為{current_stage}了！"
        return None

    def get_current_relationship_stage(self):
        """
        獲取當前的關係階段。

        返回:
            str: 當前的關係階段。
        """
        if self.relationship > 6:
            return self.RELATIONSHIP_STAGES[3]  # 夫妻
        elif self.relationship > 4:
            return self.RELATIONSHIP_STAGES[2]  # 情侶
        elif self.relationship > 2:
            return self.RELATIONSHIP_STAGES[1]  # 朋友
        else:
            return self.RELATIONSHIP_STAGES[0]  # 陌生
    def chat(self, choice):
        """
        與妹子進行聊天。根據玩家選擇的話題和妹子的當前心情，決定聊天的結果。

        參數:
            choice (str): 玩家選擇的聊天話題。

        返回:
            tuple: 包含聊天結果的字符串和一個布爾值，指示妹子是否離開。
        """
        if choice == self.current_mood:
            result = random.choices(["高興", "厭煩", "無感"], weights=[50, 30, 20])[0]
        else:
            result = random.choices(["高興", "厭煩", "無感"], weights=[30, 50, 20])[0]

        if result == "高興":
            self.excitement += 1
            if self.excitement > 3:
                self.relationship += 1
                relationship_stage = self.update_relationship()
                return f"妹子感到高興了！關係增加，現在是{relationship_stage}。妹子離開了。", True
            return "妹子感到高興了！", False
        elif result == "厭煩":
            self.displeasure += 1
            if self.displeasure > 5:
                return "妹子感到厭煩了。妹子離開了。", True
            return "妹子感到厭煩了。", False
        else:
            return "妹子無感。", False


    def leave_check(self):
        """
        檢查妹子是否達到離開的條件。

        返回:
            str: 描述妹子離開的消息，或者問玩家是否要加入本子的提議。
        """
        if self.displeasure > 5:
            return "妹子因為反感太多而離開了。"
        elif self.excitement > 3:
            return "妹子很興奮，問你是否要加入本子。"
        return None
