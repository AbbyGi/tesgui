import os
import sys
import json
from pydm import Display
from qtpy.QtWidgets import (QVBoxLayout, QHBoxLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QScrollArea, QFrame,
    QApplication, QWidget)

from pydm.widgets import PyDMEmbeddedDisplay

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5 import uic

form, base = uic.loadUiType('MainWindow.ui')


class MainWidget(base, form):

    def __init__(self):
        super(base, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
