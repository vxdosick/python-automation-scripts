import os
from pathlib import Path
import shutil

folder_path = input("Enter folder path please: ")
files = os.listdir(folder_path)


images = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"]
documents = [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"]
videos = [".mp4", ".mkv", ".avi", ".mov", ".webm"]
audio = [".mp3", ".wav", ".flac", ".m4a"]
archives = [".zip", ".rar", ".tar", ".gz", ".7z"]

for file in files:
    file_path = os.path.join(folder_path, file)
    file_suffix = Path(file).suffix

    if not os.path.isfile(file_path):
        continue

    if file_suffix in images:
        if not os.path.exists(folder_path + "/images"):
            os.mkdir(folder_path + "/images")
        shutil.move(file_path, folder_path + "/images")
    elif file_suffix in documents:
        if not os.path.exists(folder_path + "/documents"):
            os.mkdir(folder_path + "/documents")
        shutil.move(file_path, folder_path + "/documents")
    elif file_suffix in videos:
        if not os.path.exists(folder_path + "/videos"):
            os.mkdir(folder_path + "/videos")
        shutil.move(file_path, folder_path + "/videos")
    elif file_suffix in audio:
        if not os.path.exists(folder_path + "/audio"):
            os.mkdir(folder_path + "/audio")
        shutil.move(file_path, folder_path + "/audio")
    elif file_suffix in archives:
        if not os.path.exists(folder_path + "/archives"):
            os.mkdir(folder_path + "/archives")
        shutil.move(file_path, folder_path + "/archives")
    else:
        if not os.path.exists(folder_path + "/other"):
            os.mkdir(folder_path + "/other")
        shutil.move(file_path, folder_path + "/other")
print("Finish")

