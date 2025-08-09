# Clone Demo - Day 1 (PySide6)

This is the **Day 1** scaffold for your cross-platform demo (macOS/Windows). 
It gives you a minimal PySide6 app window with logging and config loading in place.

## Structure
```
demo/
  app/
    main.py            # PySide6 UI entry
  core/
    config.py          # load/save config
    chat.py            # (stub) LLM adapter
    tts.py             # (stub) TTS adapter
    store.py           # (stub) persistence
  assets/              # avatars, sample audio
  data/
    logs/              # log files
  tests/
  requirements.txt
  config.json
  README.md
```

## Quickstart

### 1) Create & activate venv
**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2) Install deps
```bash
pip install -r requirements.txt
```

### 3) Run
```bash
python app/main.py
```

You should see a window with:
- a text input
- a "Send" button (no-op for now)
- a disabled "Play" button
- a log file at `data/logs/app.log`

## Next steps (Day 2 preview)
- Implement `core/chat.py: ask(prompt)->str`
- Wire the UI "Send" button to call `ask` and render response.
