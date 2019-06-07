from PyQt5 import QtWidgets, uic
from bs4 import BeautifulSoup as Bs4
import requests
import sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("HTMLTagAnalyzer.ui", self)
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        url = self.lineEdit.text()
        parseHTML(url)


def parseHTML(url):
    page = requests.get(url)
    soup = Bs4(page.content, 'html.parser')

    tagDict = {}

    for tag in soup.findAll():
        if tag.name in tagDict.keys():
            tagDict[tag.name] += 1
        else:
            tagDict[tag.name] = 1

    # To be removed, testing return values are correct
    for keys, values in tagDict.items():
        print(keys)
        print(values)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    sys.exit(app.exec())
