from PyQt5 import QtWidgets

import unittest

import HTMLTagAnalyzer

app = QtWidgets.QApplication([])


class TestApp(unittest.TestCase):
    def setUp(self):
        self.win = HTMLTagAnalyzer.App()

    def test_parseHTML_returns_correct_true_value(self):
        self.assertTrue(self.win.parseHTML("https://www.google.com/"))

    def test_parseHTML_returns_correct_false_value_1(self):
        self.assertFalse(self.win.parseHTML("www.google.com"))

    def test_parseHTML_returns_correct_false_value_2(self):
        self.assertFalse(self.win.parseHTML("invalidString"))


if __name__ == '__main__':
    unittest.main()


