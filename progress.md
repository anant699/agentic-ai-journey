# My Progress Log

> Where I am, what I did, and what's next. Updated at the end of every learning session so I never lose context between days.

---

## Week 1 — Python Foundations

### Thursday, Nov 26, 2026

**Status:** ✅ Complete

**What I did:**
- Created GitHub repo `agentic-ai-journey`
- Installed Python 3.12 (alongside pre-existing 3.14)
- Installed Git 2.54, configured identity
- Installed VS Code Python extension
- Cloned repo locally, opened in VS Code
- Created virtual environment with Python 3.12
- Wrote and ran first Python script (`hello.py`)
- Created `.gitignore` to exclude `.venv/` from Git
- Created `bugs-journal.md` with 2 entries
- Made first commit, pushed to GitHub

**Key concepts learned:**
- What a virtual environment is and why it matters (isolates per-project packages)
- Why Python 3.14 is too new for AI libraries (LangChain support "coming soon")
- The Git flow: `add` → `commit` → `push`
- Why `.gitignore` matters (keeps machine-specific junk out of the repo)
- PowerShell's `&` operator for running executables from full paths

**Bugs/challenges hit:**
- VS Code didn't detect Python 3.12 → fixed with full-path `&` command
- Accidentally committed `.venv/` → fixed with `git rm -r --cached .venv`

### Thursday, Nov 26, 2026 — Section 0.2 (Variables, Types, Arithmetic)

**Status:** ✅ Complete

**What I did:**
- Read handbook Section 0.2 (Variables, types, and arithmetic)
- Typed every code example into `day1_variables.py` and ran each block
- Changed values and re-ran to see what happens
- Solved the 3 checkpoint exercises in `day1_exercises.py`
- Committed and pushed both files to GitHub

**Key concepts learned:**
- Python infers types automatically — no need to declare them
- Core types: `str` (text), `int` (whole numbers), `float` (decimals), `bool` (True/False), `None`
- Type conversion using `str()`, `int()`, `float()`
- f-strings: `f"Hello {name}"` lets you embed any variable or expression inside a string
- String methods: `.strip()`, `.lower()`, `.upper()`, `.split()`, `.join()`, `.replace()`, `.startswith()`, `len()`
- Arithmetic: `+`, `-`, `*`, `/` (always float), `//` (integer division), `%` (remainder), `**` (power)

**What confused me / what clicked:**
- I thought `day1_variables.py` was broken because running it printed almost nothing. It wasn't — assignment is *silent*, and only `print()` puts anything on screen. Adding a `print()` for each variable made the whole file come alive.
- `"hello".split("l")` returning `['he', '', 'o']` threw me — where did that empty string come from? It clicked when I saw the two `l`s sit next to each other, so the piece *between* them is nothing. Checking `"hello".split("ll")` → `['he', 'o']` confirmed it.
- `age_str` prints as `30`, looking identical to `age`. Only `type()` shows the difference, and that's exactly why `year + 1` works but `age_str + 1` would error.

**Next session:** Day 3 — Functions and control flow (handbook Section 0.3)

---

---