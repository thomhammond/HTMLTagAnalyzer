from PyQt5 import QtWidgets, uic
from bs4 import BeautifulSoup as bs4
import requests, sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("HTMLTagAnalyzer.ui", self)
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        print("It's Alive...")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    sys.exit(app.exec())
