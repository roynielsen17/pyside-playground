# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_vars()
        self.connect_events()

    def init_vars(self):
        self.motor_on=QPixmap("img/button1.png")
        self.motor_off=QPixmap("img/button0.png")
        self.stato_motor=0

    def connect_events(self):
        self.ui.button.clicked.connect(self.button_clicked)

    def button_clicked(self, *args):
        self.stato_motor=1-self.stato_motor
        print("motor=",self.stato_motor)
        if self.stato_motor==0:
            self.ui.motor.setPixmap(self.motor_off)
        else:
            self.ui.motor.setPixmap(self.motor_on)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
