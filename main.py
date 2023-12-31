class Player:
    def __init__(self):
        self.mana = 100  # 初始咒力

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            print("你發動了一個強大的咒術！")
        else:
            print("咒力不足！")

    def recharge(self):
        self.mana += 20
        print("你的咒力增加了！")

    def get_mana(self):
        return self.mana

def main():
    player = Player()
    while True:
        print(f"\n當前咒力：{player.get_mana()}")
        print("1. 發動咒術")
        print("2. 充能咒力")
        print("3. 結束遊戲")
        choice = input("請選擇你的行動：")

        if choice == '1':
            player.cast_spell()
        elif choice == '2':
            player.recharge()
        elif choice == '3':
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
