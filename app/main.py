from __future__ import annotations
import sys
from pathlib import Path
from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QLabel
)
from core.config import load_config, get_log_path
from core import chat

def setup_logging(log_path: Path) -> None:
    logger.remove()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger.add(log_path, rotation="1 MB", encoding="utf-8")
    logger.add(sys.stderr, level="INFO")

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Clone Demo - Day 1")
        self.resize(700, 480)

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("输入你的问题...")
        self.btn_send = QPushButton("发送", self)
        self.btn_play = QPushButton("播放", self)
        self.btn_play.setEnabled(False)  # Day 1: disabled

        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        self.status = QLabel("准备就绪", self)

        top = QHBoxLayout()
        top.addWidget(self.input, stretch=1)
        top.addWidget(self.btn_send)
        top.addWidget(self.btn_play)

        layout = QVBoxLayout()
        layout.addLayout(top)
        layout.addWidget(self.output, stretch=1)
        layout.addWidget(self.status)
        self.setLayout(layout)

        self.btn_send.clicked.connect(self.on_send_clicked)

    def on_send_clicked(self) -> None:
        text = self.input.text().strip()
        if not text:
            self.status.setText("请输入内容再发送。")
            return
        self.status.setText("发送中...")
        logger.info(f"User prompt: {text}")
        try:
            reply = chat.ask(text)  # Day 1: stub
            self.output.append(f"你：{text}")
            self.output.append(f"答：{reply}")
            self.output.append("")
            self.status.setText("完成")
        except Exception as e:
            logger.exception("Chat error")
            self.status.setText(f"出错：{e}")

def main() -> int:
    cfg = load_config()
    setup_logging(get_log_path(cfg))
    logger.info("App starting")
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    ret = app.exec()
    logger.info("App exit")
    return ret

if __name__ == "__main__":
    raise SystemExit(main())
