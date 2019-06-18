import sys
import unittest
from PyQt5 import QtWidgets
from PyQt5 import QtTest
from PyQt5 import QtCore

import HTMLTagAnalyzer

app = QtWidgets.QApplication(sys.argv)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.win = HTMLTagAnalyzer.App()
        self.analyzeButton = self.win.pushButton

    # test GUI state on 'analyze' button click with no input
    def test_analyze_button_1(self):
        # click button
        QtTest.QTest.mouseClick(self.analyzeButton, QtCore.Qt.LeftButton)

        # test URL input is an empty string
        self.assertEqual(self.win.lineEdit.text(), '')
        # test table label is set to 'Invalid Entry'
        self.assertEqual(self.win.label_2.text(), 'Invalid Entry')

    # test GUI state on 'analyze' button click with valid input
    def test_analyze_button_2(self):
        # create valid input
        self.win.lineEdit.setText('https://www.google.com/')

        # click button
        QtTest.QTest.mouseClick(self.analyzeButton, QtCore.Qt.LeftButton)

        # test URL input has been cleared
        self.assertEqual(self.win.lineEdit.text(), '')
        # test table label is set to 'Invalid Entry'
        self.assertEqual(self.win.label_2.text(), 'google.com')

    # test GUI state on 'analyze' button click with invalid input 'www.google.com'
    def test_analyze_button_3(self):
        # create valid input
        self.win.lineEdit.setText('www.google.com')

        # click button
        QtTest.QTest.mouseClick(self.analyzeButton, QtCore.Qt.LeftButton)

        # test URL input has been cleared
        self.assertEqual(self.win.lineEdit.text(), '')
        # test table label is set to 'Invalid Entry'
        self.assertEqual(self.win.label_2.text(), 'Invalid Entry')

    # test GUI state on 'analyze' button click with invalid input 'invalidString'
    def test_analyze_button_4(self):
        # create invalid input
        self.win.lineEdit.setText('invalidString')

        # click button
        QtTest.QTest.mouseClick(self.analyzeButton, QtCore.Qt.LeftButton)

        # test URL input is an empty string
        self.assertEqual(self.win.lineEdit.text(), '')
        # test table label is set to 'Invalid Entry'
        self.assertEqual(self.win.label_2.text(), 'Invalid Entry')

    def test_parseHTML_returns_correct_true_value(self):
        self.assertTrue(self.win.parseHTML("https://www.google.com/"))

    def test_parseHTML_returns_correct_false_value_1(self):
        self.assertFalse(self.win.parseHTML("www.google.com"))

    def test_parseHTML_returns_correct_false_value_2(self):
        self.assertFalse(self.win.parseHTML("invalidString"))


if __name__ == '__main__':
    unittest.main()


