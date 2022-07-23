"""GUI for test login process"""


import sys
import os
import time
import logging
import logging.config

from PyQt5.QtCore import Qt, QThread, QTimer, QObject, pyqtSignal
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QGridLayout,
                             QWidget,
                             QPushButton)

from login_simple import login_user

class LoginGUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self):
        username_label = QLabel("Username:")
        self.username_line_edit = QLineEdit()

        password_label = QLabel("Password:")
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        run_button = QPushButton()
        run_button.setText("Run Login Process")
        run_button.pressed.connect(self.on_run_button_pressed)

        central_widget = QWidget()

        combined_layout = QGridLayout()

        combined_layout.addWidget(username_label, 0 ,0)
        combined_layout.addWidget(self.username_line_edit, 0, 1)
        combined_layout.addWidget(password_label, 1, 0)
        combined_layout.addWidget(self.password_line_edit, 1, 1)
        combined_layout.addWidget(run_button, 2, 1)

        central_widget.setLayout(combined_layout)

        self.setCentralWidget(central_widget)

    def on_run_button_pressed(self):
        print("Running 'Login' process...")
        un = self.username_line_edit.text()
        pw = self.password_line_edit.text()

        login_user(un, pw)
        print("'Login' process complete!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginGUI()
    window.show()

    app.exec()
