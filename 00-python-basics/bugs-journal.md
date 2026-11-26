# Bugs Journal

A log of every error I hit and how I fixed it.

---

## 2026-11-26 — Day 1: Python 3.14 vs 3.12 PATH confusion

**What broke:** VS Code's "Python: Create Environment" only showed Python 3.14, even though 3.12 was installed.

**Why:** Python 3.12 installer didn't register with VS Code's discovery, likely because 3.14 was installed first and took the default PATH.

**Fix:** Used PowerShell `&` operator with the full path to Python 3.12's executable to create the venv manually (`& "C:\...\Python312\python.exe" -m venv .venv`), then selected it via `Ctrl+Shift+P` → Python: Select Interpreter.

**Lesson:** On Windows with multiple Python versions, use the full path to the specific `python.exe` you want. Don't trust the default `python` command.

---

## 2026-11-26 — Day 1: Committed .venv to GitHub by accident

**What broke:** My first commit pushed the entire `.venv/` folder to GitHub.

**Why:** No `.gitignore` file existed, so Git tracked every file in the project — including the virtual environment which is machine-specific.

**Fix:** Created `.gitignore` with standard Python exclusions. Ran `git rm -r --cached .venv` to untrack the folder without deleting it locally.

**Lesson:** Every new Python project gets a `.gitignore` as the FIRST file created, before anything else.