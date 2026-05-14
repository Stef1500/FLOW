# F.L.O.W. - File Live Organizer & Watcher

A lightweight Python application that automatically organizes files inside a selected folder and continuously monitors it for new files.

F.L.O.W. helps users keep their directories clean by sorting files into categorized subfolders based on file extensions.

This project is designed for students, office workers, and anyone who regularly downloads or handle large amounts of files and do not want to manually organize everything.

---

# Features

## Current Core Features

- Select common Windows folders:
  - Desktop
  - Documents
  - Downloads
  - Music
  - Pictures
  - Videos

- Custom folder path support

- Automatic creation of categorized subfolders

- File organization by extension

- Live folder monitoring using the `watchdog` library

- Automatic sorting of newly added files

---

# How It Works

When the program starts:

1. The user selects a folder to organize.
2. The user defines categories and file extensions.
3. The program creates the necessary subfolders.
4. Existing files are organized automatically.
5. Live monitoring starts.
6. Any newly added file is instantly moved to its correct category.

---

# Example

## Before

```text
Downloads/

image.png
song.mp3
notes.pdf
```

## After

```text
Downloads/

Images/
    image.png

Music/
    song.mp3

Documents/
    notes.pdf
```

---

# Project Structure

```text
F.L.O.W/
│
├── main.py
├── FileHandler.py
├── requirements.txt
└── README.md
```

---

# Program Components

## Functions

### `CreateFolder()`

Creates category subfolders inside the selected parent directory.

### `Move_file()`

Moves files into their corresponding categorized folder.

---

## FileHandler Class

Handles all live file monitoring operations.

### Methods

#### `organize_files()`

Scans the selected folder and organizes all files.

#### `on_created()`

Overrides the watchdog event handler method and triggers automatic organization whenever a new file is detected.

---

# Data Stored

The program stores:

- The selected folder path
- File category names
- Associated file extensions

---

# Technologies Used

- Python
- watchdog
- pathlib
- shutil

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/F.L.O.W.git
cd F.L.O.W
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python main.py
```

---

# Future Improvements

- Graphical User Interface (GUI)
- Custom save/load configurations
- Drag-and-drop folder selection
- Multi-folder monitoring
- Cross-platform support
- File duplicate detection
- Automatic cleanup rules

---

# License

This project is for educational purposes.