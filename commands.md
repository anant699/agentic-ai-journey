# My Commands Cheatsheet

> Commands I've actually used. What each does. When to reach for it. Added to as I learn.

---

## Git

| Command | What it does | When to use |
|---|---|---|
| `git --version` | Shows installed Git version | Verify Git works |
| `git config --global user.name "X"` | Sets your Git identity name | One-time per machine |
| `git config --global user.email "X"` | Sets your Git identity email | One-time per machine |
| `git clone <url>` | Downloads a repo to your machine | Getting a repo locally for the first time |
| `git status` | Shows what files changed | Before committing, to see what's staged |
| `git add .` | Stages all changes for commit | After editing, before commit |
| `git commit -m "message"` | Saves staged changes with a message | After `git add`, to create a snapshot |
| `git push` | Uploads commits to GitHub | After commit, to sync with remote |
| `git rm -r --cached <folder>` | Untracks a folder without deleting locally | When you accidentally committed something that should be ignored |

## Python

| Command | What it does | When to use |
|---|---|---|
| `python --version` | Shows active Python version | Verify which Python is in use |
| `python script.py` | Runs a Python script | Execute your code |
| `python -m venv .venv` | Creates a virtual environment | Starting a new Python project |
| `py -3.12 -m venv .venv` | Creates venv with specific version (Windows py launcher) | When multiple Pythons are installed |

## Virtual Environment (Windows PowerShell)

| Command | What it does | When to use |
|---|---|---|
| `.venv\Scripts\activate` | Activates the venv | Every new terminal session |
| `deactivate` | Exits the venv | When done, or switching projects |
| `Remove-Item -Recurse -Force .venv` | Deletes the .venv folder | Starting over with a broken venv |

## PowerShell Basics

| Command | What it does | When to use |
|---|---|---|
| `pwd` | Shows current directory | Verify where you are |
| `cd <folder>` | Changes directory | Navigate filesystem |
| `dir` or `ls` | Lists folder contents | See what's in a directory |
| `& "C:\full\path\to.exe" args` | Runs an executable from a full path | When the command isn't on PATH |
| `mkdir <folder>` | Creates a new folder | Set up new directory |

## VS Code Shortcuts

| Shortcut | What it does |
|---|---|
| `Ctrl+Shift+P` | Opens Command Palette (do anything in VS Code) |
| `Ctrl+Shift+` ` | Opens new terminal |
| `Ctrl+` ` | Toggles terminal panel |
| `Ctrl+S` | Save file |
| `Ctrl+Shift+X` | Opens Extensions |

---

*I add to this file every day. If I used a command and had to look it up, it belongs here.*