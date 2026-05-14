import time
from watchdog.observers import Observer
from pathlib import Path
from FileHandler import FileHandler



def CreateFolder(target_folder_path, foldername):

    try:
        Path(f"{target_folder_path}/{foldername}").mkdir(parents=True, exist_ok=True)
    except:
        exit("Error in CreateFolder function")



if __name__ == '__main__':

    default_folder_options = ["Desktop", "Downloads", "Documents", "Music", "Pictures", "Videos"]
    target_folder = ""
    target_folder_path = ""

    print("Select a target folder: ")
    for i in range(len(default_folder_options)):
        print(f"{i+1}. {default_folder_options[i]}")
    option = input("Select a target folder(1-7) or 'custom' to select a custom folder: ")

    if str(option).lower() == "custom":
        custom_folder_name = input("Custom folder name: ")
        custom_folder_path = input("Custom folder path: (example: 'C:/Users\Stefano B\Desktop\Programing courses FSU\Folder': ")
        #check if folder exists in this path
        if Path(custom_folder_path).is_dir():
            print("Folder path found!")
            target_folder = Path(custom_folder_name)
            target_folder_path = Path(custom_folder_path)
        else:
            print("folder path not found.")
            exit()
    else:
        option = int(option)
        target_folder = default_folder_options[option - 1]
        target_folder_path = Path(Path.home() / target_folder)
        print(Path.home())


    print(f"Target folder selected: {target_folder}")
    print("Name subfolders and their corresponding file extensions (/q to stop):")

    new_folders = []



    while True:
        temp = str(input("subfolder name: "))
        if temp.lower() == "/q":
            break

        extensions = []
        while True:
            ext = str(input("file extensions (.txt,.pdf,.png,... (/n to skip): "))
            if ext.lower() == "/n":
                break
            extensions.append(ext)

        new_folders.append((temp, extensions))

    other_folder_flag = False

    tmep = str(input("do you want files not organized to be directed to an 'Other' folder? (y/n): "))
    if tmep.lower() == "y":
        new_folders.append(("Other", []))


    print("*********************************")
    print("Summary: ")
    print("Target Folder: ", target_folder)
    print("SubFolders: ")
    for folder,extensions in new_folders:
        print(f"{folder}: {extensions}")
    print("*********************************")

    print("")
    print(f"Creating folders at {Path.home()/target_folder}....\n")

    for folder,extension in new_folders:
        CreateFolder(target_folder_path, folder)

    observer = Observer()
    handler = FileHandler(target_folder_path,new_folders)

    observer.schedule(handler, target_folder_path, recursive=False)
    observer.start()


    handler.organize_files()
    print("Initial files organized. Starting Live monitoring.")


    while True:
        try:
            time.sleep(0.2)
            handler.organize_files()
        except KeyboardInterrupt:
            observer.stop()


