import os
import shutil
# Path to organize
source = r"your folder path"
# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".txt",".json"],
    "msoffice": [".doc", ".xls", ".ppt"],
    "archives": [".zip", ".rar", ".tar"],
    "videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "music": [".mp3", ".wav"],
    "web": [".html", ".css", ".js", ".xml"],
    "Python": [".py", ".ipynb"],
    "others":[]
}
for filename in os.listdir(source):
    file_path = os.path.join(source, filename) # Get full file path
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename) # Get file extension
        ext = ext.lower()
        moved = False
        for folder, extensions in file_types.items(): # Iterate through file types
            if ext in extensions:
                folder_path = os.path.join(source, folder) # Create folder path
                os.makedirs(folder_path, exist_ok=True) # Create folder if it doesn't exist
                shutil.move(file_path, os.path.join(folder_path, filename)) # Move file
                print(f"Moved {filename} to {folder}")
                moved = True # Break after moving
                break
        # move any file with an extension not listed (or with no extension) to Others
        if not moved:
            others_folder = os.path.join(source, "others") # Create Others folder
            os.makedirs(others_folder, exist_ok=True) # Create Others folder if it doesn't exist
            shutil.move(file_path, os.path.join(others_folder, filename)) # Move file to Others
            print(f"Moved {filename} to Others")