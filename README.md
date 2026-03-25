# 🎬 YT Manager CLI

> A clean and interactive **Command Line YouTube Video Manager** built in Python with a professional terminal UI.

---

## Features

-  View all stored YouTube videos  
-  Add new videos with details  
-  Update existing video information  
-  Delete videos easily  
-  Smooth CLI flow with continue/exit control  
-  Persistent storage using JSON  

---

## Tech Stack

- **Python 3**
- **JSON File Handling**
- **CLI (Terminal UI Design)**

---

## 📂 Project Structure

yt-manager/
│
├── main.py # Main application file
├── videos.json # Data storage (auto-created)
└── README.md


---

## UI Preview

==================================================
                 🎬 YT MANAGER
==================================================

1. List Videos
2. Add Video
3. Update Video
4. Delete Video
5. Exit


##  Example Output

➕ Add Video
Enter Title   : Python Tutorial
Enter Channel : DevGoel
Enter Views   : 12000

✅ Video Added Successfully!


## 📋 List Videos

1. Python Tutorial
   Channel : DevGoel
   Views   : 12000

## ❌ Delete Video

1. Python Tutorial
0. Cancel

🗑️ Deleted: Python Tutorial


## 🧾 Data Format

Stored inside videos.json:

[
    {
        "title": "Python Tutorial",
        "channel": "DevGoel",
        "views": 12000
    }
]




---

This one is **proper GitHub-ready** — formatting, spacing, code blocks all fixed.  

If you want next level:
👉 badges (stars, forks, python version)  
