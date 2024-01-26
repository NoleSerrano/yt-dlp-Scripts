import os
import shutil
import sys

def move_files_to_parent_folder(parent_folder):
    """Move all files from subfolders to the parent folder."""
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    shutil.move(file_path, parent_folder)
                    print(f"Moved {file_name} to {parent_folder}")

            # Optionally, remove the empty folder
            os.rmdir(folder_path)
            print(f"Removed empty folder: {folder_name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_folder>")
        sys.exit(1)

    parent_folder = sys.argv[1]
    if not os.path.exists(parent_folder) or not os.path.isdir(parent_folder):
        print(f"Error: {parent_folder} is not a valid directory")
        sys.exit(1)

    move_files_to_parent_folder(parent_folder)

if __name__ == "__main__":
    main()
