from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


def create_toolbar(window):

    toolbar = QToolBar("Main Toolbar")

    toolbar.setMovable(False)

    toolbar.setFloatable(False)

    toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    open_action = QAction("Open", window)

    save_action = QAction("Save", window)

    search_action = QAction("Search", window)

    ai_action = QAction("AI", window)

    toolbar.addAction(open_action)

    toolbar.addAction(save_action)

    toolbar.addSeparator()

    toolbar.addAction(search_action)

    toolbar.addSeparator()

    toolbar.addAction(ai_action)

    window.addToolBar(toolbar)