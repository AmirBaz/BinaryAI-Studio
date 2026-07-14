import sys

from PySide6.QtWidgets import QApplication

from src.ui.widgets.welcome_widget import WelcomeWidget

app = QApplication(sys.argv)

window = WelcomeWidget()

window.resize(700,500)

window.show()

app.exec()