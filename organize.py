import os
import shutil

def organize_desktop():
    # Get the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    print(desktop_path)
    # Define the categories and their associated file extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".xls", ".csv", ".rtf"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
        "Others": []  # Any uncategorized files will go here
    }
    
    # Create subfolders if they do not exist
    for folder in categories:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files into the subfolders
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)
        
        # Skip directories and this script file itself
        if os.path.isdir(file_path) or file_name == os.path.basename(__file__):
            continue
        
        # Find the appropriate category
        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(desktop_path, category, file_name))
                moved = True
                break
        
        # Move uncategorized files to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(desktop_path, "Others", file_name))

    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()