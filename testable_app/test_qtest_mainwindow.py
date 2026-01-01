import unittest
from PySide6.QtWidgets import QApplication
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt
from mainwindow import MainWindow

# Ensure QApplication is created only once
app = QApplication.instance() or QApplication([])

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.window = MainWindow()

    def test_initial_state(self):
        self.assertEqual(self.window.ui.lbl_number.text(), "42")
        self.assertIn("color: green", self.window.ui.lbl_number.styleSheet())

    def test_inc_button(self):
        QTest.mouseClick(self.window.ui.btnInc, Qt.LeftButton)
        self.assertEqual(self.window.ui.lbl_number.text(), "43")
        self.assertIn("color: red", self.window.ui.lbl_number.styleSheet())

    def test_dec_button(self):
        QTest.mouseClick(self.window.ui.btnDec, Qt.LeftButton)
        self.assertEqual(self.window.ui.lbl_number.text(), "41")
        self.assertIn("color: red", self.window.ui.lbl_number.styleSheet())

    def test_fail_inc_button(self):
        QTest.mouseClick(self.window.ui.btnInc, Qt.LeftButton)
        self.assertNotEqual(self.window.ui.lbl_number.text(), "53")
        self.assertIn("color: red", self.window.ui.lbl_number.styleSheet())

    def test_fail_dec_button(self):
        QTest.mouseClick(self.window.ui.btnDec, Qt.LeftButton)
        self.assertNotEqual(self.window.ui.lbl_number.text(), "31")
        self.assertIn("color: red", self.window.ui.lbl_number.styleSheet())


if __name__ == "__main__":
    unittest.main()   

