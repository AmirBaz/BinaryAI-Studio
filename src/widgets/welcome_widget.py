from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WelcomeWidget(QWidget):
    """
    Home page displayed when no binary file is opened.
    """

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("BinaryAI Studio")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            QLabel{
                font-size:30px;
                font-weight:bold;
            }
        """)

        subtitle = QLabel(
            "Modern Binary & Hex Editor powered by AI"
        )

        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle.setStyleSheet("""
            QLabel{
                color:gray;
                font-size:16px;
            }
        """)

        self.open_button = QPushButton("📂 Open Binary File")

        self.open_button.setMinimumHeight(45)

        self.open_button.setMinimumWidth(220)

        layout.addWidget(title)

        layout.addSpacing(15)

        layout.addWidget(subtitle)

        layout.addSpacing(40)

        layout.addWidget(self.open_button)

        self.setLayout(layout)