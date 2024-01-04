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

# 使用範例
#scanner = FolderScanner("example_folder", "/path/to/base")
#scanner.scan_folder()
#random_file = scanner.get_random_file()
#print("隨機選擇的檔案：", random_file)
