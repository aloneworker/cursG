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
    DELY = [
        "我...我不太確定這是個好主意...",
        "或許我們可以嘗試些別的？",
        "我覺得我還不太準備好這個...",
        "這可能不是最好的時機...",
        "對不起，我今天不太舒服。",
        "我不確定這是否合適...",
        "可能現在還不是時候吧。",
        "我...我不確定...",
        "讓我們保持現狀如何？",
        "或許不是現在...",
        "我覺得我需要更多時間去考慮。",
        "這對我來說有點太快了。",
        "我不確定我是否準備好這個步驟。",
        "我今天不太想這樣做。",
        "或許我們可以先停一停？",
        "我覺得我們應該再等等。",
        "讓我們先不要這樣好嗎？",
        "我需要一點時間來思考。",
        "讓我們保持一點距離如何？",
        "我覺得我們可以先做些別的。",
        "嗯...不，不行...我不確定...",
        "啊...也許...也許不應該吧...",
        "嗯，我...我不太確定這個...",
        "啊...這...這可能不太好...",
        "我...我覺得...可能不行...",
        "或許...或許我們不應該這樣...",
        "我...我還不太準備好...",
        "或許...我們應該停下來？",
        "這...這樣好嗎？我不太確定...",
        "我...我不太確定這是否合適...",
        "嗯...不...我們...我們或許不應該...",
        "我...我還需要一點時間...",
        "我不確定...這是個好主意...",
        "啊...也許我們可以...嗯...不...",
        "我...我不太確定...嗯...",
        "這...這對我來說...有點太快了...",
        "我覺得...我們應該...應該等等...",
        "或許我們...可以先不...嗯...",
        "我...我覺得我們可以...也許不行...",
        "我...我覺得我們應該先...先停下..."
    ]
    AGAR = [
    "嗯...好吧，就這樣吧...",
    "如果你喜歡的話，可以的。",
    "嗯，我想試試看。",
    "好吧，就讓你這麼做吧。",
    "我想這樣應該沒問題。",
    "好吧，就照你的方式吧。",
    "如果你真的想要，那就這樣吧。",
    "我...我覺得可以嘗試。",
    "好吧，我信任你。",
    "嗯，就這樣做吧。",
    "如果這能讓你開心，那就好。",
    "嗯，我想這是可以的。",
    "好吧，讓我們這麼做。",
    "我覺得我們可以試試。",
    "只要是你想要的，我都願意。",
    "嗯，我覺得我們可以這樣。",
    "好吧，就按你的想法來。",
    "如果這會讓你高興，那就這麼做吧。",
    "好的，我覺得沒問題。",
    "只要你小心點，那就行。",
    "嗯...可以...可以的...",
    "啊...好吧...就這樣...",
    "啊...嗯...可以...",
    "好...好的...就這樣...",
    "嗯...我...我想可以...",
    "好吧...嗯...可以...",
    "如果...你喜歡...那就...",
    "嗯...嗯...可以的...",
    "我...我覺得...嗯...可以...",
    "好...好的...我...我同意...",
    "如果...這樣...你會開心的話...",
    "嗯...我...我覺得沒問題...",
    "好...好吧...讓...讓我們這樣吧...",
    "我...我覺得...我們可以試試...",
    "只要...是你...我...我都願意...",
    "嗯...這樣...這樣也好...",
    "好的...好的...我...我同意...",
    "如果...這會...讓你高興...那就...",
    "好...好的...沒問題...",
    "只要...你小心點...那就...那就好..."
]
    def __init__(self, name="", features=[]):
        self.name = name
        self.features = features
        self.moods = ["閒聊", "無聊", "認真"]
        self.current_mood = random.choice(self.moods)
        self.displeasure = 0
        self.excitement = 0
        self.relationship_stage = "陌生"
        self.relationship = 0
        self.current_action = random.choice(self.ACTIONS)
        self.male_friends = {}  # 將male_friends定義為字典
        self.s_actions = []  # 新增用於儲存S動作的屬性
        self.子宮 = []  # 新增子宮陣列屬性

    
    def update_action(self):
        """
        更新妹子的行動。
        """
        all_actions = self.ACTIONS.copy()  # 複製原有行動列表

        for male_name, relationship in self.male_friends.items():
            if random.randint(1, 10) == 1:  # 1/10的機會約會
                self.current_action = "跟男子約會"
                break

        # 根據當前行動更新下一個行動
        if self.current_action == "跟男子約會":
            if random.randint(1, 10) == 1:
                self.current_action = "被下藥S"
            elif random.randint(1, 5) == 1:
                self.current_action = "去酒吧"
            else:
                self.current_action = random.choice(all_actions)
        elif self.current_action == "被下藥S":
            self.子宮.append(male_name)  # 將男子名字加入子宮
            if random.randint(1, 3) != 1:  # 2/3機會繼續"被下藥S"
                self.evaluate_mating(male_name)  # 評估交配結果
            else:
                self.current_action = random.choice(all_actions)
        else:
            self.current_action = random.choice(all_actions)

            # 檢查是否有關係值超過90的男子，若有，增加約炮行為
            if any(value > 90 for value in self.male_friends.values()):
                all_actions.append("約炮")
                all_actions.append("約炮")

        if self.current_action == "去酒吧":
            if random.randint(1, 2) == 1:
                self.current_action = "酒醉交配"
            else:
                self.current_action = random.choice(all_actions)
        elif self.current_action == "酒醉交配":
            if random.randint(1, 2) != 1:  # 有1/3的機會繼續酒醉交配
                self.current_action = random.choice(all_actions)
            else:
                self.drunk_mating()  # 繼續酒醉交配      

        elif self.current_action in ["逛街", "工作"]:
            if random.randint(1, 4) == 1:
                self.current_action = "被搭訕"
            else:
                 self.current_action = random.choice(all_actions)
        elif self.current_action == "被搭訕":
            if random.randint(1, 4) == 1:
                male_name = "男子" + str(len(self.male_friends) + 1)
                if len(self.male_friends) < 20 :
                    self.male_friends[male_name] = 1
            elif random.randint(1, 4) == 1:
                self.current_action = "去酒吧"
            else:
                 self.current_action = random.choice(all_actions)
        else:
             self.current_action = random.choice(all_actions)
 


    def drunk_mating(self):
        """
        執行酒醉交配的功能。
        """
        male_name = "男子" + str(len(self.male_friends) + 1)
        if random.randint(1, 3) == 1:
            self.子宮.append(male_name)

        self.evaluate_mating(male_name)

    def evaluate_mating(self, male_name):
        """
        評估酒醉交配後的結果。

        參數:
            male_name (str): 交配中的男子名稱。
        """
        if self.子宮.count(male_name) > 5:
            self.male_friends[male_name] = 999
        else:
            self.male_friends[male_name] = 1



    
    def decide_internal_finish(self, player_name):
        """
        決定是否允許玩家射在裡面。

        參數:
            player_name (str): 玩家的名字。

        返回:
            bool: 是否允許射在裡面。
        """

        response = ""
        allowed = False
        agrees = ["有些恍神","朦朧的看著你","點頭","親了你一下","抱著你"]
        dellys = ["低著頭","搖搖頭","親了你一下","害羞的看著其他地方","雙手撐著你的胸口稍微後退了一下"]
 
        mind = ""
        if len(self.子宮) >= 5:
            response = random.choice(Girl.DELY)
            mind = random.choice(dellys)
            allowed = False
        elif self.relationship_stage == "情侶":
            if any(name != player_name for name in self.子宮):
                allowed = random.randint(1, 5) != 1
            else:
                allowed = random.randint(1, 3) != 1
        elif self.relationship_stage == "夫妻":
            if any(name != player_name for name in self.子宮):
                allowed = random.randint(1, 5) != 1
            else:
                allowed = random.randint(1, 5) == 1

        if allowed:
            response = random.choice(Girl.AGAR)
            mind = random.choice(agrees)
        else:
            if not response:  # 如果還沒有設置回應
                mind = random.choice(dellys)
                response = random.choice(Girl.DELY)
        print(self.name+mind)
        print("[{}]".format(response))
        return allowed

    def update_relationship(self):
        """
        根據關係值更新與玩家的關係階段。
        """
        if self.relationship_stage == "陌生" and self.relationship > 2:
            self.relationship_stage = "朋友"
            self.relationship = 0  # 清除關係值
            return "升級為朋友"
        elif self.relationship_stage == "情侶" and self.relationship > 4:
            # 等待求婚
            pass
        elif self.relationship_stage == "朋友" and self.relationship > 3:
            # 等待告白
            pass
        return None

    
    def get_relationship_stage(self):
        """
        獲取當前的關係階段。

        返回:
            str: 當前的關係階段。
        """
        # 使用 self.relationship_stage 直接返回當前的關係階段
        return self.relationship_stage
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
                relationship_message = self.update_relationship()  # 更新關係階段
                relationship_stage = self.get_relationship_stage()  # 獲取當前的關係階段
                return f"妹子感到高興了！關係增加，現在是{relationship_stage}階段。妹子離開了。", True
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
