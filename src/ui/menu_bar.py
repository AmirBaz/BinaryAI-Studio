from PySide6.QtGui import QAction


def create_menu_bar(window):

    menu = window.menuBar()

    file_menu = menu.addMenu("&File")

    edit_menu = menu.addMenu("&Edit")

    view_menu = menu.addMenu("&View")

    tools_menu = menu.addMenu("&Tools")

    ai_menu = menu.addMenu("&AI")

    plugins_menu = menu.addMenu("&Plugins")

    help_menu = menu.addMenu("&Help")

    open_action = QAction("Open...", window)

    save_action = QAction("Save", window)

    exit_action = QAction("Exit", window)

    exit_action.triggered.connect(window.close)

    file_menu.addAction(open_action)

    file_menu.addAction(save_action)

    file_menu.addSeparator()

    file_menu.addAction(exit_action)