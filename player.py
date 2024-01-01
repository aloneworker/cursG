class Player:
    """
    Player類別用於表示遊戲中的玩家角色。

    屬性:
        mana (int): 玩家的咒力值。
        book (list): 存儲本子中的妹子列表。
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
            girl (Girl): 要加入本子的妹子對象。
        """
        self.book.append(girl)

    def cast_book_spell(self):
        """
        使用本子術查看本子中的妹子。

        返回:
            bool: 本子術是否成功執行。
        """
        if self.mana >= 3 and self.book:
            self.mana -= 3
            for index, girl in enumerate(self.book):
                girl.update_action()
                print(f"{index + 1}. {girl.name} - {girl.update_relationship()} - 正在{girl.action}")
            return True
        else:
            print("咒力不足或本子中沒有妹子！")
            return False

    def get_mana(self):
        """
        獲取玩家當前的咒力值。

        返回:
            int: 當前咒力值。
        """
        return self.mana