
"""
Note: this does not test the model or controller directly, only the view
"""

import sys
import unittest

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest

from view import MainView
from model import MainModel
from controller import MainController

# Ensure QApplication exists
app = QApplication.instance() or QApplication(sys.argv)


class TestMVCSpinBox(unittest.TestCase):

    def setUp(self):
        # ---- Create MVC ----
        self.model = MainModel()
        self.controller = MainController(self.model)
        self.view = MainView(self.model, self.controller)

        # self.view.show()

        # ---- Existing spinBox from View ----
        self.spin = self.view.ui.spinBox_amount
        self.assertIsNotNone(self.spin)

        # Known starting state
        self.view.ui.spinBox_amount.setValue(41)      # or however your model sets it
        self.spin.setFocus()

    def test_spinbox_updates_model(self):
        """
        User presses UP → controller → model updates
        """
        QTest.keyClick(self.spin, Qt.Key_Up)
        # print(self.spin.value())
        self.assertEqual(self.spin.value(), 42)

    def test_model_updates_view(self):
        """
        Model change → controller → view updates spinBox
        """
        self.spin.setValue(5)

        # Let queued signals process
        QTest.qWait(0)

        self.assertEqual(self.spin.value(), 5)

    def test_spinbox_down_updates_model(self):
        self.spin.setValue(3)

        QTest.keyClick(self.spin, Qt.Key_Down)

        self.assertEqual(self.spin.value(), 2)

    def test_multiple_user_steps(self):
        self.spin.setValue(0)
        QTest.keyClick(self.spin, Qt.Key_Up)
        QTest.keyClick(self.spin, Qt.Key_Up)
        QTest.keyClick(self.spin, Qt.Key_Up)

        self.assertEqual(self.spin.value(), 3)


if __name__ == "__main__":
    unittest.main()

