#F.L.O.W. – File Live Organizer & Watcher

A lightweight Python application that automatically organizes files inside a selected folder and continuously monitors it for new files.
F.L.O.W. helps users keep their directories clean by sorting files into categorized subfolders based on file extensions.

The project is designed for students, office workers, and anyone who regularly downloads or handles large amounts of files and does not want to manually organize them.

Features
Current Core Features
Select common Windows folders:
Desktop
Documents
Downloads
Music
Pictures
Videos
Custom folder path support
Automatic creation of categorized subfolders
File organization by extension
Live folder monitoring using the watchdog library
Automatic sorting of newly added files
How It Works

When the program starts:

The user selects a folder to organize
The user defines categories and file extensions
The program creates the necessary subfolders
Existing files are organized automatically
Live monitoring starts
Any newly added file is instantly moved to its correct category
Example
Before

Downloads/

image.png
song.mp3
notes.pdf
After

Downloads/

Images/
image.png
Music/
song.mp3
Documents/
notes.pdf
Project Structure
F.L.O.W/
│
├── main.py
├── FileHandler.py
├── requirements.txt
└── README.md
Program Components
Functions
CreateFolder()

Creates category subfolders inside the selected parent directory.

Move_file()

Moves files into their corresponding categorized folder.

FileHandler Class

Handles all live file monitoring operations.

Methods
organize_files()

Scans the selected folder and organizes all files.

on_created()

Overrides the watchdog event handler method and triggers automatic organization whenever a new file is detected.

Data Stored

The program stores:

The selected folder path
File category names
Associated file extensions
Technologies Used
Python
watchdog
pathlib
shutil
