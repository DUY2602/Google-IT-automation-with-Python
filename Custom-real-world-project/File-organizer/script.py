import os
import shutil
import tkinter as tk
from tkinter import filedialog


extension_dict = {
    'Images': ['jpg', 'jpeg', 'png', 'svg'],
    'Documents': ['doc', 'docx', 'ppt', 'txt'],
    'Data': ['csv', 'sql', 'json'],
    'Audio & Video': ['mp3', 'mp4'],
    'Application': ['apk', 'exe'] 
}

def ext_to_dir(file):
    extension = file.rsplit(".", 1)[-1].lower()
    for directory, exts in extension_dict.items():
        if extension in exts:
            return directory
    return None

def file_organizer(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if not os.path.isfile(item_path):
            continue

        folder = ext_to_dir(item)

        if folder:
            full_path = os.path.join(directory, folder)
            if not os.path.exists(full_path):
                os.mkdir(full_path)

            shutil.move(item_path, full_path)    

# A simple GUI using tkinter to help user select directory more easily
def main():
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính

    # Mở hộp thoại chọn thư mục
    selected_directory = filedialog.askdirectory(title="Chọn thư mục gốc để tổ chức file")

    print("Folder bạn chọn là:", selected_directory)
    file_organizer(selected_directory)


if __name__ == "__main__":
    main()