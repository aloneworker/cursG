import os
import random

class FolderScanner:
    def __init__(self, folder_name, base_path="."):
        """
        初始化FolderScanner類。

        參數:
            folder_name (str): 要掃描的資料夾名稱。
            base_path (str): 資料夾的基礎路徑。默認為當前目錄。
        """
        self.folder_name = folder_name
        self.base_path = base_path
        self.files = []

    def scan_folder(self):
        """
        掃描指定資料夾中的檔案。
        """
        folder_path = os.path.join(self.base_path, self.folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            self.files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            print("指定的資料夾不存在或不是一個有效的資料夾。")

    def get_random_file(self):
        """
        從掃描結果中隨機選擇一個檔案。

        返回:
            str: 隨機選擇的檔案名稱。如果沒有檔案，返回None。
        """
        if self.files:
            return random.choice(self.files)
        else:
            print("沒有可用的檔案。")
            return None



class SGame:
    def __init__(self, base_path="."):
        """
        初始化SGame類。

        參數:
            base_path (str): 基礎路徑。默認為當前目錄。
        """
        self.base_path = base_path


    def play_s_game(self, girl):
        """
        執行S遊戲。

        參數:
            girl (Girl): 參與S遊戲的妹子對象。

        返回:
            str: 隨機選擇的檔案名稱。如果沒有檔案，返回None。
        """
        # 如果妹子的S動作輯中有檔案，則有4/5的機會使用這些檔案
        if girl.s_actions and random.randint(1, 5) != 1:
            return random.choice(girl.s_actions)

        # 從S檔案夾中隨機選取一個檔案
        s_folder_scanner = FolderScanner("S", self.base_path)
        s_folder_scanner.scan_folder()
        s_file = s_folder_scanner.get_random_file()

        # 檢查是否存在與人名對應的S資料夾
        person_s_folder_scanner = FolderScanner(f"{girl.name}S", self.base_path)
        person_s_folder_scanner.scan_folder()
        person_s_file = person_s_folder_scanner.get_random_file()

        # 從上述兩個檔案中隨機選擇一個
        available_files = [f for f in [s_file, person_s_file] if f]
        if available_files:
            selected_file = random.choice(available_files)
            girl.s_actions.append(selected_file)  # 將選擇的檔案添加到S動作輯中
            return selected_file
        else:
            print("沒有可用的檔案。")
            return None

# 使用範例
#scanner = FolderScanner("example_folder", "/path/to/base")
#scanner.scan_folder()
#random_file = scanner.get_random_file()
#print("隨機選擇的檔案：", random_file)




# 使用範例
#s_game = SGame("/path/to/base")
#selected_file = s_game.play_s_game("John")
#print("隨機選擇的檔案：", selected_file)
