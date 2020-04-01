import json
import os
from pydm import Display
from qtpy.QtWidgets import (QVBoxLayout, QHBoxLayout, QGroupBox,
                            QLabel, QLineEdit, QPushButton, QScrollArea, QFrame,
                            QApplication, QWidget)
from qtpy import QtCore
from pydm.widgets import PyDMEmbeddedDisplay

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))


class AllMotors(Display):
    def __init__(self, parent=None, args=[], macros=None):
        super(AllMotors, self).__init__(parent=parent, args=args, macros=None)
        self.app = QApplication.instance()
        self.results_layout = None
        self.frm_result = None
        self.all_motor_layout = None
        self.motors = []
        self.load_motors()
        self.setup_ui()
        self.show_motors()

    def ui_filepath(self):
        return None

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        lbl_title = QLabel("Motor Parameters")
        lbl_title.setStyleSheet("\
                    QLabel {\
                        qproperty-alignment: AlignCenter;\
                        max-height: 25px;\
                        font-size: 14px;\
                    }")
        main_layout.addWidget(lbl_title)
        self.results_layout = QVBoxLayout()
        self.results_layout.setContentsMargins(0, 0, 0, 0)

        # Create a Frame to host the results of search
        self.frm_result = QFrame(parent=self)
        self.frm_result.setLayout(self.results_layout)

        # Create a ScrollArea so we can properly handle
        # many entries
        scroll_area = QScrollArea(parent=self)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)

        # Add the Frame to the scroll area
        scroll_area.setWidget(self.frm_result)

        # Add the scroll area to the main layout
        main_layout.addWidget(scroll_area)

    def load_motors(self):
        self.motors = ['sample_stage.x', 'sample_stage.y', 'sample_stage.z']

    def show_motors(self):
        for m in self.motors:
            disp = PyDMEmbeddedDisplay(parent=self)
            disp.macros = json.dumps({"MOTOR": m})
            if os.path.exists(os.path.join(LOCAL_PATH, 'motors.ui')):
                disp.filename = os.path.join(LOCAL_PATH, 'motors.ui')
            disp.setMinimumWidth(300)
            disp.setMinimumHeight(24)
            disp.setMaximumHeight(30)
            # Add the Embedded Display to the Results Layout
            self.results_layout.addWidget(disp)
