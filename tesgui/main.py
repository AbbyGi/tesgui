import os
import sys
import json

from pydm.widgets import PyDMEmbeddedDisplay

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5 import uic

import time
from os import path
from pydm import Display


class MainScreen(Display):
    def __init__(self, parent=None, args=None):
        super(MainScreen, self).__init__(parent=parent, args=args)
        self.ui.PyDMEmbeddedDisplay.filename = 'motor_params.py'
        # # Attach our custom process_image method
        # self.ui.imageView.process_image = self.process_image
        # # Hook up to the newImageSignal so we can update
        # # our widgets after the new image is done
        # self.ui.imageView.newImageSignal.connect(self.show_blob)
        # # Store blob coordinate
        # self.blob = (0, 0)

    def ui_filename(self):
        # Point to our UI file
        return 'main.ui'

    def ui_filepath(self):
        # Return the full path to the UI file
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())
