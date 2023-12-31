class Player:
    def __init__(self):
        self.mana = 100  # 初始咒力

    def cast_spell(self, spell):
        if self.mana >= 20:
            self.mana -= 20
            if spell == "summon":
                print("你成功招喚了一位妹子！")
            elif spell == "manga":
                print("一堆新鮮的本子出現了！")
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
        print("1. 招喚妹子術")
        print("2. 本子術")
        print("3. 充能咒力")
        print("4. 結束遊戲")
        choice = input("請選擇你的行動：")

        if choice == '1':
            player.cast_spell("summon")
        elif choice == '2':
            player.cast_spell("manga")
        elif choice == '3':
            player.recharge()
        elif choice == '4':
            print("遊戲結束。")
            break
        else:
            print("無效的輸入！")

        # 更新畫面
        print("\n畫面更新...\n")

if __name__ == "__main__":
    main()
