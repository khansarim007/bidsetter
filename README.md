# Bidsetter MVP Preview

## Quick start (Windows)

Your screenshot shows this error:

- `Python was not found...`

That means Python is not installed (or not on PATH) yet.

### 1) Install Python

1. Download Python 3.11+ from: https://www.python.org/downloads/windows/
2. During install, **check**: `Add python.exe to PATH`
3. Re-open Command Prompt after install.

### 2) Verify Python works

Use either command (depending on your setup):

```bat
py --version
```

or

```bat
python --version
```

If both fail, disable the Microsoft Store alias:

- **Settings → Apps → Advanced app settings → App execution aliases**
- Turn off aliases for `python.exe` and `python3.exe`

### 3) Install dependencies and run

```bat
py -m pip install -r requirements.txt
py app.py
```

Then open:

- http://localhost:3000

---

## Quick start (macOS/Linux)

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

Then open:

- http://localhost:3000

---

## Notes

- This app binds to `0.0.0.0` and reads `PORT` (defaults to `3000`) so side-preview panes can detect it.
- In your screenshot, one line ran as `python app.pypython -m pip ...` which is two commands accidentally merged. Run one command per line.


---

## Using Codex Web

If you are using Codex in a web chat UI, there is usually **no built-in live app host/preview panel** for this repo by default.

What Codex can do:
- write/edit code
- run terminal commands in its environment

What Codex web chat usually cannot do automatically:
- open a persistent browser preview of your Flask app inside your own chat window

So if you want to interact with the app visually, you still need one of these:
- run it locally (`py app.py` / `python3 app.py`)
- run it on a hosted dev environment (Replit, Render, Railway, etc.)
