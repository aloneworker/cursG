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
        male_friends (list): 妹子本子中的男性朋友列表。
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
        更新妹子的行動，如果有男性朋友，則增加與男性朋友互動的行動選項。
        """
        if self.male_friends:
            all_actions = self.ACTIONS + self.MALE_ACTIONS
        else:
            all_actions = self.ACTIONS

        self.action = random.choice(all_actions)
        if self.action == "被搭訕" and random.randint(1, 3) == 1:
            male_name = f"男子{len(self.male_friends) + 1}"
            self.male_friends.append(male_name)

    def update_relationship(self):
        """
        根據關係值更新與玩家的關係階段。

        返回:
            str: 當前關係階段。
        """
        if self.relationship > 6:
            return self.RELATIONSHIP_STAGES[3]  # 夫妻
        elif self.relationship > 4:
            return self.RELATIONSHIP_STAGES[2]  # 情侶
        elif self.relationship > 2:
            return self.RELATIONSHIP_STAGES[1]  # 朋友
        else:
            return self.RELATIONSHIP_STAGES[0]  # 陌生

    # 聊天和離開檢查方法保持不變
