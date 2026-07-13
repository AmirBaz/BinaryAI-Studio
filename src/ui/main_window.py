from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
)

from src.ui.menu_bar import create_menu_bar
from src.ui.tool_bar import create_toolbar


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("BinaryAI Studio")

        self.resize(1600, 900)

        create_menu_bar(self)

        create_toolbar(self)

        label = QLabel()

        label.setAlignment(Qt.AlignCenter)

        label.setText("""

<h1>🚀 BinaryAI Studio</h1>

<h2>Intelligent Binary Analysis Platform</h2>

<p>Open Source Edition</p>

""")

        self.setCentralWidget(label)

        self.setStatusBar(QStatusBar())