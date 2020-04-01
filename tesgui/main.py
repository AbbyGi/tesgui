import os
import sys
import json

from pydm.widgets import PyDMEmbeddedDisplay

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow)
from PyQt5 import uic

import time
from pydm import Display

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
print(LOCAL_PATH)
print(os.path.join(LOCAL_PATH, 'motor_params.py'))


class MainScreen(Display):
    def __init__(self, parent=None, args=None):
        super(MainScreen, self).__init__(parent=parent, args=args)
        # super(MainScreen, self).__init__(parent=parent)
        self.ui_file = self.ui_filepath()

        if os.path.exists(os.path.join(LOCAL_PATH, 'motor_params.py')):
            print(self.ui.embedded_motors.filename)
            self.ui.embedded_motors.filename = os.path.join(LOCAL_PATH, 'motor_params.py')
            print(self.ui.embedded_motors.filename)
        else:
            print("can't find motors file")
        if os.path.exists(os.path.join(LOCAL_PATH, 'de_params.ui')):
            print(self.ui.embedded_de_params.filename)
            self.ui.embedded_de_params.filename = os.path.join(LOCAL_PATH, 'de_params.ui')
        else:
            print("can't find de_params file")
        if os.path.exists(os.path.join(LOCAL_PATH, 'det_params.ui')):
            print(self.ui.embedded_det_params.filename)
            self.ui.embedded_det_params.filename = os.path.join(LOCAL_PATH, 'det_params.ui')
        else:
            print("can't find det_params file")
        if os.path.exists(os.path.join(LOCAL_PATH, 'execution.ui')):
            print(self.ui.embedded_exe.filename)
            self.ui.embedded_exe.filename = os.path.join(LOCAL_PATH, 'execution.ui')
        else:
            print("can't find execution file")
        uic.loadUi(self.ui_filepath(), self)
        self.show()

    def ui_filename(self):
        # Point to our UI file
        return 'main.ui'

    def ui_filepath(self):
        # Return the full path to the UI file
        if os.path.exists(os.path.join(LOCAL_PATH, self.ui_filename())):
            print(os.path.join(LOCAL_PATH, self.ui_filename()))
            return os.path.join(LOCAL_PATH, self.ui_filename())
        else:
            print('bad')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainScreen()
    myapp.show()
    sys.exit(app.exec_())
