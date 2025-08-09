from __future__ import annotations

def ask(prompt: str) -> str:
    """
    Day 1 stub: returns a canned response.
    Day 2: replace with real LLM call (online or local).
    """
    prompt = (prompt or "").strip()
    if not prompt:
        return "（空输入）请先输入一个问题。"
    return f"【占位回复】你问了：{prompt}。这里将返回模型的回答。"
