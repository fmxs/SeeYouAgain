from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG = {
    "app_name": "Clone Demo",
    "log_path": "data/logs/app.log",
    "theme": "light",
    "llm": {"provider": "online_stub", "api_base": "", "api_key": ""},
    "tts": {"provider": "stub", "voice_profile": ""},
}

def load_config(path: str | Path = "config.json") -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        # write default
        p.write_text(json.dumps(DEFAULT_CONFIG, indent=2), encoding="utf-8")
        return DEFAULT_CONFIG.copy()
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return DEFAULT_CONFIG.copy()

def get_log_path(cfg: Dict[str, Any]) -> Path:
    p = Path(cfg.get("log_path", "data/logs/app.log"))
    p.parent.mkdir(parents=True, exist_ok=True)
    return p
