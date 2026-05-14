from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil #move files
from random import randint
import time


def move_file(file, target_folder):
    try:
        shutil.move(file, target_folder)
    except Exception as e:
        exit(f"Error in MoveFile function: {e}")


class FileHandler(FileSystemEventHandler):

    def __init__(self, target_folder_path,subfolders):
        self.target_folder_path = target_folder_path
        self.subfolders = subfolders

    def organize_files(self):

        files = self.target_folder_path.iterdir()
        for file in files:
            if file.name == "desktop.ini":
                continue
            if file.is_file():
                for folder, extensions in self.subfolders:
                    if file.suffix in extensions:
                        files2 = (self.target_folder_path / folder).iterdir()
                        for file2 in files2:
                            if file2.name == file.name:
                                try:
                                    new_name = str(file.stem) + f" (DUPLICATE{randint(1, 10000)}){file.suffix}"
                                    new_file = self.target_folder_path / new_name

                                    file.rename(new_file)
                                    file = new_file

                                    print(f"{file2.name} duplicate detected, changing, file name to {file.name}.")
                                    time.sleep(0.5)
                                except Exception as e:
                                    print(f"Warning: {e}, Aborting operation.")
                        folder_path = Path(self.target_folder_path / folder)
                        move_file(file, folder_path)
                        print(f"-------  Moved file {file.name} -------")
                if ("Other", []) in self.subfolders and file in self.target_folder_path.iterdir():
                    folder_path = Path(self.target_folder_path / "Other")
                    move_file(file, folder_path)




    def on_created(self, event):
        if event.is_directory:
            return None

        file_path = Path(event.src_path)
        file_count = sum(1 for item in self.target_folder_path.iterdir() if item.is_file() and item.name != "desktop.ini")
        print(f"{file_count} files detected at {self.target_folder_path} \n")

        self.organize_files()

        print(f"New file detected at {file_path}=, {file_path.name}")
